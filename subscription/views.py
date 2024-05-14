import json

import jdatetime
import requests
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from accounts.models import Invoice, Profile
from subscription.models import LicenceSetting, VIPPlan
from utilities.http_metod import fetch_data_from_http_post
from yekjamodir.settings import ZARINPAL_API_KEY, BASE_URL


class SubscriptionView:
    def __init__(self):
        super().__init__()

    def invoice_list(self, request, *args, **kwargs):
        context = {'page_title': 'سوابق مالی حساب',
                   'breadcrumb_1': 'خانه',
                   'breadcrumb_2': 'مالی',
                   'get_params': request.GET.urlencode()}

        if not request.user.is_authenticated:
            return redirect('accounts:login')

        invoices = Invoice.objects.filter(created_by=request.user).order_by('-created_at')
        context['invoices'] = invoices

        items_per_page = 10
        paginator = Paginator(invoices, items_per_page)
        context['paginator'] = paginator
        page_number = request.GET.get('page')
        page = paginator.get_page(page_number)
        context['page'] = page

        return render(request, 'subscription/invoices-list.html', context)

    def charge_credit(self, request, *args, **kwargs):
        context = {'page_title': 'شارژ اعتبار حساب',
                   'breadcrumb_1': 'خانه',
                   'breadcrumb_2': 'مالی',
                   'get_params': request.GET.urlencode()}

        if not request.user.is_authenticated:
            return redirect('accounts:login')

        licence_setting = LicenceSetting.objects.filter().latest('id')
        context['licence_setting'] = licence_setting
        vip_plans = VIPPlan.objects.all()
        context['vip_plans'] = vip_plans

        if request.method == 'GET':
            return render(request, 'subscription/charge-account.html', context)

        if request.method == 'POST':
            charge_amount = fetch_data_from_http_post(request, 'charge_amount', context)
            try:
                charge_amount = int(charge_amount)
                charge_amount_allowed_list = []
                for vip_plan in vip_plans:
                    charge_amount_allowed_list.append(vip_plan.price)
                if not charge_amount in charge_amount_allowed_list:
                    return JsonResponse({'message': 'not allowed'})
            except:
                return JsonResponse({'message': 'not allowed'})

            new_invoice = Invoice.objects.create(
                user=request.user,
                amount=int(charge_amount * ((licence_setting.tax_percent + 100) / 100)),
                tax=int(charge_amount * (licence_setting.tax_percent / 100)),
                description='شارژ اعتبار حساب',
                authority='',
                ref_id='',
                status='پرداخت نشده',
                created_by=request.user,
            )

            try:
                url = 'https://api.zarinpal.com/pg/v4/payment/request.json'
                header = {'Content-Type': 'application/json', 'accept': 'application/json'}
                data = {
                    "merchant_id": ZARINPAL_API_KEY,
                    "amount": new_invoice.amount * 10,
                    # "callback_url": f'{BASE_URL}{reverse("subscription:charge-wallet-callback")}',
                    "callback_url": f'http://127.0.0.1:8000{reverse("subscription:charge-wallet-callback")}',
                    "description": f"فاکتور پرداختی توسط {request.user.username}",
                    "metadata": {"mobile": request.user.username}
                }
                pay_request = requests.post(url=url, data=json.dumps(data), headers=header)
                if pay_request.status_code == 200:
                    authority = pay_request.json()['data']["authority"]
                    new_invoice.authority = authority
                    new_invoice.save()
                    return redirect(f'https://www.zarinpal.com/pg/StartPay/{new_invoice.authority}')
                else:
                    new_invoice.delete()
                    context['error'] = 'ارتباط با درگاه پرداخت زرین پال ممکن نیست'
                    return render(request, 'subscription/charge-account.html', context)
            except Exception as e:
                print(e)
                new_invoice.delete()
                context['error'] = 'ارتباط با درگاه پرداخت زرین پال ممکن نیست'
                return render(request, 'subscription/charge-account.html', context)

    def charge_credit_callback(self, request, *args, **kwargs):
        context = {'page_title': 'شارژ اعتبار حساب',
                   'breadcrumb_1': 'خانه',
                   'breadcrumb_2': 'مالی',
                   'get_params': request.GET.urlencode()}
        try:
            authority = request.GET.get('Authority')
            invoice = Invoice.objects.get(authority=authority)
            context['invoice'] = invoice
            if invoice.status == 'پرداخت شده':
                return redirect('subscription:invoices-list')
            try:
                url = 'https://api.zarinpal.com/pg/v4/payment/verify.json'
                header = {'Content-Type': 'application/json', 'accept': 'application/json'}
                data = {
                    "merchant_id": ZARINPAL_API_KEY,
                    "amount": invoice.amount * 10,
                    "authority": authority
                }
                response = requests.post(url=url, json=data, headers=header)
                result = response.json()
                response_code = int(find_code(result, 'code'))
                response_message = zarinpal_error_response(response_code)
                try:
                    if response_code == 100 or response_code == 101:
                        ref_id = find_code(result, 'ref_id')
                        invoice.status = 'پرداخت شده'
                        invoice.description = f'{response_message}'
                        invoice.ref_id = ref_id
                        invoice.save()
                        if invoice.amount == 1100000:
                            context['charge_amount'] = '1 میلیون تومان'
                        else:
                            context['charge_amount'] = f'{invoice.amount} هزار تومان'
                        return render(request, 'subscription/pay-result/pay-success.html', context)
                    else:
                        invoice.description = f'{response_message}'
                        invoice.save()
                        context['error'] = f'{response_message}'
                        return render(request, 'subscription/pay-result/pay-fail.html', context)
                except Exception as e:
                    invoice.description = f'{response_message}'
                    invoice.save()
                    context['error'] = f'{response_message}'
                    return render(request, 'subscription/pay-result/pay-fail.html', context)
            except Exception as e:
                print(e)
                invoice.description = 'اشکال در احراز پرداخت'
                invoice.save()
                context['error'] = 'اشکال در احراز پرداخت'
                return render(request, 'subscription/pay-result/pay-fail.html', context)
        except Exception as e:
            return JsonResponse({'message': 'wrong argument'})

    def change_vip_plan(self, request, *args, **kwargs):
        context = {'page_title': 'تنظیمات اشتراک حساب',
                   'breadcrumb_1': 'خانه',
                   'breadcrumb_2': 'مالی',
                   'get_params': request.GET.urlencode()}

        if not request.user.is_authenticated:
            return redirect('accounts:login')

        licence_setting = LicenceSetting.objects.filter().latest('id')
        context['licence_setting'] = licence_setting

        if request.method == 'GET':
            profile = Profile.objects.get(user=request.user)
            context['profile'] = profile
            return render(request, 'subscription/vip-plan-activation.html', context)

        if request.method == 'POST':
            policy_agreement = fetch_data_from_http_post(request, 'policy_agreement', context)

            if policy_agreement == 'on':
                policy_agreement = True

            if not policy_agreement:
                context['error'] = f'تایید قوانین استفاده از اشتراک ها الزامی است'
                return render(request, 'subscription/vip-plan-activation.html', context)

            financial_licence = fetch_data_from_http_post(request, 'financial_licence', context)
            warehouse_licence = fetch_data_from_http_post(request, 'warehouse_licence', context)
            social_licence = fetch_data_from_http_post(request, 'social_licence', context)
            blog_licence = fetch_data_from_http_post(request, 'blog_licence', context)
            automation_licence = fetch_data_from_http_post(request, 'automation_licence', context)


            now = jdatetime.datetime.now()
            star_of_today = jdatetime.datetime(year=now.year, month=now.month, day=now.day, hour=0, minute=0, second=0)

            activated_service = f''''''
            deactivate_service = f''''''
            insufficient_balance = f''''''
            insufficient_balance_amount = 0

            profile = Profile.objects.get(user=request.user)
            if financial_licence == 'on':
                try:
                    invoice = Invoice.objects.get(authority='financial_licence', invoice_type='برداشت از حساب',
                                                  user=request.user, created_at__gte=star_of_today)
                    if not profile.financial_licence:
                        profile.financial_licence = True
                        activated_service += 'اشتراک مالی, '
                except:
                    if wallet_balance_is_sufficient(request, licence_setting.financial_licence_price):
                        profile.wallet_balance -= licence_setting.financial_licence_price
                        invoice = Invoice.objects.create(
                            invoice_type='برداشت از حساب',
                            user=request.user,
                            amount=licence_setting.financial_licence_price,
                            description='برداشت خودکار بابت سرویس روزانه اشتراک مالی',
                            authority='financial_licence',
                            ref_id='financial_licence',
                            status='پرداخت شده',
                            created_by=request.user,
                        )
                        if not profile.financial_licence:
                            profile.financial_licence = True
                            activated_service += 'اشتراک مالی, '
                    else:
                        insufficient_balance += 'اشتراک مالی, '
                        insufficient_balance_amount += licence_setting.financial_licence_price
                        profile.financial_licence = False
            else:
                if profile.financial_licence:
                    profile.financial_licence = False
                    deactivate_service += 'اشتراک مالی, '
            profile.save()

            profile = Profile.objects.get(user=request.user)
            if warehouse_licence == 'on':
                try:
                    invoice = Invoice.objects.get(authority='warehouse_licence', invoice_type='برداشت از حساب',
                                                  user=request.user, created_at__gte=star_of_today)
                    if not profile.warehouse_licence:
                        profile.warehouse_licence = True
                        activated_service += 'اشتراک انبار داری, '
                except:
                    if wallet_balance_is_sufficient(request, licence_setting.warehouse_licence_price):
                        profile.wallet_balance -= licence_setting.warehouse_licence_price
                        invoice = Invoice.objects.create(
                            invoice_type='برداشت از حساب',
                            user=request.user,
                            amount=licence_setting.warehouse_licence_price,
                            description='برداشت خودکار بابت سرویس روزانه اشتراک انبار داری',
                            authority='warehouse_licence',
                            ref_id='warehouse_licence',
                            status='پرداخت شده',
                            created_by=request.user,
                        )
                        if not profile.warehouse_licence:
                            profile.warehouse_licence = True
                            activated_service += 'اشتراک انبار داری, '
                    else:
                        insufficient_balance += 'اشتراک انبار داری, '
                        insufficient_balance_amount += licence_setting.warehouse_licence_price
                        profile.warehouse_licence = False
            else:
                if profile.warehouse_licence:
                    profile.warehouse_licence = False
                    deactivate_service += 'اشتراک انبار داری, '
            profile.save()

            profile = Profile.objects.get(user=request.user)
            if social_licence == 'on':
                try:
                    invoice = Invoice.objects.get(authority='social_licence', invoice_type='برداشت از حساب',
                                                  user=request.user, created_at__gte=star_of_today)
                    if not profile.social_licence:
                        profile.social_licence = True
                        activated_service += 'اشتراک شبکه های اجتماعی, '
                except:
                    if wallet_balance_is_sufficient(request, licence_setting.social_licence_price):
                        profile.wallet_balance -= licence_setting.social_licence_price
                        invoice = Invoice.objects.create(
                            invoice_type='برداشت از حساب',
                            user=request.user,
                            amount=licence_setting.social_licence_price,
                            description='برداشت خودکار بابت سرویس روزانه اشتراک شبکه های اجتماعی',
                            authority='social_licence',
                            ref_id='social_licence',
                            status='پرداخت شده',
                            created_by=request.user,
                        )
                        if not profile.social_licence:
                            profile.social_licence = True
                            activated_service += 'اشتراک شبکه های اجتماعی, '
                    else:
                        insufficient_balance += 'اشتراک شبکه های اجتماعی, '
                        insufficient_balance_amount += licence_setting.social_licence_price
                        profile.social_licence = False
            else:
                if profile.social_licence:
                    profile.social_licence = False
                    deactivate_service += 'اشتراک شبکه های اجتماعی, '
            profile.save()

            profile = Profile.objects.get(user=request.user)
            if blog_licence == 'on':
                try:
                    invoice = Invoice.objects.get(authority='blog_licence', invoice_type='برداشت از حساب',
                                                  user=request.user, created_at__gte=star_of_today)
                    if not profile.blog_licence:
                        profile.blog_licence = True
                        activated_service += 'اشتراک بلاگ, '
                except:
                    if wallet_balance_is_sufficient(request, licence_setting.blog_licence_price):
                        profile.wallet_balance -= licence_setting.blog_licence_price
                        invoice = Invoice.objects.create(
                            invoice_type='برداشت از حساب',
                            user=request.user,
                            amount=licence_setting.blog_licence_price,
                            description='برداشت خودکار بابت سرویس روزانه اشتراک بلاگ',
                            authority='blog_licence',
                            ref_id='blog_licence',
                            status='پرداخت شده',
                            created_by=request.user,
                        )
                        if not profile.blog_licence:
                            profile.blog_licence = True
                            activated_service += 'اشتراک بلاگ, '
                    else:
                        insufficient_balance += 'اشتراک بلاگ, '
                        insufficient_balance_amount += licence_setting.blog_licence_price
                        profile.blog_licence = False
            else:
                if profile.blog_licence:
                    profile.blog_licence = False
                    deactivate_service += 'اشتراک بلاگ, '
            profile.save()

            profile = Profile.objects.get(user=request.user)
            if automation_licence == 'on':
                try:
                    invoice = Invoice.objects.get(authority='automation_licence', invoice_type='برداشت از حساب',
                                                  user=request.user, created_at__gte=star_of_today)
                    if not profile.automation_licence:
                        profile.automation_licence = True
                        activated_service += 'اشتراک اتوماسیون, '
                except:
                    if wallet_balance_is_sufficient(request, licence_setting.automation_licence_price):
                        profile.wallet_balance -= licence_setting.automation_licence_price
                        invoice = Invoice.objects.create(
                            invoice_type='برداشت از حساب',
                            user=request.user,
                            amount=licence_setting.automation_licence_price,
                            description='برداشت خودکار بابت سرویس روزانه اشتراک اتوماسیون',
                            authority='automation_licence',
                            ref_id='automation_licence',
                            status='پرداخت شده',
                            created_by=request.user,
                        )
                        if not profile.automation_licence:
                            profile.automation_licence = True
                            activated_service += 'اشتراک اتوماسیون, '
                    else:
                        insufficient_balance += 'اشتراک اتوماسیون, '
                        insufficient_balance_amount += licence_setting.automation_licence_price
                        profile.automation_licence = False
            else:
                if profile.automation_licence:
                    profile.automation_licence = False
                    deactivate_service += 'اشتراک اتوماسیون, '
            profile.save()

            if activated_service != '':
                context['message'] = f'{activated_service} فعالسازی گردید.'
            if deactivate_service != '':
                context['message_2'] = f'{deactivate_service} غیر فعال گردید.'
            if insufficient_balance != '':
                context['error'] = f'{insufficient_balance} به دلیل کمود اعتبار حساب فعالسازی نگردید. ابتدا حساب خود را به مقدار {insufficient_balance_amount} تومان برای یک روز شارژ نمایید.'
            profile = Profile.objects.get(user=request.user)
            context['profile'] = profile
            return render(request, 'subscription/vip-plan-activation.html', context)


def zarinpal_error_response(code):
    responses = {
        -9: "خطای اعتبار سنجی",
        -10: "ای پی یا مرچنت كد پذیرنده صحیح نیست.",
        -11: "مرچنت کد فعال نیست، پذیرنده مشکل خود را به امور مشتریان زرین‌پال ارجاع دهد.",
        -12: "تلاش بیش از دفعات مجاز در یک بازه زمانی کوتاه به امور مشتریان زرین پال اطلاع دهید",
        -15: "درگاه پرداخت به حالت تعلیق در آمده است، پذیرنده مشکل خود را به امور مشتریان زرین‌پال ارجاع دهد.",
        -16: "سطح تایید پذیرنده پایین تر از سطح نقره ای است.",
        -17: "محدودیت پذیرنده در سطح آبی",
        100: "عملیات موفق",
        -30: "پذیرنده اجازه دسترسی به سرویس تسویه اشتراکی شناور را ندارد.",
        -31: "حساب بانکی تسویه را به پنل اضافه کنید. مقادیر وارد شده برای تسهیم درست نیست. پذیرنده جهت استفاده از خدمات سرویس تسویه اشتراکی شناور، باید حساب بانکی معتبری به پنل کاربری خود اضافه نماید.",
        -32: "مبلغ وارد شده از مبلغ کل تراکنش بیشتر است.",
        -33: "درصدهای وارد شده صحیح نیست.",
        -34: "مبلغ وارد شده از مبلغ کل تراکنش بیشتر است.",
        -35: "تعداد افراد دریافت کننده تسهیم بیش از حد مجاز است.",
        -36: "حداقل مبلغ جهت تسهیم باید ۱۰۰۰۰ ریال باشد.",
        -37: "یک یا چند شماره شبای وارد شده برای تسهیم از سمت بانک غیر فعال است.",
        -38: "خطا، عدم تعریف صحیح شبا، لطفاً دقایقی دیگر تلاش کنید.",
        -39: "خطایی رخ داده است، به امور مشتریان زرین پال اطلاع دهید.",
        -40: "پارامترهای اضافی نامعتبر، expire_in نامعتبر است.",
        -41: "حداکثر مبلغ پرداختی ۱۰۰ میلیون تومان است.",
        -50: "مبلغ پرداخت شده با مقدار مبلغ ارسالی در متد وریفای متفاوت است.",
        -51: "پرداخت ناموفق",
        -52: "خطای غیر منتظره‌ای رخ داده است. پذیرنده مشکل خود را به امور مشتریان زرین‌پال ارجاع دهد.",
        -53: "پرداخت متعلق به این مرچنت کد نیست.",
        -54: "اتوریتی نامعتبر است.",
        -55: "تراکنش مورد نظر یافت نشد.",
        101: "تراکنش وریفای شده است."
    }
    return responses[code]


def find_code(response, key_lookup):
    for key, value in response.items():
        if key == f'{key_lookup}':
            return value
        elif isinstance(value, dict):
            code = find_code(value, key_lookup)
            if code is not None:
                return code
    return None


def wallet_balance_is_sufficient(request, withdraw_amount):
    profile = request.user.profile_user

    if profile.wallet_balance > withdraw_amount:
        return True
    else:
        return False


