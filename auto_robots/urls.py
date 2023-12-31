from django.urls import path, include

from auto_robots.tasks import StartTaskView
from auto_robots.views import AutoRobotNew, AutoRobotList, AutoRobotEdit, gap_new_message_view, \
    AutoRobotRemove, MetaPostNew, MetaPostList, MetaPostEdit, MetaPostRemoveSingle, MetaPostRemoveAllRelated

app_name = 'auto_robots'

urlpatterns = [
    # start tasks cron jobs
    path('start-tasks/', StartTaskView.as_view(), name='start-tasks'),


    # auto robot
    path('auto-robots-new/', AutoRobotNew.as_view(), name='auto-robots-new'),
    path('auto-robots-list/', AutoRobotList.as_view(), name='auto-robots-list'),
    path('auto-robots-edit&id=<int:auto_robot_id>/', AutoRobotEdit.as_view(), name='auto-robots-edit-with-id'),
    path('auto-robots-remove&id=<int:auto_robot_id>/', AutoRobotRemove.as_view(), name='auto-robots-remove-with-id'),

    # metapost
    path('metapost-new/', MetaPostNew.as_view(), name='metapost-new'),
    path('metapost-list&bot-id=<int:auto_robot_id>/', MetaPostList.as_view(), name='metapost-list-with-bot-id'),
    path('metapost-edit&id=<int:metapost_id>/', MetaPostEdit.as_view(), name='metapost-edit-with-metapost-id'),
    path('metapost-remove-single&id=<int:metapost_id>/', MetaPostRemoveSingle.as_view(), name='metapost-remove-single-with-id'),
    path('metapost-remove-all-related&id=<int:metapost_id>/', MetaPostRemoveAllRelated.as_view(), name='metapost-remove-all-related-with-id'),

    # Gap
    path('gap-new-message&bot-id=<int:bot_id>/', gap_new_message_view, name='gap-new-message-with-bot-id'),

]

