import jdatetime
from django import template
import locale
from accounts.models import Profile, Invoice
from subscription.models import LicenceSetting

register = template.Library()


@register.filter
def calculate_subscription_daily_price(request):
    licence_setting = LicenceSetting.objects.filter().latest('id')
    profile = Profile.objects.get(user=request.user)

    daily_price = 0

    if profile.financial_licence:
        daily_price += licence_setting.financial_licence_price
    if profile.warehouse_licence:
        daily_price += licence_setting.warehouse_licence_price
    if profile.social_licence:
        daily_price += licence_setting.social_licence_price
    if profile.blog_licence:
        daily_price += licence_setting.blog_licence_price
    if profile.automation_licence:
        daily_price += licence_setting.automation_licence_price

    return daily_price


@register.filter
def today_subscription_detail(request, number):
    now = jdatetime.datetime.now()
    star_of_today = jdatetime.datetime(year=now.year, month=now.month, day=now.day, hour=0, minute=0, second=0)

    today_active_service = f''''''

    today_price = 0
    try:
        invoice = Invoice.objects.get(authority='financial_licence', invoice_type='برداشت از حساب',
                                      user=request.user, created_at__gte=star_of_today)
        today_price += invoice.amount
        today_active_service += 'لایسنس مالی, '
    except:
        pass
    try:
        invoice = Invoice.objects.get(authority='warehouse_licence', invoice_type='برداشت از حساب',
                                      user=request.user, created_at__gte=star_of_today)
        today_price += invoice.amount
        today_active_service += 'لایسنس انبار داری, '
    except:
        pass
    try:
        invoice = Invoice.objects.get(authority='social_licence', invoice_type='برداشت از حساب',
                                      user=request.user, created_at__gte=star_of_today)
        today_price += invoice.amount
        today_active_service += 'لایسنس شبکه های اجتماعی, '
    except:
        pass
    try:
        invoice = Invoice.objects.get(authority='blog_licence', invoice_type='برداشت از حساب',
                                      user=request.user, created_at__gte=star_of_today)
        today_price += invoice.amount
        today_active_service += 'لایسنس بلاگ, '
    except:
        pass
    try:
        invoice = Invoice.objects.get(authority='automation_licence', invoice_type='برداشت از حساب',
                                      user=request.user, created_at__gte=star_of_today)
        today_price += invoice.amount
        today_active_service += 'لایسنس اتوماسیون, '
    except:
        pass

    if number == '0':
        return today_price
    else:
        return today_active_service


@register.filter
def has_user_active_licence(request, licence_name):
    now = jdatetime.datetime.now()
    star_of_today = jdatetime.datetime(year=now.year, month=now.month, day=now.day, hour=0, minute=0, second=0)

    if licence_name == 'financial_licence':
        try:
            invoice = Invoice.objects.get(authority='financial_licence', invoice_type='برداشت از حساب',
                                          user=request.user, created_at__gte=star_of_today)
            return True
        except:
            return False

    if licence_name == 'warehouse_licence':
        try:
            invoice = Invoice.objects.get(authority='warehouse_licence', invoice_type='برداشت از حساب',
                                          user=request.user, created_at__gte=star_of_today)
            return True
        except:
            return False

    if licence_name == 'social_licence':
        try:
            invoice = Invoice.objects.get(authority='social_licence', invoice_type='برداشت از حساب',
                                          user=request.user, created_at__gte=star_of_today)
            return True
        except:
            return False

    if licence_name == 'blog_licence':
        try:
            invoice = Invoice.objects.get(authority='blog_licence', invoice_type='برداشت از حساب',
                                          user=request.user, created_at__gte=star_of_today)
            return True
        except:
            return False

    if licence_name == 'automation_licence':
        try:
            invoice = Invoice.objects.get(authority='automation_licence', invoice_type='برداشت از حساب',
                                          user=request.user, created_at__gte=star_of_today)
            return True
        except:
            return False


@register.filter
def get_profile_wallet_balance(request):
    profile = Profile.objects.get(user=request.user)
    return profile.wallet_balance


@register.filter
def calculate_subscription_send_message_price(request):
    licence_setting = LicenceSetting.objects.filter().latest('id')
    return licence_setting.send_message_price


@register.filter
def subtract_two_value(value_1, value_2):
    value_1 = int(value_1)
    value_2 = int(value_2)
    return value_1 - value_2


@register.filter
def amount_human_readable(content):
    content = str(content)
    # Set locale to use comma as a thousands separator
    locale.setlocale(locale.LC_ALL, '')

    # Remove non-numeric characters and commas
    numeric_value = ''.join(char for char in content if char.isdigit() or char == '.')

    # Use locale to format the number
    try:
        # Parse the numeric value as float
        numeric_value = float(numeric_value)

        # Format the numeric value with a thousands separator
        formatted_value = locale.format_string('%0.0f', numeric_value, grouping=True)
    except ValueError:
        # Handle the case where the input is not a valid number
        formatted_value = '0'

    return formatted_value


def profile_withdraw_message_price(profile):
    licence_setting = LicenceSetting.objects.filter().latest('id')
    profile.wallet_balance -= licence_setting.send_message_price
    profile.save()
