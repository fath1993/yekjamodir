from django.urls import path
from task_manager.views import task_new_view, my_task_list_table_view, my_task_list_chart_view, task_detail_view, \
    task_remove_view, task_edit_view

app_name = 'tasks'

urlpatterns = [
    path('task-new/', task_new_view, name='task-new'),
    path('my-task-list-table/', my_task_list_table_view, name='my-task-list-table'),
    path('my-task-list-chart/', my_task_list_chart_view, name='my-task-list-chart'),
    path('task-detail&id=<int:task_id>/', task_detail_view, name='task-detail-with-id'),
    path('task-remove&id=<int:task_id>/', task_remove_view, name='task-remove-with-id'),
    path('task-edit&id=<int:task_id>/', task_edit_view, name='task-edit-with-id'),
]

