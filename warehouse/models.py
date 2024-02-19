import datetime

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_jalali.db import models as jmodels
from gallery.models import FileGallery
from accounts.models import Profile

PROPERTY_CONDITION = (('آکبند','آکبند'), ('در حد نو','در حد نو'), ('کار کرده با وضعیت خوب', 'کار کرده با وضعیت خوب'), ('کار کرده با وضعیت بد', 'کار کرده با وضعیت بد'), ('خراب','خراب'))

DIGITAL_PROPERTY_TYPE = (('رم', 'رم'), ('مادر بورد', 'مادر بورد'), ('کیس', 'کیس'), ('پاور', 'پاور'),
                         ('سی دی', 'سی دی'), ('هارد', 'هارد'), ('سی پی یو', 'سی پی یو'), ('مانیتور', 'مانیتور'),
                         ('کارت گرافیک', 'کارت گرافیک'), ('سایر', 'سایر'))

HOUSE_PROPERTY_TYPE = (('لوازم خانگی', 'لوازم خانگی'), ('لوازم اداری', 'لوازم اداری'),)


CULTURAL_PROPERTY_TYPE = (('کتاب', 'کتاب'), ('مجله', 'مجله'), ('بنر', 'بنر'), ('یادبود', 'یادبود'), ('سایر', 'سایر'),)


class Property(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False, verbose_name='عنوان')
    description = models.TextField(null=True, blank=True, verbose_name='توضیحات')
    buying_price = models.PositiveIntegerField(default=0, blank=True, verbose_name='قیمت خرید')
    condition = models.CharField(max_length=255, default='آکبند', choices=PROPERTY_CONDITION, blank=True, verbose_name='شرایط عمومی کالا')
    images = models.ManyToManyField(FileGallery, blank=True, verbose_name='فیلم و تصویر از کالا')
    registration_code = models.CharField(max_length=255, null=False, blank=False, verbose_name='کد ثبت کالا', help_text='در صورت تغییر کد مشخصات کاربر تغییر دهنده ذخیره می گردد')  ## must be tracked anonymously if changed
    property_assigned_to = models.ForeignKey(Profile, limit_choices_to={'user__is_superuser': True}, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='کالا تحویل شده به')
    date_of_assignment = jmodels.jDateTimeField(null=True, blank=True, verbose_name='تاریخ تحویل')
    date_of_return = jmodels.jDateTimeField(null=True, blank=True, verbose_name='تاریخ بازگشت')
    location = models.CharField(max_length=255, null=False, blank=False, verbose_name='محل قرار گیری')
    created_at = jmodels.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated_at = jmodels.jDateTimeField(auto_now=True, verbose_name='تاریخ بروز رسانی')
    created_by = models.ForeignKey(User, related_name='%(app_label)s_%(class)s_property_created_by', on_delete=models.SET_NULL, null=True, editable=False, verbose_name='ساخته شده توسط')
    updated_by = models.ForeignKey(User, related_name='%(app_label)s_%(class)s_property_updated_by', on_delete=models.SET_NULL, null=True, editable=False, verbose_name='آخرین اصلاح توسط')

    def __str__(self):
        return 'ID' + str(self.id) + ' - ' + self.title

    class Meta:
        abstract = True


class DigitalProperty(Property):
    digital_property_type = models.CharField(max_length=255, choices=DIGITAL_PROPERTY_TYPE, verbose_name='نوع کالا')
    serial_code_1 = models.CharField(max_length=255, null=False, blank=False, verbose_name='سریال')
    serial_code_2 = models.CharField(max_length=255, null=True, blank=True, verbose_name='سریال دوم در صورت وجود')
    warranty_company = models.CharField(max_length=255, default='بدون گارانتی', null=False, blank=True, verbose_name='نام شرکت گارانتی کننده')
    warranty_expiration_date = jmodels.jDateTimeField(null=True,blank=True, verbose_name='تاریخ انقضای گارانتی')

    class Meta:
        verbose_name = '1 - کالای دیجیتال'
        verbose_name_plural = '1 - کالا های دیجیتال'


class HouseProperty(Property):
    house_property_type = models.CharField(max_length=255, choices=HOUSE_PROPERTY_TYPE, verbose_name='نوع کالا')

    class Meta:
        verbose_name = '2 - کالای خانگی'
        verbose_name_plural = '2 - کالا های خانگی'


class CulturalProperty(models.Model):
    cultural_property_type = models.CharField(max_length=255, choices=CULTURAL_PROPERTY_TYPE, verbose_name='نوع کالا')
    full_name = models.CharField(max_length=255, null=False, blank=False, verbose_name='نام')
    description = models.TextField(null=True, blank=True, verbose_name='توضیحات')
    images = models.ManyToManyField(FileGallery, blank=True, verbose_name='فیلم و تصویر از کالا')
    number_of_inventory = models.PositiveIntegerField(default=0, null=False, editable=False, verbose_name='تعداد موجودی فعلی')
    created_at = jmodels.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated_at = jmodels.jDateTimeField(auto_now=True, verbose_name='تاریخ بروز رسانی')
    created_by = models.ForeignKey(User, related_name='%(app_label)s_%(class)s_property_created_by', on_delete=models.SET_NULL, null=True, editable=False, verbose_name='ساخته شده توسط')
    updated_by = models.ForeignKey(User, related_name='%(app_label)s_%(class)s_property_updated_by', on_delete=models.SET_NULL, null=True, editable=False, verbose_name='آخرین اصلاح توسط')

    def __str__(self):
        return self.cultural_property_type + " | " + self.full_name

    class Meta:
        verbose_name = '3 - کالای فرهنگی'
        verbose_name_plural = '3 - کالا های فرهنگی'


class CulturalPropertyAddUp(models.Model):
    cultural_property = models.ForeignKey(CulturalProperty, on_delete=models.CASCADE, null=False, blank=False, verbose_name='کالای فرهنگی')
    add_up_number = models.PositiveIntegerField(null=False, blank=False, verbose_name='تعداد اضافه شده')
    date_of_addup = jmodels.jDateTimeField(null=False, blank=False, verbose_name='تاریخ افزودن')
    created_at = jmodels.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    created_by = models.ForeignKey(User, related_name='%(app_label)s_%(class)s_property_created_by', on_delete=models.SET_NULL, null=True, editable=False, verbose_name='ساخته شده توسط')

    def __str__(self):
        return str(self.date_of_addup.date()) + " | " + str(self.cultural_property.full_name) + " | " + str(self.add_up_number)

    class Meta:
        verbose_name = '3.2 - افزودن کالای فرهنگی'
        verbose_name_plural = '3.2 - افزودن کالای فرهنگی'


@receiver(post_save, sender=CulturalPropertyAddUp)
def cultural_property_inventory_add_up(instance, **kwargs):
    cultural_property = instance.cultural_property
    cultural_property_add_up = CulturalPropertyAddUp.objects.filter(cultural_property=cultural_property, created_by=instance.created_by)
    add_number = 0
    for item in cultural_property_add_up:
        add_number += item.add_up_number

    cultural_property_assignment = CulturalPropertyAssignment.objects.filter(cultural_property=cultural_property,
                                                                    created_by=instance.created_by)
    assign_number = 0
    for item in cultural_property_assignment:
        assign_number += item.number_of_assigned_property

    cultural_property.number_of_inventory = int(add_number - assign_number)
    cultural_property.save()


class CulturalPropertyAssignment(models.Model):
    cultural_property = models.ForeignKey(CulturalProperty, on_delete=models.CASCADE, null=False, blank=False, verbose_name='کالای فرهنگی')
    send_to = models.ForeignKey(Profile, on_delete=models.CASCADE, null=False, blank=False, verbose_name='تحویل شده به')
    date_of_assign = jmodels.jDateTimeField(null=False, blank=False, verbose_name='تاریخ تحویل')
    number_of_assigned_property = models.PositiveIntegerField(null=False, blank=False, verbose_name='تعداد تحویل شده')
    created_at = jmodels.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    created_by = models.ForeignKey(User, related_name='%(app_label)s_%(class)s_property_created_by', on_delete=models.SET_NULL, null=True, editable=False, verbose_name='ساخته شده توسط')

    def __str__(self):
        return str(self.date_of_assign.date()) + " | " + self.send_to.user.username + " | " + str(self.number_of_assigned_property)

    class Meta:
        verbose_name = '3.2 - تحویل کالای فرهنگی'
        verbose_name_plural = '3.2 - تحویل کالای فرهنگی'


@receiver(post_save, sender=CulturalPropertyAssignment)
def cultural_property_assignment_number(instance, **kwargs):
    cultural_property = instance.cultural_property
    cultural_property_add_up = CulturalPropertyAddUp.objects.filter(cultural_property=cultural_property,
                                                                    created_by=instance.created_by)
    add_number = 0
    for item in cultural_property_add_up:
        add_number += item.add_up_number

    cultural_property_assignment = CulturalPropertyAssignment.objects.filter(cultural_property=cultural_property,
                                                                             created_by=instance.created_by)
    assign_number = 0
    for item in cultural_property_assignment:
        assign_number += item.number_of_assigned_property

    cultural_property.number_of_inventory = int(add_number - assign_number)
    cultural_property.save()
