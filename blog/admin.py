import random
import time

from django.contrib import admin
from django.contrib.sites.models import Site

from blog.models import Blog, Slider, HeaderMenuChildItem, HeaderMenuParentItem, HeaderMenu, MagicWord, BlogPost, \
    BlogPostProfile, BlogPostUserView, BlogPostReply, FeaturePost
from utilities.arvancloud import CreateCnameThread, DeleteCnameThread


@admin.action(description="بازسازی url سیستمی")
def refresh_generated_url(modeladmin, request, queryset):
    domain = Site.objects.get_current().domain
    domain = str(domain).replace('https://', '').replace('http://', '').replace('/', ' ').split()
    for query in queryset:
        DeleteCnameThread(cname_id=query.generated_url_id).start()
        while True:
            random_number = random.randint(9999999999, 99999999999)
            new_url = f'{random_number}.{domain[0]}'
            blogs = Blog.objects.filter(generated_url=new_url)
            if blogs.count() == 0:
                query.generated_url = new_url
                query.generated_url_id = 'در حال تایید'
                query.save()
                break
        CreateCnameThread(query, domain_key=query.generated_url.split('.')[0]).start()
        time.sleep(0.1)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'description',
        'generated_url',
        'custom_url',
        'created_at',
        'created_by',
    )

    readonly_fields = (
        'generated_url',
        'generated_url_id',
        'created_at',
        'created_by',
    )

    fields = (
        'title',
        'description',
        'keywords',
        'address',
        'email',
        'mobile_phone',
        'landline',
        'generated_url',
        'generated_url_id',
        'custom_url',
        'theme',
        'created_at',
        'created_by',
    )

    @admin.display(description="تاریخ ایجاد", empty_value='???')
    def created_at_display(self, obj):
        data_time = str(obj.created_at.strftime('%Y-%m-%d - %H:%M'))
        return data_time

    def save_model(self, request, instance, form, change):
        instance = form.save(commit=False)
        if not change:
            instance.created_by = request.user
        instance.save()
        form.save_m2m()
        return instance

    actions = [refresh_generated_url, ]


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = (
        'blog',
        'created_at',
        'created_by',
    )

    readonly_fields = (
        'created_at',
        'created_by',
    )

    fields = (
        'blog',
        'images',
        'created_at',
        'created_by',
    )

    @admin.display(description="تاریخ ایجاد", empty_value='???')
    def created_at_display(self, obj):
        data_time = str(obj.created_at.strftime('%Y-%m-%d - %H:%M'))
        return data_time

    def save_model(self, request, instance, form, change):
        instance = form.save(commit=False)
        if not change:
            instance.created_by = request.user
        instance.save()
        form.save_m2m()
        return instance


@admin.register(HeaderMenuChildItem)
class HeaderMenuChildItemAdmin(admin.ModelAdmin):
    list_display = (
        'blog',
        'title',
        'href',
        'created_at',
        'created_by',
    )

    readonly_fields = (
        'created_at',
        'created_by',
    )

    fields = (
        'blog',
        'title',
        'href',
        'created_at',
        'created_by',
    )

    @admin.display(description="تاریخ ایجاد", empty_value='???')
    def created_at_display(self, obj):
        data_time = str(obj.created_at.strftime('%Y-%m-%d - %H:%M'))
        return data_time

    def save_model(self, request, instance, form, change):
        instance = form.save(commit=False)
        if not change:
            instance.created_by = request.user
        instance.save()
        form.save_m2m()
        return instance


@admin.register(HeaderMenuParentItem)
class HeaderMenuParentItemAdmin(admin.ModelAdmin):
    list_display = (
        'blog',
        'title',
        'href',
        'created_at',
        'created_by',
    )

    readonly_fields = (
        'created_at',
        'created_by',
    )

    fields = (
        'blog',
        'title',
        'href',
        'child',
        'created_at',
        'created_by',
    )

    @admin.display(description="تاریخ ایجاد", empty_value='???')
    def created_at_display(self, obj):
        data_time = str(obj.created_at.strftime('%Y-%m-%d - %H:%M'))
        return data_time

    def save_model(self, request, instance, form, change):
        instance = form.save(commit=False)
        if not change:
            instance.created_by = request.user
        instance.save()
        form.save_m2m()
        return instance


@admin.register(HeaderMenu)
class HeaderMenuAdmin(admin.ModelAdmin):
    list_display = (
        'blog',
        'title',
        'created_at',
        'created_by',
    )

    readonly_fields = (
        'created_at',
        'created_by',
    )

    fields = (
        'blog',
        'title',
        'menu_items',
        'created_at',
        'created_by',
    )

    @admin.display(description="تاریخ ایجاد", empty_value='???')
    def created_at_display(self, obj):
        data_time = str(obj.created_at.strftime('%Y-%m-%d - %H:%M'))
        return data_time

    def save_model(self, request, instance, form, change):
        instance = form.save(commit=False)
        if not change:
            instance.created_by = request.user
        instance.save()
        form.save_m2m()
        return instance


@admin.register(MagicWord)
class MagicWordAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'slug_title',
        'word_type',
        'created_at',
        'created_by',
    )

    list_filter = (
        'word_type',
    )

    readonly_fields = (
        'slug_title',
        'created_at',
        'created_by',
    )

    fields = (
        'title',
        'slug_title',
        'word_type',
        'created_at',
        'created_by',
    )

    @admin.display(description="تاریخ ایجاد", empty_value='???')
    def created_at_display(self, obj):
        data_time = str(obj.created_at.strftime('%Y-%m-%d - %H:%M'))
        return data_time

    def save_model(self, request, instance, form, change):
        instance = form.save(commit=False)
        if not change:
            instance.created_by = request.user
        instance.save()
        form.save_m2m()
        return instance


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'created_at_display',
        'updated_at_display',
    )
    search_fields = (
        'title',
        'description',
        'content',
    )
    readonly_fields = (
        'slug_title',
        'created_at',
        'updated_at',
        'created_by',
        'updated_by',
    )
    fields = (
        'title',
        'slug_title',
        'categories',
        'keywords',
        'description',
        'feature_image',
        'content',
        'created_at',
        'updated_at',
        'created_by',
        'updated_by',
    )

    @admin.display(description="تاریخ ایجاد", empty_value='???')
    def created_at_display(self, obj):
        data_time = str(obj.created_at.strftime('%Y-%m-%d - %H:%M'))
        return data_time

    @admin.display(description="تاریخ آخرین ویرایش", empty_value='???')
    def updated_at_display(self, obj):
        data_time = str(obj.updated_at.strftime('%Y-%m-%d - %H:%M'))
        return data_time

    def save_model(self, request, instance, form, change):
        instance = form.save(commit=False)
        if not change:
            instance.created_by = request.user
            instance.updated_by = request.user
        else:
            instance.updated_by = request.user
        instance.save()
        form.save_m2m()
        return instance


@admin.register(BlogPostProfile)
class BlogPostProfileAdmin(admin.ModelAdmin):
    list_display = (
        'blog_post',
        'view_count',
    )
    readonly_fields = (
        'blog_post',
        'view_count',
    )
    fields = (
        'blog_post',
        'view_count',
    )

    def has_add_permission(self, request):
        return False


@admin.register(BlogPostUserView)
class BlogPostUserViewAdmin(admin.ModelAdmin):
    list_display = (
        'blog_post',
        'user_host_name',
        'user_ip_address',
        'created_at',
    )
    readonly_fields = (
        'blog_post',
        'user_host_name',
        'user_ip_address',
        'created_at',
    )
    fields = (
        'blog_post',
        'user_host_name',
        'user_ip_address',
        'created_at',
    )

    @admin.display(description="تاریخ ایجاد", empty_value='???')
    def created_at_display(self, obj):
        data_time = str(obj.created_at.strftime('%Y-%m-%d - %H:%M'))
        return data_time

    def has_add_permission(self, request):
        return False


@admin.register(BlogPostReply)
class BlogPostReplyAdmin(admin.ModelAdmin):
    list_display = (
        'blog_post',
        'replier',
        'comment',
        'created_at_display',
        'publish_on_site',
    )
    readonly_fields = (
        'created_at',
    )
    fields = (
        'blog_post',
        'replier',
        'comment',
        'created_at',
        'publish_on_site',
    )

    @admin.display(description="تاریخ ایجاد", empty_value='???')
    def created_at_display(self, obj):
        data_time = str(obj.created_at.strftime('%Y-%m-%d - %H:%M'))
        return data_time

    def save_model(self, request, instance, form, change):
        instance = form.save(commit=False)
        instance.replier = request.user
        if change:
            if not request.user.is_superuser:
                instance.publish_on_site = False
        instance.save()
        form.save_m2m()
        return instance


@admin.register(FeaturePost)
class FeaturePostAdmin(admin.ModelAdmin):
    list_display = (
        'blog_post',
        'order',
    )

    fields = (
        'blog_post',
        'order',
    )