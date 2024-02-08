from django.contrib import admin

from auto_robots.models import Bot, MetaPost, MetapostHistory


@admin.register(Bot)
class BotAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'bot_type',
        'bot_name',
        'bot_token',
        'bot_token_belongs_to',
        'has_access_to_channels',
        'created_at_display',
        'created_by',
    )

    readonly_fields = (
        'created_at',
        'created_by',
    )

    fields = (
        'bot_type',
        'bot_name',
        'bot_token',
        'bot_token_belongs_to',
        'has_access_to_channels',
        'created_at',
        'created_by',
    )

    @admin.display(description="تاریخ ایجاد", empty_value='???')
    def created_at_display(self, obj):
        data_time = str(obj.created_at.strftime('%Y-%m-%d - %H:%M'))
        return data_time

    def save_model(self, request, instance, form, change):
        instance = form.save(commit=False)
        if not change:
            instance.created_by = request.user
        instance.save()
        form.save_m2m()
        return instance


@admin.register(MetaPost)
class MetaPostAdmin(admin.ModelAdmin):
    list_display = (
        'bot',
        'message_status',
        'title',
        'created_at_display',
        'created_by',
    )

    readonly_fields = (
        'message_id',
        'created_at',
        'updated_at',
        'created_by',
        'updated_by',
    )

    search_fields = (
        'title',
        'created_by__username',
    )

    list_filter = (
        'send_at_type',
        'message_status',
    )

    fields = (
        'bot',
        'message_status',
        'send_at_type',
        'send_at_date_time',
        'title',
        'sub_title',
        'categories',
        'keywords',
        'attached_file_link',
        'content',
        'metapost_view_type',
        'message_id',
        'created_at',
        'updated_at',
        'created_by',
        'updated_by',
    )

    @admin.display(description="تاریخ ایجاد", empty_value='???')
    def created_at_display(self, obj):
        data_time = str(obj.created_at.strftime('%Y-%m-%d - %H:%M'))
        return data_time

    def save_model(self, request, instance, form, change):
        instance = form.save(commit=False)
        if not change:
            instance.created_by = request.user
        instance.save()
        form.save_m2m()
        return instance


@admin.register(MetapostHistory)
class MetapostHistoryAdmin(admin.ModelAdmin):
    list_display = (
        'metapost',
        'chat_id',
        'message_id',
    )

    fields = (
        'metapost',
        'response_message',
        'chat_id',
        'message_id',
    )
