from django.db import models


class TelegramBotSetting(models.Model):
    bot_address = models.CharField(max_length=255, null=False, blank=False, verbose_name='آدرس')
    bot_token = models.CharField(max_length=255, null=False, blank=False, verbose_name='توکن')

    def __str__(self):
        return 'تنظیمات ربات تلگرام'

    class Meta:
        verbose_name = 'تنظیمات ربات تلگرام'
        verbose_name_plural = 'تنظیمات ربات تلگرام'


def get_telegram_bot_config_settings():
    try:
        envato_telegram_bot_config_settings = TelegramBotSetting.objects.filter().latest('id')
    except:
        envato_telegram_bot_config_settings = TelegramBotSetting(
            bot_address='',
            bot_token='',
        )
        envato_telegram_bot_config_settings.save()
    return envato_telegram_bot_config_settings
