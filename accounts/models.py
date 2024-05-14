from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_jalali.db import models as jmodel


TRANSACTION_STATUS = (('پرداخت نشده', 'پرداخت نشده'), ('پرداخت شده', 'پرداخت شده'))
INVOICE_TYPE = (('واریز به حساب', 'واریز به حساب'), ('برداشت از حساب', 'برداشت از حساب'))



class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile_user', on_delete=models.CASCADE, null=False, blank=False,
                                verbose_name='کاربر')
    mobile_phone_number = models.CharField(max_length=255, null=True, blank=True, verbose_name='شماره همراه')
    landline = models.CharField(max_length=255, null=True, blank=True, verbose_name='شماره ثابت')
    address = models.CharField(max_length=255, null=True, blank=True, verbose_name='آدرس')
    profile_pic = models.ImageField(upload_to='profile-pic/', blank=True, verbose_name='عکس پروفایل')
    wallet_balance = models.PositiveIntegerField(default=0, null=False, blank=False, verbose_name='اعتبار حساب')


    financial_licence = models.BooleanField(default=False, verbose_name='لایسنس حسابداری')
    warehouse_licence = models.BooleanField(default=False, verbose_name='لایسنس انبار داری')
    social_licence = models.BooleanField(default=False, verbose_name='لایسنس شبکه های اجتماعی')
    blog_licence = models.BooleanField(default=False, verbose_name='لایسنس بلاگ')
    automation_licence = models.BooleanField(default=False, verbose_name='لایسنس اتوماسیون')


    default_maximum_storage_quota = models.PositiveIntegerField(default=100, null=False, blank=False,
                                                                verbose_name='حداکثر فضای ذخیره سازی',
                                                                help_text='مگابایت')
    metapost_daily_sent = models.PositiveIntegerField(default=0, null=False, blank=False,
                                                      verbose_name='تعداد متاپست ارسالی اخرین روز')
    metapost_last_send_date = jmodel.jDateTimeField(null=True, blank=True, verbose_name='تاریخ آخرین ارسال متاپست')

    user_financial_default_broker_id = models.PositiveIntegerField(default=0, null=False, blank=False,
                                                                   verbose_name='صندوق  مالی پیشفرض')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'پروفایل'
        verbose_name_plural = 'پروفایل'


@receiver(post_save, sender=User)
def auto_create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


class SMSAuthCode(models.Model):
    phone_number = models.CharField(max_length=255, null=False, blank=False, editable=False,
                                    verbose_name='شماره موبایل')
    pass_code = models.CharField(max_length=255, null=False, blank=False, editable=False, verbose_name='کد احراز')
    created_at = jmodel.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')

    def __str__(self):
        return self.phone_number

    class Meta:
        ordering = ['created_at', ]
        verbose_name = 'کد تایید پیامکی'
        verbose_name_plural = 'کد های تایید پیامکی'


class Invoice(models.Model):
    invoice_type = models.CharField(max_length=255, choices=INVOICE_TYPE, default='برداشت', null=False,
                              blank=False, verbose_name='نوع صورت حساب')
    user = models.ForeignKey(User, related_name='invoice_user', on_delete=models.CASCADE, null=False, blank=False, verbose_name='کاربر')
    amount = models.PositiveIntegerField(null=False, blank=False, verbose_name='مبلغ - تومان')
    tax = models.PositiveIntegerField(default=0, null=False, blank=False, verbose_name='مالیات - تومان')
    description = models.CharField(max_length=255, null=True, blank=True, verbose_name='توضیحات')

    authority = models.CharField(max_length=255, null=True, blank=True)
    ref_id = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, choices=TRANSACTION_STATUS, default='پرداخت نشده', null=False,
                              blank=False, verbose_name='وضعیت')

    created_at = jmodel.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated_at = jmodel.jDateTimeField(auto_now=True, verbose_name='تاریخ بروز رسانی')
    created_by = models.ForeignKey(User, related_name='invoice_created_by', on_delete=models.CASCADE, null=False, blank=False,
                                   editable=False, verbose_name='ساخته شده توسط')

    def __str__(self):
        return f'{self.user.username} | {self.pk}'

    class Meta:
        ordering = ['-created_at', ]
        verbose_name = 'صورت حساب'
        verbose_name_plural = 'صورت حساب ها'
