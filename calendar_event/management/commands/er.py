from django.core.management import base

from calendar_event.event_reminder import event_reminder
from gallery.models import FileGallery


class Command(base.BaseCommand):
    def handle(self, *args, **options):
        FileGallery.objects.all().delete()
