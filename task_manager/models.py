import jdatetime
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django_jalali.db import models as jmodel

from task_manager.utils import datetime_to_number


class Task(models.Model):
    director = models.ForeignKey(User, related_name='task_director', on_delete=models.CASCADE, null=False, blank=False,
                                 verbose_name='مجری')
    activity = models.CharField(max_length=255, null=False, blank=False, verbose_name='فعالیت')
    prediction_progress_start_date = jmodel.jDateField(null=False, blank=False, verbose_name='تاریخ شروع پیش بینی شده')
    prediction_progress_end_date = jmodel.jDateField(null=False, blank=False, verbose_name='تاریخ پایان پیش بینی شده')
    prediction_progress_start_day = models.PositiveSmallIntegerField(null=True, blank=True, editable=False,
                                                                     verbose_name='تاریخ شروع پیش بینی شده بر اساس روز در سال')
    prediction_progress_end_day = models.PositiveSmallIntegerField(null=True, blank=True, editable=False,
                                                                   verbose_name='تاریخ پایان پیش بینی شده بر اساس روز در سال')
    prediction_progress_days = models.PositiveSmallIntegerField(null=True, blank=True, editable=False,
                                                                verbose_name='مدت زمان پیشبینی بر اساس روز')
    prediction_progress_start_month = models.PositiveSmallIntegerField(null=True, blank=True, editable=False,
                                                                       verbose_name='تاریخ شروع پیش بینی شده بر اساس ماه در سال')
    prediction_progress_end_month = models.PositiveSmallIntegerField(null=True, blank=True, editable=False,
                                                                     verbose_name='تاریخ پایان پیش بینی شده بر اساس ماه در سال')
    prediction_progress_months = models.PositiveSmallIntegerField(null=True, blank=True, editable=False,
                                                                  verbose_name='مدت زمان پیشبینی بر اساس ماه')
    real_progress_start_date = jmodel.jDateField(null=True, blank=True, verbose_name='تاریخ شروع واقعی')
    real_progress_end_date = jmodel.jDateField(null=True, blank=True, verbose_name='تاریخ پایان واقعی')
    real_progress_start_day = models.PositiveSmallIntegerField(null=True, blank=True, editable=False,
                                                               verbose_name='تاریخ شروع واقعی بر اساس روز در سال')
    real_progress_end_day = models.PositiveSmallIntegerField(null=True, blank=True, editable=False,
                                                             verbose_name='تاریخ پایان واقعی بر اساس روز در سال')
    real_progress_days = models.PositiveSmallIntegerField(null=True, blank=True, editable=False,
                                                          verbose_name='مدت زمان واقعی بر اساس روز')
    real_progress_start_month = models.PositiveSmallIntegerField(null=True, blank=True, editable=False,
                                                                 verbose_name='تاریخ شروع واقعی بر اساس ماه در سال')
    real_progress_end_month = models.PositiveSmallIntegerField(null=True, blank=True, editable=False,
                                                               verbose_name='تاریخ پایان واقعی بر اساس ماه در سال')
    real_progress_months = models.PositiveSmallIntegerField(null=True, blank=True, editable=False,
                                                            verbose_name='مدت زمان واقعی بر اساس ماه')

    activity_completion_percentage = models.PositiveIntegerField(default=0, null=True, blank=True,
                                                                 verbose_name='درصد پیشرفت فعالیت')
    created_at = jmodel.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    created_by = models.ForeignKey(User, related_name='task_created_by', on_delete=models.CASCADE, null=False,
                                   blank=False, editable=False, verbose_name='ساخته شده توسط')

    #
    # real_progress_state =
    # real_and_prediction_situation =

    def __str__(self):
        return self.director.username + " | " + self.activity

    class Meta:
        ordering = ['-created_at', ]
        verbose_name = 'فعالیت'
        verbose_name_plural = 'فعالیت ها'

    def save(self, *args, **kwargs):
        self.prediction_progress_start_day = datetime_to_number(self.prediction_progress_start_date, 'day')
        self.prediction_progress_end_day = datetime_to_number(self.prediction_progress_end_date, 'day')
        self.prediction_progress_days = self.prediction_progress_end_day - self.prediction_progress_start_day + 1

        self.prediction_progress_start_month = datetime_to_number(self.prediction_progress_start_date, 'month')
        self.prediction_progress_end_month = datetime_to_number(self.prediction_progress_end_date, 'month')
        self.prediction_progress_months = self.prediction_progress_end_month - self.prediction_progress_start_month + 1

        if self.real_progress_start_date and self.real_progress_end_date:
            self.real_progress_start_day = datetime_to_number(self.real_progress_start_date, 'day')
            self.real_progress_end_day = datetime_to_number(self.real_progress_end_date, 'day')
            self.real_progress_days = self.real_progress_end_day - self.real_progress_start_day + 1

            self.real_progress_start_month = datetime_to_number(self.real_progress_start_date, 'month')
            self.real_progress_end_month = datetime_to_number(self.real_progress_end_date, 'month')
            self.real_progress_months = self.real_progress_end_month - self.real_progress_start_month + 1
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('tasks:task-detail-with-id', kwargs={'task_id': self.id})
