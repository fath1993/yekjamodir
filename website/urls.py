from django.urls import path

from blog.views import BlogFrontPostList, BlogFrontContactUs, BlogFrontAboutUs, BlogFrontPostDetail

app_name = 'website'
urlpatterns = [
    # blog front
    path('blog-front-post-list/', BlogFrontPostList.as_view(), name='blog-front-post-list'),
    path('blog-front-contact-us/', BlogFrontContactUs.as_view(), name='blog-front-contact-us'),
    path('blog-front-about-us/', BlogFrontAboutUs.as_view(), name='blog-front-about-us'),
    path('blog-front-post-detail&id=<int:blog_post_id>/', BlogFrontPostDetail.as_view(),
         name='blog-front-post-detail-with-post-id'),
]
