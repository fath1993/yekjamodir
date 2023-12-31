from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

app_name = 'yekjamodir'

urlpatterns = [
    # admin
    path('admin/', admin.site.urls),
    path('captcha/', include('captcha.urls')),

    # from library
    path('tinymce/', include('tinymce.urls')),
    path('robots.txt', include('robots.urls')),

    # app
    path('', include('dashboard.urls')),
    path('', include('website.urls')),
    path('accounts/', include('accounts.urls')),
    path('calendar-event/', include('calendar_event.urls')),
    path('file/', include('gallery.urls')),
    path('financial/', include('financial_accounting.urls')),
    path('documents/', include('documents.urls')),
    path('tasks/', include('task_manager.urls')),
    path('blog/', include('blog.urls')),
    path('auto-robots/', include('auto_robots.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
