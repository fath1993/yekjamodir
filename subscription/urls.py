from django.urls import path, include

from subscription.views import SubscriptionView

app_name = 'subscription'

urlpatterns = [
    # subscription
    path('charge-wallet/', SubscriptionView().charge_credit, name='charge-wallet'),
    path('charge-wallet-callback/', SubscriptionView().charge_credit_callback, name='charge-wallet-callback'),
    path('invoices-list/', SubscriptionView().invoice_list, name='invoices-list'),
    path('change-vip-plan/', SubscriptionView().change_vip_plan, name='change-vip-plan'),
]
