import threading
import time

import jdatetime

from accounts.models import Profile, Invoice
from custom_logs.models import custom_log
from subscription.models import LicenceSetting


class RefreshSubscriptionThread(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self._name = name

    def run(self):
        while True:
            try:
                custom_log('refresh_subscription_thread has been started')
                licence_setting = LicenceSetting.objects.filter().latest('id')
                now = jdatetime.datetime.now()
                midnight = jdatetime.datetime(year=now.year, month=now.month, day=now.day, hour=0, minute=0)
                if now == midnight:
                    for profile in Profile.objects.all():
                        get_profile = Profile.objects.get(id=profile.id)
                        if get_profile.financial_licence:
                            if get_profile.wallet_balance > licence_setting.financial_licence_price:
                                get_profile.wallet_balance -= licence_setting.financial_licence_price
                                invoice = Invoice.objects.create(
                                    invoice_type='برداشت از حساب',
                                    user=get_profile.user,
                                    amount=licence_setting.financial_licence_price,
                                    description='برداشت خودکار بابت سرویس روزانه اشتراک مالی',
                                    authority='financial_licence',
                                    ref_id='financial_licence',
                                    status='پرداخت شده',
                                    created_by=get_profile.user,
                                )
                                get_profile.save()
                            else:
                                get_profile.financial_licence = False
                                get_profile.save()
                        get_profile = Profile.objects.get(id=profile.id)
                        if get_profile.social_licence:
                            if get_profile.wallet_balance > licence_setting.social_licence_price:
                                get_profile.wallet_balance -= licence_setting.social_licence_price
                                invoice = Invoice.objects.create(
                                    invoice_type='برداشت از حساب',
                                    user=get_profile.user,
                                    amount=licence_setting.social_licence_price,
                                    description='برداشت خودکار بابت سرویس روزانه اشتراک شبکه های اجتماعی',
                                    authority='social_licence',
                                    ref_id='social_licence',
                                    status='پرداخت شده',
                                    created_by=get_profile.user,
                                )
                                get_profile.save()
                            else:
                                get_profile.social_licence = False
                                get_profile.save()
                custom_log('refresh_subscription_thread has been finished.')
            except Exception as e:
                custom_log(f'{e}')
            time.sleep(60)
