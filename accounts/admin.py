from django.contrib import admin
from accounts.models import Profile, SMSAuthCode, ExtraStoragePlan, VIPPlan


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
    )

    fields = (
        'user',
        'mobile_phone_number',
        'landline',
        'address',
        'profile_pic',
        'default_maximum_storage_quota',
        'default_metapost_daily_send_limit',
        'default_financial_broker_limit',
        'vip_plan',
        'vip_plan_expiry_date',
        'extra_storage',
        'extra_storage_expiry_date',
        'metapost_daily_sent',
        'metapost_last_send_date',
        'user_financial_default_broker_id',
    )


@admin.register(SMSAuthCode)
class SMSAuthCodeAdmin(admin.ModelAdmin):
    list_display = (
        'phone_number',
        'pass_code',
        'created_at',
    )
    readonly_fields = (
        'phone_number',
        'pass_code',
        'created_at',
    )
    fields = (
        'phone_number',
        'pass_code',
        'created_at',
    )

    def has_add_permission(self, request):
        return False


@admin.register(ExtraStoragePlan)
class ExtraStoragePlanAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'price',
        'expiry_days',
        'storage',
    )

    fields = (
        'title',
        'price',
        'expiry_days',
        'storage',
    )


@admin.register(VIPPlan)
class VIPPlanAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'price',
        'expiry_days',
        'maximum_storage_quota',
        'metapost_daily_send_limit',
        'financial_broker_limit',
    )

    fields = (
        'title',
        'price',
        'expiry_days',
        'maximum_storage_quota',
        'metapost_daily_send_limit',
        'financial_broker_limit',
        'numbers_of_assistant',
        'all_licence_activate',
        'full_support',

        'card_background_color',
    )