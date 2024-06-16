from rest_framework import serializers

from gallery.models import FileGallery
from yekjamodir.settings import BASE_URL


class FileGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = FileGallery
        fields = "__all__"

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['link'] = f"{BASE_URL}{instance.file.url}".replace('//', '/')
        return ret
