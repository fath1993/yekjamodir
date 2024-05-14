import jdatetime
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.db.models import Q
from blog.models import MagicWord, BlogPost, Blog, BlogPostReply
from auto_robots.models import Bot
from subscription.templatetags.subscription_tag import has_user_active_licence
from utilities.blog_post_view_counter import BlogPostViewCounterThread
from utilities.http_metod import fetch_data_from_http_post, fetch_single_file_from_http_file, \
    fetch_datalist_from_http_post
from utilities.slug_generator import name_to_url
from django.contrib.sitemaps import Sitemap
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.urls import reverse


# --------------- admin panel ------------------------
class BlogNew(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.context = {'page_title': 'ساخت بلاگ جدید',
                        'navigation_icon_menu_id': 'service',
                        'navigation_menu_body_id': 'navigationService',
                        'navigation_menu_body_sub_item_id': 'blog-list',
                        'breadcrumb_1': 'خانه',
                        'breadcrumb_2': 'بلاگ',
                        'breadcrumb_3': 'ساخت بلاگ جدید',
                        }

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return render(request, 'blog-admin/blog-new.html', self.context)
        else:
            return redirect('accounts:login')

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if not has_user_active_licence(request, 'blog_licence'):
                return redirect('subscription:change-vip-plan')

            blog_name = fetch_data_from_http_post(request, 'blog_name', self.context)
            blog_description = fetch_data_from_http_post(request, 'blog_description', self.context)
            blog_keywords = fetch_data_from_http_post(request, 'blog_keywords', self.context)
            blog_address = fetch_data_from_http_post(request, 'blog_address', self.context)
            blog_email = fetch_data_from_http_post(request, 'blog_email', self.context)
            blog_mobile_phone = fetch_data_from_http_post(request, 'blog_mobile_phone', self.context)
            blog_landline = fetch_data_from_http_post(request, 'blog_landline', self.context)
            blog_generated_url = fetch_data_from_http_post(request, 'blog_generated_url', self.context)
            blog_generated_url_id = fetch_data_from_http_post(request, 'blog_generated_url_id', self.context)
            blog_custom_url = fetch_data_from_http_post(request, 'blog_custom_url', self.context)
            blog_theme = fetch_data_from_http_post(request, 'blog_theme', self.context)

            if not blog_name:
                self.context['alert'] = 'نام بلاگ بدرستی وارد نشده است'
                return render(request, 'blog-admin/blog-new.html', self.context)

            try:
                new_blog = Blog(
                    title=blog_name,
                    description=blog_description,
                    keywords=blog_keywords,
                    address=blog_address,
                    email=blog_email,
                    mobile_phone=blog_mobile_phone,
                    landline=blog_landline,
                    generated_url=blog_generated_url,
                    generated_url_id=blog_generated_url_id,
                    custom_url=blog_custom_url,
                    theme=blog_theme,
                    created_at=jdatetime.datetime.now(),
                    created_by=request.user,
                )
                new_blog.save()
            except Exception as e:
                self.context['alert'] = str(e)
                return render(request, 'blog-admin/blog-new.html', self.context)

            return redirect('blog:blog-list')
        else:
            return redirect('accounts:login')


class BlogEdit(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.context = {'page_title': 'ویرایش بلاگ',
                        'navigation_icon_menu_id': 'service',
                        'navigation_menu_body_id': 'navigationService',
                        'navigation_menu_body_sub_item_id': 'blog-list',
                        'breadcrumb_1': 'خانه',
                        'breadcrumb_2': 'بلاگ',
                        'breadcrumb_3': 'ویرایش بلاگ',
                        }

    def get(self, request, blog_id, *args, **kwargs):
        if request.user.is_authenticated:
            if not has_user_active_licence(request, 'blog_licence'):
                return redirect('subscription:change-vip-plan')

            try:
                blog = Blog.objects.get(id=blog_id, created_by=request.user)
                self.context['blog'] = blog
            except:
                return redirect('blog:blog-list')
            return render(request, 'blog-admin/blog-edit.html', self.context)
        else:
            return redirect('accounts:login')

    def post(self, request, blog_id, *args, **kwargs):
        if request.user.is_authenticated:
            if not has_user_active_licence(request, 'blog_licence'):
                return redirect('subscription:change-vip-plan')

            try:
                blog = Blog.objects.get(id=blog_id, created_by=request.user)
                self.context['blog'] = blog
            except:
                return redirect('blog:blog-list')
            blog_name = fetch_data_from_http_post(request, 'blog_name', self.context)
            blog_description = fetch_data_from_http_post(request, 'blog_description', self.context)
            blog_keywords = fetch_data_from_http_post(request, 'blog_keywords', self.context)
            blog_address = fetch_data_from_http_post(request, 'blog_address', self.context)
            blog_email = fetch_data_from_http_post(request, 'blog_email', self.context)
            blog_mobile_phone = fetch_data_from_http_post(request, 'blog_mobile_phone', self.context)
            blog_landline = fetch_data_from_http_post(request, 'blog_landline', self.context)
            blog_generated_url = fetch_data_from_http_post(request, 'blog_generated_url', self.context)
            blog_generated_url_id = fetch_data_from_http_post(request, 'blog_generated_url_id', self.context)
            blog_custom_url = fetch_data_from_http_post(request, 'blog_custom_url', self.context)
            blog_theme = fetch_data_from_http_post(request, 'blog_theme', self.context)

            if not blog_name:
                self.context['alert'] = 'نام بلاگ بدرستی وارد نشده است'
                return render(request, 'blog-admin/blog-edit.html', self.context)

            blog.title = blog_name
            blog.description = blog_description
            blog.keywords = blog_keywords
            blog.address = blog_address
            blog.email = blog_email
            blog.mobile_phone = blog_mobile_phone
            blog.landline = blog_landline
            blog.custom_url = blog_custom_url
            blog.theme = blog_theme
            blog.save()
            return redirect('blog:blog-edit-with-blog-id', blog_id=blog_id)
        else:
            return redirect('accounts:login')


class BlogRemove(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get(self, request, blog_id, *args, **kwargs):
        return render(request, '404.html')

    def post(self, request, blog_id, *args, **kwargs):
        if request.user.is_authenticated:
            if not has_user_active_licence(request, 'blog_licence'):
                return redirect('subscription:change-vip-plan')

            if request.method == 'POST':
                try:
                    blog = Blog.objects.get(id=blog_id, created_by=request.user)
                    blog.delete()
                except Exception as e:
                    print(str(e))
                    return HttpResponse(str(e))
            else:
                pass
            return redirect('blog:blog-list')
        else:
            return redirect('accounts:login')


class BlogList(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.context = {'page_title': 'لیست بلاگ ها',
                        'navigation_icon_menu_id': 'service',
                        'navigation_menu_body_id': 'navigationService',
                        'navigation_menu_body_sub_item_id': 'blog-list',
                        'breadcrumb_1': 'خانه',
                        'breadcrumb_2': 'لیست بلاگ ها',
                        }

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if not has_user_active_licence(request, 'blog_licence'):
                return redirect('subscription:change-vip-plan')

            blogs = Blog.objects.filter(created_by=request.user)
            self.context['blogs'] = blogs
            return render(request, 'blog-admin/blog-list.html', self.context)
        else:
            return redirect('accounts:login')

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('blog:blog-list')
        else:
            return redirect('accounts:login')


class BlogPostNew(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.context = {'page_title': 'پست بلاگ جدید',
                        'navigation_icon_menu_id': 'service',
                        'navigation_menu_body_id': 'navigationService',
                        'navigation_menu_body_sub_item_id': 'blog-post-new',
                        }

    def get(self, request, blog_id, *args, **kwargs):
        if request.user.is_authenticated:
            if not has_user_active_licence(request, 'blog_licence'):
                return redirect('subscription:change-vip-plan')

            try:
                blog = Blog.objects.get(id=blog_id, created_by=request.user)
                self.context['blog'] = blog
            except:
                return render(request, '404.html')
            categories = MagicWord.objects.filter(word_type='category')
            self.context['categories'] = categories
            my_bots = Bot.objects.filter(created_by=request.user)
            self.context['my_bots'] = my_bots
            return render(request, 'blog/blog-post-new.html', self.context)
        else:
            return redirect('accounts:login')

    def post(self, request, blog_id, *args, **kwargs):
        if request.user.is_authenticated:
            if not has_user_active_licence(request, 'blog_licence'):
                return redirect('subscription:change-vip-plan')

            try:
                blog = Blog.objects.get(id=blog_id, created_by=request.user)
                self.context['blog'] = blog
            except:
                return render(request, '404.html')
            categories = MagicWord.objects.filter(word_type='category')
            self.context['categories'] = categories
            my_bots = Bot.objects.filter(created_by=request.user)
            self.context['my_bots'] = my_bots
            blog_post_title = fetch_data_from_http_post(request, 'blog_post_title', self.context)
            blog_post_description = fetch_data_from_http_post(request, 'blog_post_description', self.context)
            blog_post_categories = fetch_datalist_from_http_post(request, 'blog_post_categories', self.context)
            blog_post_keywords = fetch_data_from_http_post(request, 'blog_post_keywords', self.context)
            blog_feature_image = fetch_single_file_from_http_file(request, 'blog_feature_image', self.context)
            blog_post_content = fetch_data_from_http_post(request, 'blog_post_content', self.context)

            if blog_post_title is None:
                self.context['alert'] = 'عنوان پست بدرستی وارد نشده است'
                self.context['toast'] = 'عنوان پست بدرستی وارد نشده است'
                return render(request, 'blog/blog-post-new.html', self.context)
            if blog_post_description is None:
                self.context['alert'] = 'توضیحات مختصر بدرستی وارد نشده است'
                self.context['toast'] = 'توضیحات مختصر بدرستی وارد نشده است'
                return render(request, 'blog/blog-post-new.html', self.context)
            categories_list = []
            if blog_post_categories is not None:
                for category in blog_post_categories:
                    try:
                        category = MagicWord.objects.get(id=int(category))
                    except:
                        try:
                            category = MagicWord.objects.get(title='uncategorized')
                        except:
                            category = MagicWord(
                                title='uncategorized',
                                word_type='category',
                            )
                            category.save()
                    categories_list.append(category)
            keywords_list = []
            if blog_post_keywords is not None:
                blog_post_keywords = str(blog_post_keywords).replace('،', ',').split(',')
                for blog_post_keyword in blog_post_keywords:
                    if blog_post_keyword == '':
                        continue
                    elif blog_post_keyword is None:
                        continue
                    else:
                        try:
                            keyword = MagicWord.objects.get(word_type='keyword',
                                                            slug_title=name_to_url(blog_post_keyword))
                        except:
                            keyword = MagicWord(
                                title=blog_post_keyword,
                                word_type='keyword',
                            )
                            keyword.save()
                        keywords_list.append(keyword)
            if blog_post_content is None:
                self.context['alert'] = 'محتوای پست بدرستی وارد نشده است'
                self.context['toast'] = 'محتوای پست بدرستی وارد نشده است'
                return render(request, 'blog/blog-post-new.html', self.context)
            try:
                new_blog_post = BlogPost(
                    blog=blog,
                    title=blog_post_title,
                    feature_image=blog_feature_image,
                    description=blog_post_description,
                    content=blog_post_content,
                    created_by=request.user,
                    updated_by=request.user,
                )
                new_blog_post.save()
            except Exception as e:
                self.context['alert'] = f'هنگام ذخیره پست ارور زیر رخ داد: ' + str(e)
                self.context['toast'] = f'هنگام ذخیره پست ارور زیر رخ داد: ' + str(e)
                return render(request, 'blog/blog-post-new.html', self.context)
            if len(categories_list) != 0:
                for category_item in categories_list:
                    new_blog_post.categories.add(category_item)
                    new_blog_post.save()
            if len(keywords_list) != 0:
                for keyword_item in keywords_list:
                    new_blog_post.keywords.add(keyword_item)
                    new_blog_post.save()
            new_blog_post.save()
            return redirect('blog:blog-post-detail-with-id', blog_post_id=new_blog_post.id)
        else:
            return redirect('accounts:login')


class BlogPostEdit(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.context = {'page_title': 'ویرایش پست بلاگ',
                        'navigation_icon_menu_id': 'service',
                        'navigation_menu_body_id': 'navigationService',
                        'navigation_menu_body_main_item_id': 'blog-post',
                        }

    def get(self, request, blog_post_id, *args, **kwargs):
        if request.user.is_authenticated:
            if not has_user_active_licence(request, 'blog_licence'):
                return redirect('subscription:change-vip-plan')

            try:
                blog_post = BlogPost.objects.get(id=blog_post_id, created_by=request.user)
                self.context['blog_post'] = blog_post
            except:
                return redirect('blog:my-blog-post-list')
            categories = MagicWord.objects.filter(word_type='category')
            self.context['categories'] = categories
            my_bots = Bot.objects.filter(created_by=request.user)
            self.context['my_bots'] = my_bots
            return render(request, 'blog/blog-post-edit.html', self.context)
        else:
            return redirect('accounts:login')

    def post(self, request, blog_post_id, *args, **kwargs):
        if request.user.is_authenticated:
            if not has_user_active_licence(request, 'blog_licence'):
                return redirect('subscription:change-vip-plan')

            categories = MagicWord.objects.filter(word_type='category')
            self.context['categories'] = categories
            my_bots = Bot.objects.filter(created_by=request.user)
            self.context['my_bots'] = my_bots
            try:
                blog_post_title = request.POST['blog-post-title']
                if blog_post_title == '':
                    blog_post_title = None
            except:
                blog_post_title = None
            if blog_post_title is None:
                self.context['alert'] = 'عنوان پست بدرستی وارد نشده است'
                self.context['toast'] = 'عنوان پست بدرستی وارد نشده است'
                return render(request, 'blog/blog-post-edit.html', self.context)
            try:
                blog_post_description = request.POST['blog-post-description']
                if blog_post_description == '':
                    blog_post_description = None
            except:
                blog_post_description = None
            if blog_post_description is None:
                self.context['alert'] = 'توضیحات مختصر بدرستی وارد نشده است'
                self.context['toast'] = 'توضیحات مختصر بدرستی وارد نشده است'
                return render(request, 'blog/blog-post-edit.html', self.context)
            categories_list = []
            try:
                blog_post_categories = request.POST.getlist('blog-post-categories')
                if blog_post_categories == '':
                    blog_post_categories = None
                else:
                    for category in blog_post_categories:
                        try:
                            category = MagicWord.objects.get(id=int(category))
                        except:
                            try:
                                category = MagicWord.objects.get(title='uncategorized')
                            except:
                                category = MagicWord(
                                    title='uncategorized',
                                    word_type='category',
                                )
                                category.save()
                        categories_list.append(category)
            except:
                blog_post_categories = None
            keywords_list = []
            try:
                blog_post_keywords = request.POST['blog-post-keywords']
                if blog_post_keywords == '':
                    blog_post_keywords = None
                else:
                    blog_post_keywords = str(blog_post_keywords).split(',')
                    for blog_post_keyword in blog_post_keywords:
                        try:
                            keyword = MagicWord.objects.get(word_type='keyword',
                                                            slug_title=name_to_url(blog_post_keyword))
                        except:
                            keyword = MagicWord(
                                title=blog_post_keyword,
                                word_type='keyword',
                            )
                            keyword.save()
                        keywords_list.append(keyword)
            except:
                blog_post_keywords = None
            try:
                blog_feature_image = request.FILES['blog-feature-image']
                if blog_feature_image == '':
                    blog_feature_image = None
            except:
                blog_feature_image = None
            try:
                blog_post_content = request.POST['blog-post-content']
                if blog_post_content == '':
                    blog_post_content = None
            except:
                blog_post_content = None
            if blog_post_content is None:
                self.context['alert'] = 'محتوای پست بدرستی وارد نشده است'
                self.context['toast'] = 'محتوای پست بدرستی وارد نشده است'
                return render(request, 'blog/blog-post-edit.html', self.context)
            blog_post = BlogPost.objects.get(id=blog_post_id, created_by=request.user)
            blog_post.title = blog_post_title
            if blog_feature_image:
                blog_post.feature_image = blog_feature_image
            blog_post.description = blog_post_description
            blog_post.content = blog_post_content
            blog_post.created_by = request.user
            blog_post.updated_by = request.user
            blog_post.save()
            for category_item in categories_list:
                blog_post.categories.add(category_item)
                blog_post.save()
            for keyword_item in keywords_list:
                blog_post.keywords.add(keyword_item)
                blog_post.save()
            return redirect('blog:blog-post-detail-with-id', blog_post_id=blog_post.id)
        else:
            return redirect('accounts:login')


class BlogPostRemove(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get(self, request, blog_post_id, *args, **kwargs):
        return render(request, '404.html')

    def post(self, request, blog_post_id, *args, **kwargs):
        if request.user.is_authenticated:
            if not has_user_active_licence(request, 'blog_licence'):
                return redirect('subscription:change-vip-plan')

            if request.method == 'POST':
                try:
                    post = BlogPost.objects.get(id=blog_post_id, created_by=request.user)
                    post.delete()
                except Exception as e:
                    print(str(e))
            else:
                pass
            return redirect('blog:my-blog-post-list')
        else:
            return redirect('accounts:login')


class BlogPostList(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.context = {'navigation_icon_menu_id': 'service',
                        'navigation_menu_body_id': 'navigationService',
                        'navigation_menu_body_sub_item_id': 'my-blog-post-list',
                        }

    def get(self, request, blog_id, *args, **kwargs):
        if request.user.is_authenticated:
            if not has_user_active_licence(request, 'blog_licence'):
                return redirect('subscription:change-vip-plan')

            try:
                blog = Blog.objects.get(id=blog_id, created_by=request.user)
                self.context['blog'] = blog
                self.context['page_title'] = f'پست های بلاگ {blog.title}'
            except:
                return render(request, '404.html')

            my_blog_posts = BlogPost.objects.filter(created_by=request.user)
            self.context['blog_posts'] = my_blog_posts
            return render(request, 'blog/my-blog-post-list.html', self.context)
        else:
            return redirect('accounts:login')

    def post(self, request, blog_id, *args, **kwargs):
        if request.user.is_authenticated:
            if not has_user_active_licence(request, 'blog_licence'):
                return redirect('subscription:change-vip-plan')

            try:
                blog = Blog.objects.get(id=blog_id, created_by=request.user)
                self.context['blog'] = blog
            except:
                return render(request, '404.html')
            return render(request, 'blog/my-blog-post-list.html', self.context)
        else:
            return redirect('accounts:login')


# --------------- admin panel ------------------------


# --------------- front ------------------------
class BlogFrontHome(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.context = {}

    def get(self, request, *args, **kwargs):
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

    def post(self, request, *args, **kwargs):
        return render(request, '404.html')


class BlogFrontPostList(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.context = {'navigation_icon_menu_id': 'service',
                        'navigation_menu_body_id': 'navigationService',
                        'navigation_menu_body_sub_item_id': 'my-blog-post-list',
                        }

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            try:
                blog_id = 1
                blog = Blog.objects.get(id=blog_id, created_by=request.user)
                self.context['blog'] = blog
                self.context['page_title'] = f'پست های بلاگ {blog.title}'
            except:
                return render(request, '404.html')

            my_blog_posts = BlogPost.objects.filter(created_by=request.user)
            self.context['blog_posts'] = my_blog_posts
            return render(request, 'blog/my-blog-post-list.html', self.context)
        else:
            return redirect('accounts:login')

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            try:
                blog_id = 1
                blog = Blog.objects.get(id=blog_id, created_by=request.user)
                self.context['blog'] = blog
            except:
                return render(request, '404.html')
            return render(request, 'blog/my-blog-post-list.html', self.context)
        else:
            return redirect('accounts:login')


class BlogFrontPostDetail(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.context = {}

    def get(self, request, blog_post_id, *args, **kwargs):
        try:
            blog_post = BlogPost.objects.get(id=blog_post_id)
            self.context['page_title'] = blog_post.title
            self.context['post_content'] = blog_post

            blog_post_comments = BlogPostReply.objects.filter(blog_post=blog_post_id)
            self.context['blog_post_comments'] = blog_post_comments
        except:
            return render(request, '404.html')
        BlogPostViewCounterThread(post=blog_post, published_on='panel').start()
        return render_with_desired_theme(request, 'blog-post-detail.html', self.context, blog_post.blog)

    def post(self, request, blog_post_id, *args, **kwargs):
        if request.user.is_authenticated:
            try:
                comment = request.POST['comment']
                if comment == '':
                    comment = None
            except:
                comment = None
            if comment is None:
                return redirect('blog:blog-post-detail-with-id', blog_post_id=blog_post_id)
            try:
                blog_post = BlogPost.objects.get(id=blog_post_id)
                self.context['page_title'] = blog_post.title
                self.context['post_content'] = blog_post

                new_comment = BlogPostReply(
                    blog_post=blog_post,
                    replier=request.user,
                    comment=comment,
                )
                new_comment.save()
                blog_post_comments = BlogPostReply.objects.filter(blog_post=blog_post_id)
                self.context['blog_post_comments'] = blog_post_comments
                self.context['message'] = 'نظر شما ثبت شد و پس از تایید مدیریت نمایش داده خواهد شد'
                return render_with_desired_theme(request, 'blog-post-detail.html', self.context, blog_post.blog)
            except:
                return redirect('blog:blog-post-detail-with-id', blog_post_id=blog_post_id)
        else:
            return redirect('accounts:login')


class BlogFrontContactUs(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.context = {}

    def get(self, request, *args, **kwargs):
        try:
            requested_url = request.META['HTTP_HOST']
            try:
                blog = Blog.objects.get(generated_url=requested_url)
            except:
                try:
                    blog = Blog.objects.get(custom_url=requested_url)
                except:
                    return render(request, '404.html')
            self.context['blog'] = blog
            return render_with_desired_theme(request, 'index.html', self.context, blog)
        except:
            return render(request, '404.html')

    def post(self, request, *args, **kwargs):
        return render(request, '404.html')


class BlogFrontAboutUs(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.context = {}

    def get(self, request, *args, **kwargs):
        try:
            requested_url = request.META['HTTP_HOST']
            try:
                blog = Blog.objects.get(generated_url=requested_url)
            except:
                try:
                    blog = Blog.objects.get(custom_url=requested_url)
                except:
                    return render(request, '404.html')
            self.context['blog'] = blog
            return render_with_desired_theme(request, 'index.html', self.context, blog)
        except:
            return render(request, '404.html')

    def post(self, request, *args, **kwargs):
        return render(request, '404.html')


# --------------- front ------------------------

# def post_list_view(request):
#     context = {'page_title': 'اخبار - نمای جوانی',
#                'page_type': 'article',
#                'tab_index': '2'}
#     page_number = request.GET.get('page')
#     header_tab_word = HeaderTabWord.objects.all()
#
#     blog_post_list = []
#     blog_posts = BlogPost.objects.filter(post_publish_status='1', publish_on_namayejavani=True)
#     paginator = Paginator(blog_posts, 10)
#     try:
#         page_obj = paginator.get_page(page_number)
#     except PageNotAnInteger:
#         page_obj = paginator.page(1)
#     except EmptyPage:
#         page_obj = paginator.page(paginator.num_pages)
#     blog_post_list.append(['همه', page_obj])
#     for tab in header_tab_word[0].tab_word.all():
#         blog_posts = BlogPost.objects.filter(post_publish_status='1', publish_on_namayejavani=True,
#                                              categories__in=[tab])
#         paginator = Paginator(blog_posts, 10)
#         try:
#             page_obj = paginator.get_page(page_number)
#         except PageNotAnInteger:
#             page_obj = paginator.page(1)
#         except EmptyPage:
#             page_obj = paginator.page(paginator.num_pages)
#         blog_post_list.append([tab.title, page_obj])
#
#     context['blog_post_list'] = blog_post_list
#
#     featured_posts = FeaturePost.objects.filter(post__publish_on_namayejavani=True)[:10]
#     context['featured_posts'] = featured_posts
#
#     most_viewed_posts = BlogPostProfile.objects.filter(post__publish_on_namayejavani=True).order_by('view_count')[:10]
#     context['most_viewed_posts'] = most_viewed_posts
#     return render(request, 'blog_namayejavani/post-list.html', context)
#
#


class BlogStaticSitemap(Sitemap):
    priority = 0.5
    changefreq = "monthly"

    def items(self):
        return ["home", "contact-us", "about-us"]

    def location(self, item):
        return reverse(item)


class BlogSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.5

    def items(self):
        return BlogPost.objects.filter()

    def lastmod(self, obj):
        return obj.updated_at


def render_with_desired_theme(request, html_name, context, blog):
    html_path = f'blog/{blog.theme}/{html_name}'
    try:
        return render(request, html_path, context)
    except Exception as e:
        return HttpResponse(f'render exception: {str(e)}')
