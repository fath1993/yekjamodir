from django.db import models
from django_jalali.db import models as jmodel


class SystemThreadIsActive(models.Model):
    updated_at = jmodel.jDateTimeField(auto_now=True, verbose_name='بروز شده در')

    def __str__(self):
        return f'{self.id}'

    class Meta:
        verbose_name = 'پردازش موازی سیستم'
        verbose_name_plural = 'پردازش موازی سیستم'
