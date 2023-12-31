import jdatetime
from django.db.models import Q
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from accounts.models import VIPPlan, ExtraStoragePlan
from auto_robots.models import MetaPost
from blog.models import BlogPost, Blog
from blog.views import BlogFrontHome, render_with_desired_theme
from gallery.models import FileGallery
from gallery.templatetags.gallery_custom_tag import number_with_ext
from gallery.views import user_maximum_quote_size_in_mb, user_all_file_size_in_mb


class Dashboard(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.context = {'page_title': 'پورتال مدیریت آسان شبکه های شخصی و سازمانی',
                        'navigation_icon_menu_id': 'overview',
                        'navigation_menu_body_id': 'navigationDashboard',
                        'navigation_menu_body_sub_item_id': 'dashboard-latest-posts',
                        }

    def get(self, request, *args, **kwargs):
        if request.x_blog:
            try:
                try:
                    blog = Blog.objects.get(Q(generated_url=request.get_host()) | Q(custom_url=request.get_host()))
                    self.context = {'page_title': f'{blog.title}'}
                except:
                    return render(request, '404.html')
                self.context['blog'] = blog
                return render_with_desired_theme(request, 'index.html', self.context, blog)
            except Exception as e:
                return render(request, '404.html')

        if request.user.is_authenticated:
            today = jdatetime.datetime.now()
            metas = MetaPost.objects.filter(created_by=request.user)
            self.context['latest_metas'] = metas[:6]
            all_time_metas = metas
            has_queued_metas = metas.filter(message_status='queued')
            today_has_sent_metas = request.user.profile_user.metapost_daily_sent
            all_time_has_sent_metas = metas.filter(message_status='sent')
            self.context['all_time_metas'] = all_time_metas.count()
            self.context['has_queued_metas'] = has_queued_metas.count()
            self.context['today_has_sent_metas'] = today_has_sent_metas
            self.context['all_time_has_sent_metas'] = all_time_has_sent_metas.count()
            if metas.count() != 0:
                self.context['first_meta'] = metas[0].created_at
            if has_queued_metas.count() != 0:
                self.context['last_queued_meta'] = has_queued_metas.latest('id').created_at

            user_all_file_size = user_all_file_size_in_mb(request.user)
            all_files_size_with_ext = number_with_ext(user_all_file_size)
            self.context['all_files_size_with_ext'] = all_files_size_with_ext
            all_files_percentage = int((user_all_file_size / user_maximum_quote_size_in_mb(request.user)) * 100)
            self.context['all_files_percentage'] = all_files_percentage

            metapost_daily_limit = request.user.profile_user.default_metapost_daily_send_limit
            if request.user.profile_user.vip_plan_expiry_date:
                if request.user.profile_user.vip_plan_expiry_date > today:
                    metapost_daily_limit = request.user.profile_user.vip_plan.metapost_daily_send_limit
            self.context['metapost_daily_limit'] = metapost_daily_limit
            self.context['metapost_daily_percentage'] = int((request.user.profile_user.metapost_daily_sent / metapost_daily_limit) * 100)
            return render(request, 'dashboard/dashboard.html', self.context)
        else:
            return redirect('accounts:login')

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return render(request, 'financial/financial-brokers-list.html', self.context)
        else:
            return redirect('accounts:login')


class PricingView(View):
    def __init__(self):
        super().__init__()
        self.context = {'page_title': 'اشتراک ها و قیمت ها',
                        'navigation_icon_menu_id': 'pricing',
                        'navigation_menu_body_id': 'navigationSubscription',
                        'breadcrumb_1': 'خانه',
                        'breadcrumb_2': 'مالی',
                        }

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            vip_plans = VIPPlan.objects.filter()
            self.context['vip_plans'] = vip_plans
            storage_plans = ExtraStoragePlan.objects.filter()
            self.context['storage_plans'] = storage_plans
            return render(request, 'accounts/vip-subscription/pricing.html', self.context)
        else:
            return redirect('accounts:login')

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return render(request, '404.html')
        else:
            return redirect('accounts:login')