import json

from django.core.management import base
import requests
import zipfile
import io

from accounts.models import Profile
from blog.models import MagicWord, Blog
from utilities.arvancloud import CreateCnameThread


class Command(base.BaseCommand):
    def handle(self, *args, **options):
        profile = Profile.objects.filter()
        for prof in profile:
            prof.profile_pic = None
            prof.save()


