from django.urls import path, include

from accounts.views import login_view, logout_view, signup_view, two_step_verification_view, \
    ajax_two_step_verification_retry_send, ProfileView, ProfileEdit

app_name = 'accounts'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('signup/', signup_view, name='signup'),
    path('two-step/', two_step_verification_view, name='two-step'),
    path('two-step&phone-number=<int:phone_number>/', two_step_verification_view, name='two-step-with-phone-number'),
    path('ajax-two-step-verification-retry-send/', ajax_two_step_verification_retry_send, name='ajax-two-step-verification-retry-send'),

    # profile
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile-edit/', ProfileEdit.as_view(), name='profile-edit'),
]