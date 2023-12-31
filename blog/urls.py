from django.urls import path, include

from blog.views import BlogPostNew, BlogPostEdit, BlogPostList, \
    BlogPostRemove, BlogList, BlogNew, BlogEdit, BlogRemove

app_name = 'blog'

urlpatterns = [
    # blog admin
    path('blog-new/', BlogNew.as_view(), name='blog-new'),
    path('blog-edit&id=<int:blog_id>/', BlogEdit.as_view(), name='blog-edit-with-blog-id'),
    path('blog-remove&id=<int:blog_id>/', BlogRemove.as_view(), name='blog-remove-with-blog-id'),
    path('blog-list/', BlogList.as_view(), name='blog-list'),

    # blog post admin
    path('blog-post-new&id=<int:blog_id>/', BlogPostNew.as_view(), name='blog-post-new-with-blog-id'),
    path('blog-post-edit&id=<int:blog_post_id>/', BlogPostEdit.as_view(), name='blog-post-edit-with-post-id'),
    path('blog-post-remove&id=<int:blog_post_id>/', BlogPostRemove.as_view(), name='blog-post-remove-with-post-id'),
    path('blog-post-list&id=<int:blog_id>/', BlogPostList.as_view(), name='blog-post-list-with-blog-id'),

    # path('blog-post-list&category-id=<int:category_id>&category-title=<str:category_title>/', BlogPostList.as_view(), name='blog-post-list-with-category-id-and-category-title'),
    # path('blog-post-list&keyword-id=<int:keyword_id>&keyword-title=<str:keyword_title>/', BlogPostList.as_view(), name='blog-post-list-with-keyword-id-and-keyword-title'),
]

