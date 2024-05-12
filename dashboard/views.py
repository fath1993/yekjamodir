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
            return render(request, 'dashboard/dashboard.html', self.context)
        else:
            return redirect('accounts:login')

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return render(request, 'financial/financial-brokers-list.html', self.context)
        else:
            return redirect('accounts:login')


