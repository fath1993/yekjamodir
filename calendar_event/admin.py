from django.contrib import admin

from calendar_event.models import Event


@admin.register(Event)
class CustomEventAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'start_date',
        'end_date',
    )
    readonly_fields = (
        'created_by',
    )
    fields = (
        'name',
        'description',
        'start_date',
        'end_date',
        'remind_me_at',
        'remind_me_hourly_at',
        'remin_me_daily_at',
        'remind_me_monthly_at',
        'remind_me_yearly_at',
        'created_by',
    )

    @admin.display(description="تاریخ بروزرسانی", empty_value='???')
    def updated_at_display(self, obj):
        data_time = str(obj.created_at.strftime('%Y-%m-%d - %H:%M %Z'))
        return data_time

    def save_model(self, request, instance, form, change):
        user = request.user
        instance = form.save(commit=False)
        if not change:
            instance.created_by = user
        instance.save()
        form.save_m2m()
        return instance

