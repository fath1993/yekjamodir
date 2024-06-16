from django.urls import path, include

from gallery.views import ajax_file_remove, FilesList, upload_files_view, upload_permission_view, \
    ajax_user_storage_analyzer, FileGalleryView

app_name = 'file-gallery'

urlpatterns = [
    path('files-list/', FilesList.as_view(), name='files-list'),
    path('upload-files/', upload_files_view, name='upload-files'),
    path('upload-permission/', upload_permission_view, name='upload-permission'),
    path('ajax-file-remove/', ajax_file_remove, name='ajax-file-remove'),
    path('ajax-user-storage-analyzer/', ajax_user_storage_analyzer, name='ajax-user-storage-analyzer'),
    path('file/delete-file/', FileGalleryView().delete_file, name='delete-file'),
]
