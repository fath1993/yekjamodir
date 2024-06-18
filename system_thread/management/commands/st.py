import time

import jdatetime
from django.contrib.auth.models import User
from django.core.management import base

from auto_robots.tests import test_send_message
from system_thread.cron import check_system_thread_is_active


class Command(base.BaseCommand):
    def handle(self, *args, **options):
        check_system_thread_is_active()
