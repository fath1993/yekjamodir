import time

import jdatetime
from django.contrib.auth.models import User
from django.core.management import base

from auto_robots.cron_jobs import cron_jobs
from auto_robots.tests import test_send_message


class Command(base.BaseCommand):
    def handle(self, *args, **options):
        print('please choose: (1. cron_jobs, 2.send_test)')
        choice = int(input())
        if choice == 1:
            cron_jobs()
        else:
            while True:
                print('please input bot_token:')
                bot_token = str(input())
                print('please input action: (new_send, republish, revise, delete)')
                action = str(input())
                print('please input message_status: (sent, queued)')
                message_status = str(input())
                print('please input metapost_view_type: (simple_text, photo, video)')
                metapost_view_type = str(input())
                test_send_message(bot_token, action, message_status, metapost_view_type)
