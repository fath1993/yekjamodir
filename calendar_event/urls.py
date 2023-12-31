from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from calendar_event.views import NewEventView, \
    event_list_view, event_edit_view, event_delete_view, CalendarView, ajax_event_list

app_name = 'calendar_event'

urlpatterns = [
    path('calendar/', CalendarView.as_view(), name='calendar'),

    # site view
    path('event-new/', NewEventView.as_view(), name='event-new'),
    path('event-list/', event_list_view, name='event-list'),
    path('event-edit&id=<str:event_id>/', event_edit_view, name='event-edit'),
    path('event-delete&id=<str:event_id>/', event_delete_view, name='event-delete'),

    path('ajax-event-list/', ajax_event_list, name='ajax-event-list'),

]
