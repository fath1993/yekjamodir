from django.contrib import admin

from system_thread.models import SystemThreadIsActive


@admin.register(SystemThreadIsActive)
class SystemThreadIsActiveAdmin(admin.ModelAdmin):
    list_display = (
        'updated_at_display',
    )

    readonly_fields = (
        'updated_at',
    )

    fields = (
        'updated_at',
    )

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    @admin.display(description="تاریخ بروزرسانی", empty_value='???')
    def updated_at_display(self, obj):
        data_time = str(obj.updated_at.strftime('%Y-%m-%d - %H:%M'))
        return data_time

