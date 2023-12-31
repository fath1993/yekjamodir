import os
import csv

from django.contrib.auth.models import User
from django.core.management import base

import re

from blog.models import EitaaBot
from financial_accounting.models import TransactionRecord, FinancialAccount, FinancialBroker
from gallery.models import FileGallery


class Command(base.BaseCommand):
    def handle(self, *args, **options):
        fb = EitaaBot.objects.filter()[0]
        fb.created_by = User.objects.get(id=2)
        fb.save()
