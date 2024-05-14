from django.db import models

CARD_BG_COLOR = (('gold', 'gold'), ('silver', 'silver'), ('bronze', 'bronze'), ('none', 'none'))


class LicenceSetting(models.Model):
    tax_percent = models.FloatField(default=0, null=False, blank=False, verbose_name='درصد مالیات شارژ حساب')
    financial_licence_is_active = models.BooleanField(default=True, verbose_name='لایسنس حسابداری')
    financial_licence_price = models.PositiveIntegerField(default=2000, null=False, blank=False, verbose_name='هزینه روزانه لایسنس حسابداری - تومان')
    warehouse_licence_is_active = models.BooleanField(default=True, verbose_name='لایسنس انبار داری')
    warehouse_licence_price = models.PositiveIntegerField(default=2000, null=False, blank=False, verbose_name='هزینه روزانه لایسنس انبار داری - تومان')
    social_licence_is_active = models.BooleanField(default=True, verbose_name='لایسنس شبکه های اجتماعی')
    social_licence_price = models.PositiveIntegerField(default=2000, null=False, blank=False, verbose_name='هزینه روزانه لایسنس شبکه های اجتماعی - تومان')
    blog_licence_is_active = models.BooleanField(default=True, verbose_name='لایسنس بلاگ')
    blog_licence_price = models.PositiveIntegerField(default=2000, null=False, blank=False, verbose_name='هزینه روزانه لایسنس بلاگ - تومان')
    automation_licence_is_active = models.BooleanField(default=True, verbose_name='لایسنس اتوماسیون')
    automation_licence_price = models.PositiveIntegerField(default=2000, null=False, blank=False, verbose_name='هزینه روزانه لایسنس اتوماسیون - تومان')
    send_message_price = models.PositiveIntegerField(default=100, null=False, blank=False,
                                                    verbose_name='هزینه ارسال هر پیام - تومان')

    def __str__(self):
        return f"{self.id}"

    class Meta:
        verbose_name = 'تنظیمات اشتراک'
        verbose_name_plural = 'تنظیمات اشتراک'


class VIPPlan(models.Model):
    price = models.PositiveIntegerField(default=0, null=False, blank=False, verbose_name='قیمت - تومان')

    def __str__(self):
        return f"{self.price}"

    class Meta:
        ordering = ['price']
        verbose_name = 'قیمت اشتراک'
        verbose_name_plural = 'قیمت های اشتراک'



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





