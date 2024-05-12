from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_jalali.db import models as jmodel

CARD_BG_COLOR = (('gold', 'gold'), ('silver', 'silver'), ('bronze', 'bronze'), ('none', 'none'))
TRANSACTION_STATUS = (('پرداخت نشده', 'پرداخت نشده'), ('پرداخت شده', 'پرداخت شده'))
INVOICE_TYPE = (('واریز به حساب', 'واریز به حساب'), ('برداشت از حساب', 'برداشت از حساب'))


class ExtraStoragePlan(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False, verbose_name='عنوان')
    price = models.PositiveIntegerField(null=False, blank=False, verbose_name='قیمت - تومان')
    expiry_days = models.PositiveSmallIntegerField(null=False, blank=False,
                                                   verbose_name='تعداد روز انقضا پس از فعالسازی')
    storage = models.PositiveSmallIntegerField(null=False, blank=False, verbose_name='افزایش فضای ذخیره به میزان',
                                               help_text='مگابایت')

    def __str__(self):
        return f"{self.title} | {self.price}"

    class Meta:
        verbose_name = 'پلن افزایش حجم'
        verbose_name_plural = 'پلن های افزایش حجم'


class Licence(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False, verbose_name='عنوان')
    order = models.PositiveSmallIntegerField(default=0, null=False, blank=False, verbose_name='ترتیب')

    def __str__(self):
        return f"{self.title}"

    class Meta:
        ordering = ['order', ]
        verbose_name = 'لایسنس'
        verbose_name_plural = 'لایسنس ها'


class VIPPlan(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False, verbose_name='عنوان')
    price = models.PositiveIntegerField(null=False, blank=False, verbose_name='قیمت - تومان')
    tax = models.PositiveIntegerField(default=0, null=False, blank=False, verbose_name='درصد مالیات')
    expiry_days = models.PositiveSmallIntegerField(null=False, blank=False,
                                                   verbose_name='تعداد روز انقضا پس از فعالسازی')
    has_access_to_licence = models.ManyToManyField(Licence, blank=True, verbose_name='لایسنس')
    max_storage_quote = models.PositiveSmallIntegerField(default=100, null=False, blank=False,
                                                         verbose_name='حداکثر فضای ذخیره سازی')
    card_background_color = models.CharField(default='none', choices=CARD_BG_COLOR, max_length=255, null=False,
                                             blank=False, verbose_name='عنوان')


    def __str__(self):
        return f"{self.title} | {self.price}"

    class Meta:
        ordering = ['price']
        verbose_name = 'پلن اشتراک'
        verbose_name_plural = 'پلن های اشتراک'


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile_user', on_delete=models.CASCADE, null=False, blank=False,
                                verbose_name='کاربر')
    mobile_phone_number = models.CharField(max_length=255, null=True, blank=True, verbose_name='شماره همراه')
    landline = models.CharField(max_length=255, null=True, blank=True, verbose_name='شماره ثابت')
    address = models.CharField(max_length=255, null=True, blank=True, verbose_name='آدرس')
    profile_pic = models.ImageField(upload_to='profile-pic/', blank=True, verbose_name='عکس پروفایل')
    wallet_balance = models.PositiveIntegerField(default=0, null=False, blank=False, verbose_name='اعتبار حساب')


    # Licence related
    demo_used_once = models.BooleanField(default=False, verbose_name='استفاده از دمو')

    default_maximum_storage_quota = models.PositiveIntegerField(default=100, null=False, blank=False,
                                                                verbose_name='حداکثر فضای ذخیره سازی',
                                                                help_text='مگابایت')
    default_metapost_daily_send_limit = models.PositiveIntegerField(default=10, null=False, blank=False,
                                                                    verbose_name='حداکثر تعداد پیام ارسالی روزانه')
    default_financial_broker_limit = models.PositiveIntegerField(default=1, null=False, blank=False,
                                                                 verbose_name='حداکثر تعداد کارگزاران مالی')
    vip_plan = models.ForeignKey(VIPPlan, related_name='vip_plan_profile', on_delete=models.CASCADE, null=True,
                                 blank=True, verbose_name='اشتراک')
    vip_plan_expiry_date = jmodel.jDateTimeField(null=True, blank=True, verbose_name='تاریخ انقضای اشتراک ویژه')
    extra_storage = models.ForeignKey(ExtraStoragePlan, related_name='extra_storage_profile', on_delete=models.CASCADE,
                                      null=True, blank=True, verbose_name='اشتراک')
    extra_storage_expiry_date = jmodel.jDateTimeField(null=True, blank=True, verbose_name='تاریخ انقضای حجم اضافه')

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
    description = models.CharField(max_length=255, null=True, blank=True, verbose_name='توضیحات')

    authority = models.CharField(max_length=255, null=True, blank=True)
    ref_id = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, choices=TRANSACTION_STATUS, default='pending', null=False,
                              blank=False, verbose_name='وضعیت')

    created_at = jmodel.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated_at = jmodel.jDateTimeField(auto_now=True, verbose_name='تاریخ بروز رسانی')
    created_by = models.ForeignKey(User, related_name='invoice_created_by', on_delete=models.CASCADE, null=False, blank=False,
                                   editable=False, verbose_name='ساخته شده توسط')

    def __str__(self):
        return f'{self.user.username} | {self.pk}'

    class Meta:
        ordering = ['created_at', ]
        verbose_name = 'صورت حساب'
        verbose_name_plural = 'صورت حساب ها'
