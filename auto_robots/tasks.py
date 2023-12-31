import json
from django.http import JsonResponse
from django.views import View
from custom_logs.models import custom_log
import threading
import time
import jdatetime
from auto_robots.models import MetaPost
from utilities.messengers.messenger import messenger


class StartTaskView(View):
    def __init__(self):
        super().__init__()

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_superuser:
            StartTasksThread().start()
            return JsonResponse({'message': 'has started'})
        else:
            return JsonResponse({'message': 'not authorized'})


class StartTasksThread(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        active_threads = threading.enumerate()
        threads_name_list = []
        for thread in active_threads:
            if thread.is_alive():
                threads_name_list.append(str(thread.name))
        custom_log(json.dumps(threads_name_list))

        if not 'messenger_thread' in threads_name_list:
            custom_log("general_functions: start MessengerThread", "d")
            MessengerThread(name='messenger_thread').start()


class MessengerThread(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self._name = name

    def run(self):
        custom_log('messenger cron thread has been started')
        while True:
            now = jdatetime.datetime.now()
            now_plus_30_seconds = now + jdatetime.timedelta(seconds=30)
            custom_log(f'time: {now.strftime("%Y/%m/%d %H:%M")} to {now_plus_30_seconds.strftime("%Y/%m/%d %H:%M")}')
            metaposts_one_time = MetaPost.objects.filter(message_status='queued',
                                                         send_at__range=[now, now_plus_30_seconds])
            for metapost_one_time in metaposts_one_time:
                if not metapost_one_time.is_send_hourly_at_active and not metapost_one_time.is_send_daily_at_active and not metapost_one_time.is_send_monthly_at_active and not metapost_one_time.is_send_yearly_at_active:
                    if metapost_one_time.action == 'new_send':
                        metapost_one_time.message_status = 'sent'
                    elif metapost_one_time.action == 'delete':
                        metapost_one_time.message_status = 'deleted'
                    elif metapost_one_time.action == 'revise':
                        metapost_one_time.message_status = 'revised'
                    elif metapost_one_time.action == 'republish':
                        metapost_one_time.message_status = 'republished'
                    metapost_one_time.save()
                messenger(metapost_one_time)
                time.sleep(1)
            custom_log(metaposts_one_time)
            metaposts_hourly = MetaPost.objects.filter(message_status='queued', is_send_hourly_at_active=True,
                                                       send_hourly_at=now.minute)
            for metapost_hourly in metaposts_hourly:
                messenger(metapost_hourly)
                time.sleep(1)
            custom_log(metaposts_hourly)
            metaposts_daily = MetaPost.objects.filter(message_status='queued', is_send_daily_at_active=True,
                                                      send_daily_at__hour=now.hour,
                                                      send_daily_at__minute=now.minute)
            for metapost_daily in metaposts_daily:
                messenger(metapost_daily)
                time.sleep(1)
            custom_log(metaposts_daily)
            metaposts_monthly = MetaPost.objects.filter(message_status='queued', is_send_monthly_at_active=True,
                                                        send_monthly_at__day=now.day,
                                                        send_monthly_at__hour=now.hour,
                                                        send_monthly_at__minute=now.minute)
            for metapost_monthly in metaposts_monthly:
                messenger(metapost_monthly)
                time.sleep(1)
            custom_log(metaposts_monthly)
            metaposts_yearly = MetaPost.objects.filter(message_status='queued', is_send_yearly_at_active=True,
                                                       send_yearly_at__month=now.month,
                                                       send_yearly_at__day=now.day,
                                                       send_yearly_at__hour=now.hour,
                                                       send_yearly_at__minute=now.minute)
            for metapost_yearly in metaposts_yearly:
                messenger(metapost_yearly)
                time.sleep(1)
            custom_log(metaposts_yearly)
            custom_log('messenger cron thread has been finished. we are waiting for 5 seconds')
            time.sleep(5)
