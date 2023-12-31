from django import template

from accounts.models import VIPPlan

register = template.Library()


@register.filter
def vip_plan_check_if_better(current_active_vip_plan, checking_vip_plan):
    if checking_vip_plan.price > current_active_vip_plan.price:
        return True
    else:
        return False
