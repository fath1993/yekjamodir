from django.urls import path, include

from dashboard.views import Dashboard, PricingView

app_name = 'dashboard'

urlpatterns = [
    path('', Dashboard.as_view(), name='dashboard'),

    # pricing
    path('pricing/', PricingView.as_view(), name='pricing'),
]
