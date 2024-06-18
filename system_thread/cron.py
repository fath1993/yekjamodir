import jdatetime

from custom_logs.models import custom_log
from system_thread.models import SystemThreadIsActive
from system_thread.views import CheckSystemThread

"""
crontab task start
"""


def check_system_thread_is_active():
    now = jdatetime.datetime.now()
    now_minus_three_minute = now - jdatetime.timedelta(minutes=3)
    threads = SystemThreadIsActive.objects.filter()
    if threads.count() == 0:
        thread = SystemThreadIsActive.objects.create()
    else:
        thread = threads.latest('id')
    if not now_minus_three_minute < thread.updated_at < now:
        custom_log("start CheckSystemThread")
        CheckSystemThread(name='check_system_thread').start()


"""
crontab task end
"""
