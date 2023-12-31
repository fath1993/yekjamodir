from django.contrib import admin

from task_manager.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'director',
        'activity',
        'prediction_progress_start_date',
        'prediction_progress_end_date',
        'real_progress_start_date',
        'real_progress_end_date',
        'activity_completion_percentage',
    )

    readonly_fields = (
        'created_at',
        'created_by',

        'prediction_progress_start_day',
        'prediction_progress_end_day',
        'prediction_progress_days',
        'prediction_progress_start_month',
        'prediction_progress_end_month',
        'prediction_progress_months',

        'real_progress_start_day',
        'real_progress_end_day',
        'real_progress_days',
        'real_progress_start_month',
        'real_progress_end_month',
        'real_progress_months',
    )

    fields = (
        'director',
        'activity',
        'prediction_progress_start_date',
        'prediction_progress_end_date',
        'prediction_progress_start_day',
        'prediction_progress_end_day',
        'prediction_progress_days',
        'prediction_progress_start_month',
        'prediction_progress_end_month',
        'prediction_progress_months',
        'real_progress_start_date',
        'real_progress_end_date',
        'real_progress_start_day',
        'real_progress_end_day',
        'real_progress_days',
        'real_progress_start_month',
        'real_progress_end_month',
        'real_progress_months',
        'activity_completion_percentage',
        'created_at',
        'created_by',
    )

    def save_model(self, request, instance, form, change):
        instance = form.save(commit=False)
        if not change:
            instance.created_by = request.user
        instance.save()
        form.save_m2m()
        return instance
