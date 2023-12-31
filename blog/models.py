import random
from django.db.models import Q
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.urls import reverse
from tinymce.models import HTMLField
from django_jalali.db import models as jmodels
from django.contrib.sites.models import Site
from gallery.models import FileGallery
from utilities.arvancloud import CreateCnameThread, DeleteCnameThread
from utilities.slug_generator import name_to_url

MAGIC_WORDS = (('category', 'دسته'), ('keyword', 'کلمه کلیدی'))
POST_VIEW_TYPE = (('1', 'عکس + توضیحات'), ('2', 'عکس + توضیحات + بیشتر بخوانید'),
                  ('3', 'توضیحات بر روی عکس'), ('4', 'عکس + عنوان + توضیحات + تاریخ'),
                  ('5', 'عنوان + توضیحات + تاریخ + عکس'), ('6', 'تنها عکس'),
                  ('7', 'عنوان + عکس + توضیحات + بیشتر بخوانید'))
BLOG_THEME = (('1', 'پوسته 1'), ('2', 'پوسته 2'),)


class Blog(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False, verbose_name='عنوان')
    description = models.CharField(max_length=255, null=True, blank=True, verbose_name='توضیحات')
    keywords = models.CharField(max_length=255, null=True, blank=True, verbose_name='کلمات کلیدی')
    address = models.CharField(max_length=255, null=True, blank=True, verbose_name='آدرس')
    email = models.CharField(max_length=255, null=True, blank=True, verbose_name='ایمیل')
    mobile_phone = models.CharField(max_length=255, null=True, blank=True, verbose_name='شماره موبایل')
    landline = models.CharField(max_length=255, null=True, blank=True, verbose_name='شماره ثابت')
    generated_url = models.CharField(max_length=255, null=True, blank=True, editable=False, verbose_name='دامنه سیستمی')
    generated_url_id = models.CharField(max_length=255, null=True, blank=True, editable=False,
                                        verbose_name='آیدی دامنه سیستمی')
    custom_url = models.CharField(max_length=255, null=True, blank=True, verbose_name='دامنه شخصی')
    theme = models.CharField(max_length=255, default='پوسته 1', choices=BLOG_THEME, null=False, blank=False,
                             verbose_name='پوسته')
    created_at = jmodels.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=False, editable=False,
                                   verbose_name='ایجاد شده توسط')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'بلاگ'
        verbose_name_plural = 'بلاگ ها'

    def get_absolute_url(self):
        return reverse('blog:blog-edit-with-blog-id', kwargs={'blog_id': self.id})

    def save(self, *args, **kwargs):
        # we make sure generated_url and custom_url be unique
        new_cname = False
        domain = Site.objects.get_current().domain
        domain = str(domain).replace('https://', '').replace('http://', '').replace('/', ' ').split()
        if not self.generated_url:
            while True:
                random_number = random.randint(9999999999, 99999999999)
                new_url = f'{random_number}.{domain[0]}'
                blogs = Blog.objects.filter(generated_url=new_url)
                if blogs.count() == 0:
                    self.generated_url = new_url
                    self.generated_url_id = 'در حال تایید'
                    new_cname = True
                    break
        if self.custom_url is not None and self.custom_url != '':
            blogs = Blog.objects.filter(custom_url=self.custom_url)
            if blogs.count() != 0:
                blogs = blogs.filter(id=self.id)
                if blogs.count() == 0:
                    self.custom_url = f'دامنه {self.custom_url} غیر قابل انتخاب است. با مدیریت تماس بگیرید'
        super().save(*args, **kwargs)
        if new_cname:
            CreateCnameThread(self, domain_key=self.generated_url.split('.')[0]).start()


@receiver(post_delete, sender=Blog)
def delete_cname_receiver(sender, instance, **kwargs):
    DeleteCnameThread(cname_id=instance.generated_url_id).start()


class Slider(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=False, blank=False, verbose_name='بلاگ')
    images = models.ManyToManyField(FileGallery, blank=False, verbose_name='تصاویر')
    created_at = jmodels.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=False, editable=False,
                                   verbose_name='ایجاد شده توسط')

    def __str__(self):
        return self.id

    class Meta:
        verbose_name = 'تصویر اسلایدر هدر'
        verbose_name_plural = 'تصاویر اسلایدر هدر'


class HeaderMenuChildItem(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=False, blank=False, verbose_name='بلاگ')
    title = models.CharField(max_length=255, null=False, blank=False, verbose_name='عنوان')
    href = models.CharField(max_length=255, null=False, blank=False, verbose_name='لینک')
    created_at = jmodels.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=False, editable=False,
                                   verbose_name='ایجاد شده توسط')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'ایتم زیر منو'
        verbose_name_plural = 'ایتم های زیر منو'


class HeaderMenuParentItem(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=False, blank=False, verbose_name='بلاگ')
    title = models.CharField(max_length=255, null=False, blank=False, verbose_name='عنوان')
    href = models.CharField(max_length=255, null=False, blank=False, verbose_name='لینک')
    child = models.ManyToManyField(HeaderMenuChildItem, blank=True, verbose_name='زیر آیتم ها')
    created_at = jmodels.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=False, editable=False,
                                   verbose_name='ایجاد شده توسط')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'ایتم منو'
        verbose_name_plural = 'ایتم های منو'


class HeaderMenu(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=False, blank=False, verbose_name='بلاگ')
    title = models.CharField(max_length=255, null=False, blank=False, verbose_name='عنوان')
    menu_items = models.ManyToManyField(HeaderMenuParentItem, blank=False, verbose_name='آیتم های منو')
    created_at = jmodels.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=False, editable=False,
                                   verbose_name='ایجاد شده توسط')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'منو هدر'
        verbose_name_plural = 'منو های هدر'


class MagicWord(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=False, blank=False, verbose_name='بلاگ')
    title = models.CharField(max_length=255, null=False, blank=False, verbose_name='عنوان')
    slug_title = models.CharField(max_length=255, null=False, blank=False, editable=False, verbose_name='اسلاگ عنوان')
    word_type = models.CharField(max_length=255, choices=MAGIC_WORDS, null=False, blank=False, verbose_name='نوع کلمه')
    created_at = jmodels.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=False, editable=False,
                                   verbose_name='ایجاد شده توسط')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'کلمه جادویی'
        verbose_name_plural = 'کلمات جادویی'

    def save(self, *args, **kwargs):
        self.slug_title = name_to_url(self.title)
        super().save(*args, **kwargs)


class BlogPost(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=False, blank=False, verbose_name='بلاگ')
    title = models.CharField(max_length=255, null=False, blank=False, verbose_name='عنوان')
    slug_title = models.CharField(max_length=255, null=False, blank=False, editable=False, verbose_name='اسلاگ عنوان')
    categories = models.ManyToManyField(MagicWord, limit_choices_to={'word_type': 'category'},
                                        related_name='blog_post_magic_word_categories', blank=True,
                                        verbose_name='دسته ها')
    keywords = models.ManyToManyField(MagicWord, limit_choices_to={'word_type': 'keyword'},
                                      related_name='blog_post_magic_word_keywords', blank=True,
                                      verbose_name='کلمات کلیدی')
    feature_image = models.ForeignKey(FileGallery, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='تصویر شاخص')
    description = models.CharField(max_length=255, null=False, blank=False, verbose_name='توضیحات مختصر')
    content = HTMLField(null=True, blank=True, verbose_name='محتوا')
    created_at = jmodels.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated_at = jmodels.jDateTimeField(auto_now=True, verbose_name='تاریخ بروز رسانی')
    created_by = models.ForeignKey(User, related_name='blog_post_created_by', on_delete=models.CASCADE,
                                   null=False, editable=False, verbose_name='کاربر سازنده')
    updated_by = models.ForeignKey(User, related_name='blog_post_updated_by', on_delete=models.CASCADE,
                                   null=False, editable=False, verbose_name='کاربر بروز کننده')

    def __str__(self):
        return str(self.id) + ' | ' + self.title

    class Meta:
        ordering = ['-created_at', ]
        verbose_name = "بلاگ پست"
        verbose_name_plural = "بلاگ پست ها"

    def get_absolute_url(self):
        return reverse('blog:blog-post-detail-with-id', kwargs={'blog_post_id': self.id})

    def save(self, *args, **kwargs):
        self.slug_title = name_to_url(self.title)
        super().save(*args, **kwargs)


class BlogPostProfile(models.Model):
    blog_post = models.OneToOneField(BlogPost, on_delete=models.CASCADE, null=False, blank=False, editable=False,
                                     verbose_name='بلاگ پست')
    view_count = models.PositiveIntegerField(default=0, null=False, blank=False, verbose_name='دفعات مشاهده')

    def __str__(self):
        return self.blog_post.title[:10]

    class Meta:
        verbose_name = "ویژگی بلاگ پست"
        verbose_name_plural = "ویژگی های بلاگ پست ها"


@receiver(post_save, sender=BlogPost)
def blog_post_profile_get_or_create(sender, instance, created, **kwargs):
    try:
        old_blogpost = BlogPostProfile.objects.get(blog_post=instance)
        old_blogpost.save()
    except:
        BlogPostProfile.objects.create(blog_post=instance)


class BlogPostUserView(models.Model):
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, null=False, blank=False, editable=False,
                                  verbose_name='بلاگ پست')
    user_host_name = models.CharField(max_length=255, null=False, blank=False, editable=False,
                                      verbose_name='user host name')
    user_ip_address = models.CharField(max_length=255, null=False, blank=False, editable=False,
                                       verbose_name='user ip address')
    created_at = jmodels.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')

    def __str__(self):
        return self.blog_post.title[:10]

    class Meta:
        ordering = ['-created_at', ]
        verbose_name = "مشاهده بلاگ پست توسط کاربر"
        verbose_name_plural = "مشاهده بلاگ پست ها توسط کاربران"


@receiver(post_save, sender=BlogPostUserView)
def update_user_view_on_blog_post_profile(sender, instance, created, **kwargs):
    try:
        blog_post_user_views = BlogPostUserView.objects.filter(meta_post=instance.meta_post)
        blog_post_profile = BlogPostProfile.objects.get(meta_post=instance.meta_post)
        blog_post_profile.view_count = blog_post_user_views.count()
        blog_post_profile.save()
    except Exception as e:
        print(str(e))
        pass


class BlogPostReply(models.Model):
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, null=False, blank=False, verbose_name='بلاگ پست')
    replier = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, verbose_name='نظر گذارنده')
    comment = models.TextField(null=False, blank=False, verbose_name='نظر')
    publish_on_site = models.BooleanField(default=False, verbose_name='نمایش نظر در سایت')
    created_at = jmodels.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')

    def __str__(self):
        return self.replier.username + ' | ' + self.comment[:20]

    class Meta:
        ordering = ['-created_at', ]
        verbose_name = "نظر بلاگ پست"
        verbose_name_plural = "نظر های بلاگ پست ها"


class FeaturePost(models.Model):
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, null=False, blank=False, verbose_name='بلاگ پست')
    order = models.PositiveSmallIntegerField(default=0, null=False, blank=False, verbose_name='ترتیب نمایش')

    def __str__(self):
        return self.blog_post.title

    class Meta:
        ordering = ['order', ]
        verbose_name = 'پست ویژه'
        verbose_name_plural = 'پست های ویژه'
