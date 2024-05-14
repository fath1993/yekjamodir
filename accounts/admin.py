from django.contrib import admin
from accounts.models import Profile, SMSAuthCode, Invoice


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

        'financial_licence',
        'warehouse_licence',
        'social_licence',
        'blog_licence',
        'automation_licence',

        'default_maximum_storage_quota',
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


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = (
        'invoice_type',
        'user',
        'amount',
        'tax',
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
        'tax',
        'description',
        'authority',
        'ref_id',
        'status',
        'created_at',
        'updated_at',
        'created_by',
    )
