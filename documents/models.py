from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django_jalali.db import models as jmodels
from tinymce.models import HTMLField

from accounts.models import Profile
from gallery.models import FileGallery


class Folder(models.Model):
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='پوشه مادر')
    title = models.CharField(default='New folder', max_length=255, null=False, blank=False, verbose_name='عنوان')
    created_at = jmodels.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    created_by = models.ForeignKey(User, related_name='folder_created_by', on_delete=models.CASCADE, null=False,
                                   editable=False, verbose_name='کاربر سازنده')

    def __str__(self):
        return self.title + " | " + str(self.id)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "1 - فولدر"
        verbose_name_plural = "1 - فولدر ها"


class Document(models.Model):
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, null=False, blank=False, verbose_name='پوشه')
    title = models.CharField(max_length=255, null=False, blank=False, verbose_name='عنوان')
    description = models.CharField(max_length=255, null=False, blank=False, verbose_name='توضیحات')
    files = models.ManyToManyField(FileGallery, blank=True, verbose_name='فایل ها')
    content = HTMLField(null=True, blank=True, verbose_name='محتوای سند')
    allowed_to = models.ManyToManyField(User, related_name='document_edit_allowed_to', blank=True, verbose_name='اجازه دسترسی به')
    created_at = jmodels.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated_at = jmodels.jDateTimeField(auto_now=True, verbose_name='تاریخ بروز رسانی')
    created_by = models.ForeignKey(User, related_name='document_created_by', on_delete=models.CASCADE,
                                   null=False, editable=False,
                                   verbose_name='کاربر سازنده')
    document_parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True,
                                        editable=False, verbose_name='پرونده مادر')

    def __str__(self):
        return self.folder.title + ' | ' + self.title

    class Meta:
        ordering = ['-updated_at', ]
        verbose_name = "2 - سند"
        verbose_name_plural = "2 - اسناد"

    def get_absolute_url(self):
        return reverse('documents:document-edit', kwargs={'document_id': self.id})
