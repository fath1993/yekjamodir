from django.urls import path, include

from dashboard.views import Dashboard, BuyLicenceView, ChargeAccountView

app_name = 'dashboard'

urlpatterns = [
    path('', Dashboard.as_view(), name='dashboard'),

    # pricing
    path('buy-licence/', BuyLicenceView.as_view(), name='buy-licence'),
    path('charge-account/', ChargeAccountView.as_view(), name='charge-account'),
]