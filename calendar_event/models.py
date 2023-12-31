from django.contrib.auth.models import User
from django.db import models
from django_jalali.db import models as jmodels


class Event(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False, verbose_name='رویداد')
    description = models.TextField(null=True, blank=True, verbose_name='توضیحات')
    start_date = jmodels.jDateTimeField(null=True, blank=True, verbose_name='تاریخ شروع رویداد')
    end_date = jmodels.jDateTimeField(null=True, blank=True, verbose_name='تاریخ پایان رویداد')
    remind_me_at = jmodels.jDateTimeField(null=True, blank=True, verbose_name='یاداوری یک باره')
    remind_me_hourly_at = models.PositiveSmallIntegerField(default=0, null=True, blank=True,
                                                           verbose_name='یاداوری ساعتی')
    remin_me_daily_at = jmodels.jDateTimeField(null=True, blank=True, verbose_name='یاداوری روزانه')
    remind_me_monthly_at = jmodels.jDateTimeField(null=True, blank=True, verbose_name='یاداوری ماهانه')
    remind_me_yearly_at = jmodels.jDateTimeField(null=True, blank=True, verbose_name='یاداوری سالانه')
    created_by = models.ForeignKey(User, related_name='custom_event_created_by', on_delete=models.CASCADE, null=False,
                                   editable=False, verbose_name='کاربر سازنده')

    def __str__(self):
        return self.created_by.username + " | " + self.name

    class Meta:
        verbose_name = "رویداد"
        verbose_name_plural = "رویداد ها"
