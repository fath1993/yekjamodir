from django.urls import path, include

from subscription.views import InvoiceView, InvoiceList, ChargeWalletView

app_name = 'subscription'

urlpatterns = [
    # subscription
    path('charge-wallet/', ChargeWalletView().charge_credit, name='charge-wallet'),
    path('charge-wallet-callback/', ChargeWalletView().charge_credit_callback, name='charge-wallet-callback'),
    path('invoice/', InvoiceView.as_view(), name='invoice'),
    path('invoice&id=<int:invoice_id>/', InvoiceView.as_view(), name='invoice-with-id'),
    path('invoices-list/', InvoiceList.as_view(), name='invoices-list'),
]