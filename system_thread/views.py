import threading
import time
import jdatetime
from auto_robots.tasks import OnceMessengerThread, DailyMessengerThread, MonthlyMessengerThread
from custom_logs.models import custom_log
from subscription.tasks import RefreshSubscriptionThread
from system_thread.models import SystemThreadIsActive


class CheckSystemThread(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self._name = name

    def run(self):
        custom_log("CheckSystemThread: start thread")
        while True:
            now = jdatetime.datetime.now()
            now_minus_three_minute = now - jdatetime.timedelta(minutes=3)
            thread = SystemThreadIsActive.objects.filter().latest('id')

            if not now_minus_three_minute < thread.updated_at < now:
                custom_log("start OnceMessengerThread", "d")
                OnceMessengerThread(name='once_messenger_thread').start()
                time.sleep(1)

                custom_log("start DailyMessengerThread", "d")
                DailyMessengerThread(name='daily_messenger_thread').start()
                time.sleep(1)

                custom_log("start MonthlyMessengerThread", "d")
                MonthlyMessengerThread(name='monthly_messenger_thread').start()
                time.sleep(1)

                custom_log("start RefreshSubscriptionThread", "d")
                RefreshSubscriptionThread(name='refresh_subscription_thread').start()
                time.sleep(1)

            thread.save()
            time.sleep(60)
