from django.urls import path, include

from dashboard.views import Dashboard

app_name = 'dashboard'

urlpatterns = [
    path('', Dashboard.as_view(), name='dashboard'),

]