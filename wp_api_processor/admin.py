from django.apps import apps
from django.contrib import admin

from wp_api_processor.models import WpUsers


@admin.register(WpUsers)
class WpUsersAdmin(admin.ModelAdmin):
    db = 'wp_db'
    list_display = (
        'id',
        'user_login',
        'user_pass',
        'user_nicename',
        'user_email',
    )

    readonly_fields = (
        'id',
    )

    fields = (
        'id',
        'user_login',
        'user_pass',
        'user_nicename',
        'user_email',
        'user_url',
        'user_registered',
        'user_activation_key',
        'user_status',
        'display_name',
    )


models = apps.get_app_config('wp_api_processor').get_models()

for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
