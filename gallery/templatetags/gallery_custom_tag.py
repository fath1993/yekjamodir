# my_app/templatetags/my_custom_filters.py
import os

import jdatetime
from django import template

from gallery.views import user_maximum_quote_size_in_mb, file_ext, number_with_ext

register = template.Library()


@register.filter
def divide(value_1, value_2):
    try:
        return int(int(value_1) / int(value_2))
    except (ValueError, ZeroDivisionError):
        return 0


@register.filter
def file_ext_tag(file_path):
    return file_ext(file_path)


@register.filter
def number_with_ext_tag(value):
    return number_with_ext(value)


@register.filter
def int_percentage(int_string):
    int_string = round((int(int_string) / 100), 2)
    return int_string


@register.filter
def file_name(name):
    return str(name).replace('file-gallery/', '')[:10]


@register.filter
def user_maximum_quota_size_tag(user):
    return number_with_ext(user_maximum_quote_size_in_mb(user))


@register.filter
def check_user_is_vip(profile):
    today = jdatetime.datetime.now()
    if profile.vip_plan_expiry_date:
        if profile.vip_plan_expiry_date > today:
            return True
    return False
