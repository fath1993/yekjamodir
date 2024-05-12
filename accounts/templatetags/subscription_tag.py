import jdatetime
from django import template

from accounts.models import VIPPlan, Licence

register = template.Library()


@register.filter
def vip_plan_check_if_current_is_better(current_active_vip_plan, checking_vip_plan):
    if not current_active_vip_plan:
        return False
    else:
        if current_active_vip_plan.price > checking_vip_plan.price:
            return True
        else:
            return False


@register.filter
def all_available_licence(request):
    return Licence.objects.all()


@register.filter
def user_vip_plan(request):
    now = jdatetime.datetime.now()
    profile = request.user.profile_user

    if profile.vip_plan_expiry_date > now:
        return profile.vip_plan
    else:
        return None


@register.filter
def user_access_to_licence(request):
    return user_vip_plan(request).has_access_to_licence.all()


@register.filter
def demo_used_once(request):
    if request.user.profile_user.demo_used_once:
        return True
    else:
        return False

