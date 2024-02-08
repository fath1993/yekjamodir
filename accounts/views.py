import random

import jdatetime
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
import re

from accounts.models import SMSAuthCode, VIPPlan
from auto_robots.models import MetaPost
from blog.models import BlogPost
from financial_accounting.models import TransactionRecord
from utilities.http_metod import fetch_data_from_http_post, fetch_single_file_from_http_file
from utilities.send_sms import SendVerificationSMSThread


def login_view(request):
    context = {'page_title': 'ورود به حساب کاربری'}
    if request.user.is_authenticated:
        return redirect('panel:panel-dashboard')
    else:
        if request.method == 'POST':
            form_type = fetch_data_from_http_post(request, 'form_type', context)
            if form_type == 'password_login':
                context['active_tab'] = 'password_login'
                try:
                    username = request.POST['username']
                    if username == '':
                        username = None
                except:
                    username = None
                if username is None:
                    context['err'] = 'نام کاربری بدرستی وارد نشده است'
                    return render(request, 'accounts/login.html', context)
                try:
                    password = request.POST['password']
                    if password == '':
                        password = None
                except:
                    password = None
                if password is None:
                    context['username'] = username
                    context['err'] = 'کلمه عبور بدرستی وارد نشده است'
                    return render(request, 'accounts/login.html', context)

                user = authenticate(request=request, username=username, password=password)
                if user is not None:
                    login(request=request, user=user)
                    return redirect('dashboard:dashboard')
                else:
                    try:
                        user = User.objects.get(username=username)
                        context['username'] = username
                        context['err'] = 'کلمه عبور صحیح نیست'
                        return render(request, 'accounts/login.html', context)
                    except:
                        context['username'] = username
                        context['err'] = 'نام کاربری در سامانه وجود ندارد'
                        return render(request, 'accounts/login.html', context)
            else:
                context['active_tab'] = 'sms_login'
                phone_number = fetch_data_from_http_post(request, 'phone_number', context)
                try:
                    user = User.objects.get(username=phone_number)
                    try:
                        sms_auth_code = SMSAuthCode.objects.get(phone_number=phone_number)
                        time_spent = (jdatetime.datetime.now() - sms_auth_code.created_at).total_seconds()
                        if time_spent <= 120:
                            context['sms_err'] = 'از ارسال قبلی کمتر از دو دقیقه گذشته است'
                            return render(request, 'accounts/login.html', context)
                        else:
                            sms_auth_code.delete()
                    except Exception as e:
                        pass
                    random_otp = random.randint(100000, 999999)
                    new_sms_auth_code = SMSAuthCode.objects.create(
                        phone_number=phone_number,
                        pass_code=random_otp,
                    )
                    SendVerificationSMSThread(phone_number, '942224', f'{random_otp}').start()
                    context['alert'] = 'کد تایید به شماره همراه شما پیامک شد'
                    context['phone_number'] = phone_number
                    return render(request, 'accounts/two-step.html', context)
                except Exception as e:
                    print(str(e))
                    context['sms_err'] = 'شماره همراه در سامانه موجود نیست'
                    return render(request, 'accounts/login.html', context)
        else:
            context['active_tab'] = 'password_login'
            return render(request, 'accounts/login.html', context)


def logout_view(request):
    logout(request=request)
    return redirect('accounts:login')


def signup_view(request):
    context = {'page_title': 'ثبت نام کاربر جدید'}
    if request.user.is_authenticated:
        return redirect('panel:panel-dashboard')
    else:
        if request.method == 'POST':
            full_name = fetch_data_from_http_post(request, 'full_name', context)
            if full_name is None:
                context['err'] = 'نام و نام خانوادگی بدرستی وارد نشده است'
                return render(request, 'accounts/signup.html', context)
            phone_number = fetch_data_from_http_post(request, 'phone_number', context)
            if phone_number is None:
                context['full_name'] = full_name
                context['err'] = 'شماره همراه بدرستی وارد نشده است'
                return render(request, 'accounts/signup.html', context)
            email = fetch_data_from_http_post(request, 'email', context)
            if not re.fullmatch(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b', email):
                email = None
            if email is None:
                context['full_name'] = full_name
                context['phone_number'] = phone_number
                context['err'] = 'ایمیل بدرستی وارد نشده است'
                return render(request, 'accounts/signup.html', context)
            landline = fetch_data_from_http_post(request, 'landline', context)
            address = fetch_data_from_http_post(request, 'address', context)
            password1 = fetch_data_from_http_post(request, 'password_1', context)
            if password1 is None:
                context['full_name'] = full_name
                context['phone_number'] = phone_number
                context['email'] = email
                context['err'] = 'کلمه عبور بدرستی وارد نشده است'
                return render(request, 'accounts/signup.html', context)
            password2 = fetch_data_from_http_post(request, 'password_2', context)
            if password2 is None:
                context['full_name'] = full_name
                context['phone_number'] = phone_number
                context['email'] = email
                context['err'] = 'تکرار کلمه عبور بدرستی وارد نشده است'
                return render(request, 'accounts/signup.html', context)
            if password1 != password2:
                context['full_name'] = full_name
                context['phone_number'] = phone_number
                context['email'] = email
                context['err'] = 'کلمه عبور بدرستی تکرار نشده است'
                return render(request, 'accounts/signup.html', context)

            try:
                user = User.objects.get(username=phone_number)
                context['full_name'] = full_name
                context['phone_number'] = phone_number
                context['email'] = email
                context['err'] = 'نام کاربری از قبل در سامانه وجود دارد'
                return render(request, 'accounts/signup.html', context)
            except:
                context['err'] = 'ثبت نام شما تکمیل شد. اکانت شما پس از بررسی تایید و فعال خواهد گردید'
                user = User.objects.create_user(username=phone_number, first_name=full_name,
                                                email=email, password=password1, is_active=False)
                profile = user.profile_user
                profile.mobile_phone_number = phone_number
                profile.save()
                login(request=request, user=user)
                return render(request, 'accounts/signup.html', context)
                # return redirect('dashboard:dashboard')

        return render(request, 'accounts/signup.html', context)


def two_step_verification_view(request, phone_number=None):
    context = {'page_title': 'کد تایید'}
    if request.user.is_authenticated:
        return redirect('dashboard:dashboard')
    else:
        if request.method == 'POST':
            verification_code = fetch_data_from_http_post(request, 'verification_code', context)
            phone_number = fetch_data_from_http_post(request, 'phone_number', context)
            if phone_number is None:
                context['err'] = 'شماره همراه خالی است'
                return render(request, 'accounts/two-step.html', context)
            if verification_code is None:
                context['err'] = 'کد پیامکی خالی است'
                return render(request, 'accounts/two-step.html', context)
            try:
                user = User.objects.get(username=phone_number)
                try:
                    sms_auth_code = SMSAuthCode.objects.get(phone_number=phone_number, pass_code=verification_code)
                    time_spent = (jdatetime.datetime.now() - sms_auth_code.created_at).total_seconds()
                    if time_spent > 120:
                        context['err'] = 'کد تایید منقضی شده است'
                        return render(request, 'accounts/two-step.html', context)
                    else:
                        sms_auth_code.delete()
                        login(request=request, user=user)
                        return redirect('dashboard:dashboard')
                except Exception as e:
                    context['err'] = 'کد تایید اشتباه است'
                    return render(request, 'accounts/two-step.html', context)
            except Exception as e:
                context['err'] = 'شماره همراه در سامانه موجود نیست'
                return render(request, 'accounts/two-step.html', context)
        else:
            return redirect('accounts:login')


def ajax_two_step_verification_retry_send(request):
    context = {}
    phone_number = fetch_data_from_http_post(request, 'phone_number', context)
    if not phone_number:
        return JsonResponse({'message': 'شماره همراه صحیح نیست'})
    try:
        user = User.objects.get(username=phone_number)
        try:
            sms_auth_code = SMSAuthCode.objects.get(phone_number=phone_number)
            time_spent = (jdatetime.datetime.now() - sms_auth_code.created_at).total_seconds()
            if time_spent <= 120:
                return JsonResponse({'message': 'از ارسال پیامک قبلی کمتر از دو دقیقه گذشته است'})
            else:
                sms_auth_code.delete()
        except Exception as e:
            pass
        random_otp = random.randint(100000, 999999)
        new_sms_auth_code = SMSAuthCode.objects.create(
            phone_number=phone_number,
            pass_code=random_otp,
        )
        SendVerificationSMSThread(phone_number, '942224', f'{random_otp}').start()

        return JsonResponse({'message': 'کد تایید به شما پیامک شد'})
    except Exception as e:
        print(str(e))
        return JsonResponse({'message': 'شماره همراه موجود نیست'})


class ProfileView(View):
    def __init__(self):
        super().__init__()
        self.context = {'page_title': 'پروفایل کاربر',
                        'navigation_icon_menu_id': 'overview',
                        'navigation_menu_body_id': 'navigationDashboard',
                        'navigation_menu_body_sub_item_id': 'dashboard-latest-posts',
                        'breadcrumb_1': 'خانه',
                        'breadcrumb_2': 'پروفایل',
                        }

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            all_time_transaction_records = TransactionRecord.objects.filter(created_by=request.user).count()
            all_time_metas = MetaPost.objects.filter(created_by=request.user).count()
            all_time_blog_posts = BlogPost.objects.filter(created_by=request.user).count()
            self.context['all_time_transaction_records'] = all_time_transaction_records
            self.context['all_time_metas'] = all_time_metas
            self.context['all_time_blog_posts'] = all_time_blog_posts
            profile_completion_percentage = 50
            if request.user.email:
                profile_completion_percentage += 10
            if request.user.first_name:
                profile_completion_percentage += 10
            if request.user.profile_user.landline:
                profile_completion_percentage += 10
            if request.user.profile_user.address:
                profile_completion_percentage += 10
            if request.user.profile_user.profile_pic:
                profile_completion_percentage += 10
            self.context['profile_completion_percentage'] = profile_completion_percentage
            return render(request, 'accounts/profile.html', self.context)
        else:
            return redirect('accounts:login')


class ProfileEdit(View):
    def __init__(self):
        super().__init__()
        self.context = {'page_title': 'ویرایش پروفایل کاربر',
                        'navigation_icon_menu_id': 'overview',
                        'navigation_menu_body_id': 'navigationDashboard',
                        'navigation_menu_body_sub_item_id': 'dashboard-latest-posts',
                        'breadcrumb_1': 'خانه',
                        'breadcrumb_2': 'ویرایش پروفایل',
                        }

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return render(request, 'accounts/profile-edit.html', self.context)
        else:
            return redirect('accounts:login')

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            user = request.user
            profile = request.user.profile_user

            full_name = fetch_data_from_http_post(request, 'full_name', self.context)
            email = fetch_data_from_http_post(request, 'email', self.context)
            address = fetch_data_from_http_post(request, 'address', self.context)
            landline = fetch_data_from_http_post(request, 'landline', self.context)
            old_password = fetch_data_from_http_post(request, 'old_password', self.context)
            password_1 = fetch_data_from_http_post(request, 'password_1', self.context)
            password_2 = fetch_data_from_http_post(request, 'password_2', self.context)
            profile_pic = fetch_single_file_from_http_file(request, 'profile_pic', self.context)

            if old_password and password_1 and password_2:
                old_user = authenticate(username=user.username, password=old_password)
                if not old_user:
                    self.context['password_check'] = True
                    self.context['alert'] = 'رمز قدیم بدرستی وارد نشده است'
                    return render(request, 'accounts/profile-edit.html', self.context)
                if len(str(password_1)) < 8:
                    self.context['password_check'] = True
                    self.context['alert'] = 'طول رمز میبایست حداقل 8 کاراکتر باشد'
                    return render(request, 'accounts/profile-edit.html', self.context)
                user.set_password(password_1)
                login(request, user)
            elif not old_password and not password_1 and not password_2:
                pass
            else:
                self.context['password_check'] = True
                self.context['alert'] = 'رمز قدیم و رمز جدید و تکرار رمز جدید بصورت کامل وارد نشده است'
                return render(request, 'accounts/profile-edit.html', self.context)

            if full_name:
                user.first_name = full_name
            if email:
                user.email = email
            user.save()
            if address:
                profile.address = address
            if landline:
                profile.landline = landline
            if profile_pic:
                profile.profile_pic = profile_pic
            profile.save()
            return redirect('accounts:profile')
        else:
            return redirect('accounts:login')


class InvoiceView(View):
    def __init__(self):
        super().__init__()
        self.context = {'page_title': 'صورت حساب',
                        'navigation_icon_menu_id': 'pricing',
                        'navigation_menu_body_id': 'navigationSubscription',
                        'breadcrumb_1': 'خانه',
                        'breadcrumb_2': 'مالی',
                        }

    def get(self, request, invoice_id=None, *args, **kwargs):
        if request.user.is_authenticated:
            return render(request, 'accounts/vip-subscription/invoice.html', self.context)
        else:
            return redirect('accounts:login')

    def post(self, request, invoice_id=None, *args, **kwargs):
        if request.user.is_authenticated:
            upgrade_to = fetch_data_from_http_post(request, 'upgrade_to', self.context)
            vip_plan_id = fetch_data_from_http_post(request, 'vip_plan_id', self.context)

            vip_plan = VIPPlan.objects.get(id=vip_plan_id)
            if upgrade_to:
                today = jdatetime.datetime.now()
                user_current_plan = request.user.profile_user.vip_plan
                user_current_plan_expiry_date = request.user.profile_user.vip_plan_expiry_date
                # user_vipe
            return render(request, '404.html')
        else:
            return redirect('accounts:login')


class InvoiceList(View):
    def __init__(self):
        super().__init__()
        self.context = {'page_title': 'صورت حساب های خرید',
                        'navigation_icon_menu_id': 'accounts_invoices_list',
                        'navigation_menu_body_id': 'navigationSubscription',
                        'breadcrumb_1': 'خانه',
                        'breadcrumb_2': 'مالی',
                        }

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return render(request, 'accounts/vip-subscription/invoice.html', self.context)
        else:
            return redirect('accounts:login')

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return render(request, '404.html')
        else:
            return redirect('accounts:login')