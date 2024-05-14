from django.contrib import admin

from subscription.models import VIPPlan, ExtraStoragePlan, Licence, LicenceSetting


@admin.register(LicenceSetting)
class LicenceSettingAdmin(admin.ModelAdmin):
    list_display = (
        'tax_percent',
        'send_message_price',
        'financial_licence_is_active',
        'warehouse_licence_is_active',
        'social_licence_is_active',
        'blog_licence_is_active',
        'automation_licence_is_active',
    )

    fields = (
        'tax_percent',
        'financial_licence_is_active',
        'financial_licence_price',
        'warehouse_licence_is_active',
        'warehouse_licence_price',
        'social_licence_is_active',
        'social_licence_price',
        'blog_licence_is_active',
        'blog_licence_price',
        'automation_licence_is_active',
        'automation_licence_price',
        'send_message_price',
    )

    def has_add_permission(self, request):
        if LicenceSetting.objects.all().count() > 0:
            return False
        else:
            return True


@admin.register(VIPPlan)
class VIPPlanAdmin(admin.ModelAdmin):
    list_display = (
        'price',
    )

    fields = (
        'price',
    )

#
# @admin.register(Licence)
# class LicenceAdmin(admin.ModelAdmin):
#     list_display = (
#         'title',
#         'order',
#     )
#
#     fields = (
#         'title',
#         'order',
#     )
#
#
# @admin.register(ExtraStoragePlan)
# class ExtraStoragePlanAdmin(admin.ModelAdmin):
#     list_display = (
#         'title',
#         'price',
#         'expiry_days',
#         'storage',
#     )
#
#     fields = (
#         'title',
#         'price',
#         'expiry_days',
#         'storage',
#     )
#
#

