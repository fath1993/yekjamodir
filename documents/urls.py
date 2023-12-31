from django.urls import path, include

from documents.views import document_new, folder_new, folder_list, document_list, folder_delete, \
    document_delete, folder_edit, document_edit, document_edit_history_list, ajax_file_delete

app_name = 'documents'

urlpatterns = [
    path('folder-new/', folder_new, name='folder-new'),
    path('folder-list/', folder_list, name='folder-list'),
    path('folder-edit&id=<int:folder_id>/', folder_edit, name='folder-edit'),
    path('folder-delete&id=<int:folder_id>/', folder_delete, name='folder-delete'),
    path('document-new/', document_new, name='document-new'),
    path('document-list/', document_list, name='document-list'),
    path('document-edit-history-list&id=<int:document_id>/', document_edit_history_list, name='document-edit-history-list'),
    path('document-edit&id=<int:document_id>/', document_edit, name='document-edit'),
    path('document-delete&id=<int:document_id>/', document_delete, name='document-delete'),
    path('ajax-file-delete/', ajax_file_delete, name='ajax-file-delete'),



]

