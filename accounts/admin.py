from django.contrib import admin
from accounts.models import Profile, SMSAuthCode, ExtraStoragePlan, VIPPlan, Licence, Invoice


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
        'wallet_balance',


        'demo_used_once',
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


# @admin.register(SMSAuthCode)
# class SMSAuthCodeAdmin(admin.ModelAdmin):
#     list_display = (
#         'phone_number',
#         'pass_code',
#         'created_at',
#     )
#     readonly_fields = (
#         'phone_number',
#         'pass_code',
#         'created_at',
#     )
#     fields = (
#         'phone_number',
#         'pass_code',
#         'created_at',
#     )
#
#     def has_add_permission(self, request):
#         return False


@admin.register(Licence)
class LicenceAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'order',
    )

    fields = (
        'title',
        'order',
    )


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
        'max_storage_quote',
    )

    fields = (
        'title',
        'price',
        'tax',
        'expiry_days',
        'has_access_to_licence',
        'max_storage_quote',
        'card_background_color',
    )


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = (
        'invoice_type',
        'user',
        'amount',
        'authority',
        'ref_id',
        'status',
    )

    list_filter = (
        'invoice_type',
        'status',
    )

    readonly_fields = (
        'created_at',
        'updated_at',
        'created_by',
    )

    fields = (
        'invoice_type',
        'user',
        'amount',
        'description',
        'authority',
        'ref_id',
        'status',
        'created_at',
        'updated_at',
        'created_by',
    )