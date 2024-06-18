from django.contrib import admin

from website.models import TelegramBotSetting


@admin.register(TelegramBotSetting)
class TelegramBotSettingAdmin(admin.ModelAdmin):
    list_display = (
        'bot_address',
        'bot_token',
    )

    fields = (
        'bot_address',
        'bot_token',
    )
