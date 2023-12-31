from django.contrib import admin
from financial_accounting.models import FinancialBroker, TransactionRecord


@admin.register(FinancialBroker)
class FinancialBrokerAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'broker_name',
        'account_owner',
        'account_number',
        'account_ISBN',
        'account_card_number',
        'calculated_credit_balance',
    )
    readonly_fields = (
        'calculated_credit_balance',
        'created_at',
        'updated_at',
        'created_by',
        'updated_by',
    )
    fields = (
        'broker_name',
        'account_owner',
        'account_number',
        'account_ISBN',
        'account_card_number',
        'calculated_credit_balance',
        'created_at',
        'updated_at',
        'created_by',
        'updated_by',
    )

    def get_queryset(self, request):
        qs = super(FinancialBrokerAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs.filter()
        else:
            return qs.filter(created_by=request.user)

    def save_model(self, request, instance, form, change):
        user = request.user
        instance = form.save(commit=False)
        if not change:
            instance.created_by = user
            instance.updated_by = user
        else:
            instance.updated_by = user
        instance.save()
        form.save_m2m()
        return instance


@admin.register(TransactionRecord)
class TransactionRecordAdmin(admin.ModelAdmin):
    list_display = (
        'financial_broker',
        'updated_by',
        'date_of_action_display',
        'transaction_type',
        'title',
        'amount',
    )
    list_filter = (
        'transaction_type',
    )
    readonly_fields = (
        'created_at',
        'updated_at',
        'created_by',
        'updated_by',
    )
    fields = (
        'financial_broker',
        'transaction_type',
        'amount',
        'date_of_action',
        'title',
        'description',
        'attachments',
        'created_at',
        'updated_at',
        'created_by',
        'updated_by',
    )

    @admin.display(description="تاریخ اقدام", empty_value='???')
    def date_of_action_display(self, obj):
        data_time = str(obj.date_of_action.strftime('%Y-%m-%d - %H:%M'))
        return data_time

    def save_model(self, request, instance, form, change):
        user = request.user
        instance = form.save(commit=False)
        if not change:
            instance.created_by = user
            instance.updated_by = user
        else:
            instance.updated_by = user
        instance.save()
        form.save_m2m()
        return instance

