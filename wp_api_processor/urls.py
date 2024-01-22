from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from wp_api_processor.views import WPAPIProcessorView

app_name = 'wp_api_processor'

urlpatterns = [
    path('wp-api/request/', csrf_exempt(WPAPIProcessorView.as_view()), name='wp-api-request'),
]
