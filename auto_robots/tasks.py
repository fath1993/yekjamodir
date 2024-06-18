import json
import random
import uuid
from custom_logs.models import custom_log
import threading
import time
import jdatetime
from auto_robots.models import MetaPost
from utilities.messengers.messenger import messenger



class OnceMessengerThread(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self._name = name

    def run(self):
        try:
            custom_log('once_messenger_thread has been started')
            now = jdatetime.datetime.now()
            now_plus_15_minute = now + jdatetime.timedelta(minutes=15)
            custom_log(f'time: {now.strftime("%Y/%m/%d %H:%M")} to {now_plus_15_minute.strftime("%Y/%m/%d %H:%M")}')
            metaposts_one_time = MetaPost.objects.filter(send_at_type='زمانبندی شده یکباره', message_status='queued',
                                                         send_at_date_time__range=[now, now_plus_15_minute])
            metapost_unhandled_list = []
            for metapost_one_time in metaposts_one_time:
                metapost_unhandled_list.append(metapost_one_time)
            while True:
                handled_list = []
                now = jdatetime.datetime.now()
                now_plus_15_seconds = now + jdatetime.timedelta(seconds=15)
                now_minus_15_seconds = now - jdatetime.timedelta(seconds=15)
                for unhandled_metapost in metapost_unhandled_list:
                    if now_minus_15_seconds < unhandled_metapost.send_at_date_time < now_plus_15_seconds:
                        if unhandled_metapost.action == 'new_send':
                            unhandled_metapost.message_status = 'sent'
                        elif unhandled_metapost.action == 'delete':
                            unhandled_metapost.message_status = 'deleted'
                        elif unhandled_metapost.action == 'revise':
                            unhandled_metapost.message_status = 'revised'
                        elif unhandled_metapost.action == 'republish':
                            unhandled_metapost.message_status = 'republished'
                        unhandled_metapost.save()
                        EachMessengerThread(str(uuid.uuid4()), unhandled_metapost).start()
                        handled_list.append(unhandled_metapost)
                for handled_metapost in handled_list:
                    metapost_unhandled_list.remove(handled_metapost)
                if len(metapost_unhandled_list) == 0:
                    break
                time.sleep(1)
            custom_log('once_messenger_thread has been finished.')
        except Exception as e:
            custom_log(f'{e}')
        return


# class WeeklyMessengerThread(threading.Thread):
#     def __init__(self, name):
#         super().__init__()
#         self._name = name
#
#     def run(self):
#         custom_log('messenger cron thread has been started')
#         while True:
#             now = jdatetime.datetime.now()
#             now_plus_30_minute = now + jdatetime.timedelta(minutes=30)
#             custom_log(f'time: {now.strftime("%Y/%m/%d %H:%M")} to {now_plus_30_minute.strftime("%Y/%m/%d %H:%M")}')
#             metaposts_one_time = MetaPost.objects.filter(send_at_type='زمانبندی شده یکباره', message_status='queued',
#                                                          send_at_date_time__range=[now, now_plus_30_minute])
#             for metapost_one_time in metaposts_one_time:
#                 if not metapost_one_time.is_send_hourly_at_active and not metapost_one_time.is_send_daily_at_active and not metapost_one_time.is_send_monthly_at_active and not metapost_one_time.is_send_yearly_at_active:
#                     if metapost_one_time.action == 'new_send':
#                         metapost_one_time.message_status = 'sent'
#                     elif metapost_one_time.action == 'delete':
#                         metapost_one_time.message_status = 'deleted'
#                     elif metapost_one_time.action == 'revise':
#                         metapost_one_time.message_status = 'revised'
#                     elif metapost_one_time.action == 'republish':
#                         metapost_one_time.message_status = 'republished'
#                     metapost_one_time.save()
#                 EachMessengerThread(str(uuid.uuid4()), metapost_one_time).start()
#             custom_log(metaposts_one_time)
#
#             metaposts_daily = MetaPost.objects.filter(send_at_type='روزانه',
#                                                       send_at_date_time__hour=now.hour,
#                                                       send_at_date_time__minute=now.minute)
#             for metapost_daily in metaposts_daily:
#                 EachMessengerThread(str(uuid.uuid4()), metapost_daily).start()
#             custom_log(metaposts_daily)
#
#             metaposts_monthly = MetaPost.objects.filter(send_at_type='ماهانه',
#                                                         send_at_date_time__day=now.day,
#                                                         send_at_date_time__hour=now.hour,
#                                                         send_at_date_time__minute=now.minute)
#             for metapost_monthly in metaposts_monthly:
#                 EachMessengerThread(str(uuid.uuid4()), metapost_monthly).start()
#             custom_log(metaposts_monthly)
#             metaposts_yearly = MetaPost.objects.filter(send_at_type='سالانه',
#                                                        send_at_date_time__month=now.month,
#                                                        send_at_date_time__day=now.day,
#                                                        send_at_date_time__hour=now.hour,
#                                                        send_at_date_time__minute=now.minute)
#             for metapost_yearly in metaposts_yearly:
#                 EachMessengerThread(str(uuid.uuid4()), metapost_yearly).start()
#             custom_log(metaposts_yearly)
#             custom_log('messenger cron thread has been finished. we are waiting for 30 minute')
#             time.sleep(900)


class DailyMessengerThread(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self._name = name

    def run(self):
        try:
            custom_log('daily_messenger_thread has been started')
            now = jdatetime.datetime.now()
            metaposts_daily = MetaPost.objects.filter(send_at_type='روزانه',
                                                      send_at_date_time__hour=now.hour,
                                                      send_at_date_time__minute=now.minute)
            for metapost_daily in metaposts_daily:
                EachMessengerThread(str(uuid.uuid4()), metapost_daily).start()
            custom_log('daily_messenger_thread has been finished.')
        except Exception as e:
            custom_log(f'{e}')
        return



class MonthlyMessengerThread(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self._name = name

    def run(self):
        try:
            custom_log('monthly_messenger_thread has been started')
            now = jdatetime.datetime.now()
            metaposts_monthly = MetaPost.objects.filter(send_at_type='ماهانه',
                                                        send_at_date_time__day=now.day,
                                                        send_at_date_time__hour=now.hour,
                                                        send_at_date_time__minute=now.minute)
            for metapost_monthly in metaposts_monthly:
                EachMessengerThread(str(uuid.uuid4()), metapost_monthly).start()
            custom_log('monthly_messenger_thread has been finished.')
        except Exception as e:
            custom_log(f'{e}')
        return



class EachMessengerThread(threading.Thread):
    def __init__(self, name, metaposts):
        super().__init__()
        self._name = name
        self.metaposts = metaposts

    def run(self):
        try:
            time.sleep(random.randint(0, 100) / 100)
            messenger(self.metaposts)
        except Exception as e:
            custom_log(f'{e}')
        return
