from django import template
from django.db.models import Q

from accounts.models import UserNotification
from tickets.models import Ticket, Notification

register = template.Library()


@register.filter
def ticket_count(request, count_type):
    if count_type == 'send_box':
        return Ticket.objects.filter(owner=request.user).count()
    if count_type == 'receive_box':
        return Ticket.objects.filter(receiver=request.user).count()
    if count_type == 'all':
        return Ticket.objects.all().count()
    return 0


@register.filter
def notification_count(request):
    if request.user.is_superuser:
        return UserNotification.objects.all().count()
    else:
        return UserNotification.objects.filter(user=request.user).count()
