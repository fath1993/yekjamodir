import uuid
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django_jalali.db import models as jmodels
from gallery.models import FileGallery
from django.db.models.signals import post_save
from django.dispatch import receiver

TRANSACTION_TYPE = (('withdraw', 'برداشت شده از حساب'), ('deposit', 'واریز شده به حساب'))
# TRANSACTION_TYPE = (('برداشت شده از حساب', 'برداشت شده از حساب'), ('واریز شده به حساب', 'واریز شده به حساب'))


class FinancialBroker(models.Model):
    broker_name = models.CharField(max_length=255, null=False, blank=False, verbose_name='نام کارگزار مالی')
    account_owner = models.CharField(max_length=255, null=False, blank=False, verbose_name='نام صاحب حساب')
    account_number = models.CharField(max_length=255, null=False, blank=False, verbose_name='شماره حساب')
    account_ISBN = models.CharField(max_length=255, null=True, blank=True, verbose_name='شماره شبا')
    account_card_number = models.CharField(max_length=255, null=True, blank=True, verbose_name='شماره کارت')
    calculated_credit_balance = models.IntegerField(null=True, editable=False, verbose_name='مانده حساب - ریال',
                                                    help_text='محاسه بر اساس تراکنش های ثبت شده')
    created_at = jmodels.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated_at = jmodels.jDateTimeField(auto_now=True, verbose_name='تاریخ بروز رسانی')
    created_by = models.ForeignKey(User, related_name='financial_broker_created_by', on_delete=models.CASCADE,
                                   null=False, editable=False,
                                   verbose_name='کاربر سازنده')
    updated_by = models.ForeignKey(User, related_name='financial_broker_updated_by', on_delete=models.CASCADE,
                                   null=False, editable=False,
                                   verbose_name='کاربر ویرایش کننده')

    def __str__(self):
        return self.broker_name

    class Meta:
        ordering = ['-updated_by']
        verbose_name = "کارگزار مالی"
        verbose_name_plural = "کارگزاران مالی"

    def get_absolute_url(self):
        return reverse('financial:financial-broker-edit', kwargs={'broker_id': self.id})


class TransactionRecord(models.Model):
    financial_broker = models.ForeignKey(FinancialBroker, related_name='transaction_record_financial_account',
                                         on_delete=models.CASCADE, null=False, blank=False, verbose_name='حساب مالی')
    transaction_type = models.CharField(max_length=255, choices=TRANSACTION_TYPE, default='برداشت شده از حساب',
                                        null=False, blank=False, verbose_name='نوع تراکنش')
    amount = models.PositiveIntegerField(default=0, null=False, blank=False, verbose_name='مقدار - ریال')
    date_of_action = jmodels.jDateTimeField(null=False, blank=False, verbose_name='تاریخ اقدام')
    title = models.CharField(max_length=255, null=False, blank=False, verbose_name='عنوان تراکنش')
    description = models.TextField(null=True, blank=True, verbose_name='توضیحات')
    attachments = models.ManyToManyField(FileGallery, blank=True, verbose_name='ضمیمه ها')
    created_at = jmodels.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated_at = jmodels.jDateTimeField(auto_now=True, verbose_name='تاریخ بروز رسانی')
    created_by = models.ForeignKey(User, related_name='transaction_record_created_by', on_delete=models.CASCADE,
                                   null=False, editable=False, verbose_name='کاربر سازنده')
    updated_by = models.ForeignKey(User, related_name='transaction_record_updated_by', on_delete=models.CASCADE,
                                   null=False, editable=False, verbose_name='کاربر ویرایش کننده')

    def __str__(self):
        return f'{self.transaction_type} | {self.title}'

    class Meta:
        ordering = ['-date_of_action', '-updated_at']
        verbose_name = "تراکنش"
        verbose_name_plural = "تراکنش ها"


@receiver(post_save, sender=TransactionRecord)
def financial_broker_updater(instance, **kwargs):
    financial_broker = instance.financial_broker
    transactions = TransactionRecord.objects.filter(financial_broker=financial_broker,
                                                    created_by=instance.created_by)
    amount = 0.0
    for tr in transactions:
        if tr.transaction_type == 'برداشت شده از حساب':
            amount += -1 * abs(float(tr.amount))
        else:
            amount += abs(float(tr.amount))
    financial_broker.calculated_credit_balance = amount
    financial_broker.save()
