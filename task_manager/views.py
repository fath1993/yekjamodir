import jdatetime
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from accounts.models import Profile
from task_manager.models import Task
from task_manager.utils import datetime_to_number, day_calculator
from utilities.http_metod import fetch_data_from_http_post


def task_new_view(request):
    context = {'page_title': 'ثبت وظیفه',
               'navigation_icon_menu_id': 'service',
               'navigation_menu_body_id': 'navigationService',
               'navigation_menu_body_sub_item_id': 'task-new',
               }
    if request.user.is_authenticated:
        directors = Profile.objects.filter(is_employee=True)
        context['directors'] = directors
        if request.method == 'POST':
            director_id = fetch_data_from_http_post(request, 'director', context)
            activity_title = fetch_data_from_http_post(request, 'activity-title', context)
            prediction_progress_start_date = fetch_data_from_http_post(request, 'prediction-progress-start-date',
                                                                       context)
            prediction_progress_end_date = fetch_data_from_http_post(request, 'prediction-progress-end-date', context)
            real_progress_start_date = fetch_data_from_http_post(request, 'real-progress-start-date',
                                                                 context)
            real_progress_end_date = fetch_data_from_http_post(request, 'real-progress-end-date', context)
            activity_completion_percentage = fetch_data_from_http_post(request, 'activity-completion-percentage',
                                                                       context)
            if not director_id:
                context['alert'] = 'مجری بدرستی وارد نشده است'
                return render(request, 'tasks/task-new.html', context)
            try:
                director = User.objects.get(id=director_id)
            except:
                context['alert'] = 'مجری بدرستی وارد نشده است'
                return render(request, 'tasks/task-new.html', context)
            if not activity_title:
                context['alert'] = 'عنوان فعالیت بدرستی وارد نشده است'
                return render(request, 'tasks/task-new.html', context)
            if not prediction_progress_start_date:
                context['alert'] = 'تاریخ شروع پیش بینی وارد نشده است'
                return render(request, 'tasks/task-new.html', context)
            if not prediction_progress_end_date:
                context['alert'] = 'تاریخ پایان پیش بینی وارد نشده است'
                return render(request, 'tasks/task-new.html', context)

            if activity_completion_percentage == '':
                activity_completion_percentage = 0
            if real_progress_start_date == '':
                real_progress_start_date = None
            if real_progress_end_date == '':
                real_progress_end_date = None
            new_task = Task.objects.create(director=director, activity=activity_title,
                                           prediction_progress_start_date=str_date_to_datetime(prediction_progress_start_date),
                                           prediction_progress_end_date=str_date_to_datetime(prediction_progress_end_date),
                                           real_progress_start_date=str_date_to_datetime(real_progress_start_date),
                                           real_progress_end_date=str_date_to_datetime(real_progress_end_date),
                                           activity_completion_percentage=activity_completion_percentage,
                                           created_by=request.user)
            return redirect(reverse('tasks:task-detail-with-id', kwargs={'task_id': new_task.id}))
        return render(request, 'tasks/task-new.html', context)
    else:
        return redirect('accounts:login')


def str_date_to_datetime(str_date):
    if str_date is None:
        return None
    else:
        date = str(str_date).split('/')
        date = jdatetime.datetime(year=int(date[0]), month=int(date[1]), day=int(date[2]))
        return date


def my_task_list_table_view(request):
    context = {'page_title': 'وظایف ثبت شده من - لیست',
               'navigation_icon_menu_id': 'service',
               'navigation_menu_body_id': 'navigationService',
               'navigation_menu_body_sub_item_id': 'task-list-table',
               }
    if request.user.is_authenticated:
        tasks = Task.objects.filter(created_by=request.user)
        context['tasks'] = tasks
        if request.method == 'POST':
            pass
        return render(request, 'tasks/task-list-table.html', context)
    else:
        return redirect('accounts:login')


def my_task_list_chart_view(request):
    context = {'page_title': 'وظایف ثبت شده من - چارت',
               'navigation_icon_menu_id': 'service',
               'navigation_menu_body_id': 'navigationService',
               'navigation_menu_body_sub_item_id': 'task-list-chart',
               }
    if request.user.is_authenticated:
        tasks = Task.objects.filter(created_by=request.user)
        task_list = []
        for task in tasks:
            p1 = task.prediction_progress_start_date
            p2 = task.prediction_progress_end_date
            r1 = task.real_progress_start_date
            r2 = task.real_progress_end_date
            state = None
            box_1 = None
            box_2 = None
            box_3 = None
            box_4 = None
            box_5 = None
            box_6 = None
            if r1 is not None and r2 is not None:
                if p1 == r1 and p2 > r2:
                    state = 1
                    box_1 = day_calculator(p1)
                    box_2 = day_calculator(r2)
                    box_3 = box_2 + 1
                    box_4 = day_calculator(p2)
                    box_5 = None
                    box_6 = None
                if p1 == r1 and p2 == r2:
                    state = 2
                    box_1 = day_calculator(p1)
                    box_2 = day_calculator(p2)
                    box_3 = None
                    box_4 = None
                    box_5 = None
                    box_6 = None
                if p1 == r1 and p2 < r2:
                    state = 3
                    box_1 = day_calculator(p1)
                    box_2 = day_calculator(p2)
                    box_3 = box_2 + 1
                    box_4 = day_calculator(r2)
                    box_5 = None
                    box_6 = None
                if p1 < r1 and p2 > r2:
                    state = 4
                    box_1 = day_calculator(p1)
                    box_2 = day_calculator(r1) - 1
                    box_3 = day_calculator(r1)
                    box_4 = day_calculator(r2)
                    box_5 = box_4 + 1
                    box_6 = day_calculator(p2)
                if p1 < r1 and p2 == r2:
                    state = 5
                    box_1 = day_calculator(p1)
                    box_2 = day_calculator(r1) - 1
                    box_3 = day_calculator(r1)
                    box_4 = day_calculator(r2)
                    box_5 = None
                    box_6 = None
                if p1 < r1 and p2 < r2 and p2 > r1:
                    state = 6
                    box_1 = day_calculator(p1)
                    box_2 = day_calculator(r1) - 1
                    box_3 = day_calculator(r1)
                    box_4 = day_calculator(p2)
                    box_5 = box_4 + 1
                    box_6 = day_calculator(r2)
                if p1 < r1 and p2 < r2 and p2 == r1:
                    state = 7
                    box_1 = day_calculator(p1)
                    box_2 = day_calculator(r1) - 1
                    box_3 = day_calculator(r1)
                    box_4 = day_calculator(r1) + 1
                    box_5 = day_calculator(r2)
                    box_6 = None
                if p1 < r1 and p2 < r2 and p2 < r1:
                    state = 8
                    box_1 = day_calculator(p1)
                    box_2 = day_calculator(p2)
                    box_3 = box_2 + 1
                    box_4 = day_calculator(r1) - 1
                    box_5 = day_calculator(r1)
                    box_6 = day_calculator(r2)
            else:
                state = 9
                box_1 = day_calculator(p1)
                box_2 = day_calculator(p2)
                box_3 = None
                box_4 = None
                box_5 = None
                box_6 = None
            task_list.append([task, state, [box_1, box_2, box_3, box_4, box_5, box_6]])

        context['task_list'] = task_list
        context['num_boxes'] = range(1, 366)
        if request.method == 'POST':
            pass
        return render(request, 'tasks/task-list-chart.html', context)
    else:
        return redirect('accounts:login')


def task_detail_view(request, task_id):
    if request.user.is_authenticated:
        task = Task.objects.get(id=task_id, created_by=request.user)
        context = {'page_title': f'جزئیات وظیفه - {task.activity}', 'navigation_icon_menu_id': 'service',
                   'navigation_menu_body_id': 'navigationService',
                   'navigation_menu_body_main_item_id': 'tasks', 'task': task}
        if request.method == 'POST':
            pass
        return render(request, 'tasks/task-detail.html', context)
    else:
        return redirect('accounts:login')


def task_edit_view(request, task_id):
    if request.user.is_authenticated:
        task = Task.objects.get(id=task_id, created_by=request.user)
        directors = Profile.objects.filter(is_employee=True)
        context = {'page_title': f' وظیفه - {task.activity}', 'navigation_icon_menu_id': 'service',
                   'navigation_menu_body_id': 'navigationService', 'navigation_menu_body_main_item_id': 'tasks',
                   'task': task, 'directors': directors}
        if request.method == 'POST':
            director_id = fetch_data_from_http_post(request, 'director', context)
            activity_title = fetch_data_from_http_post(request, 'activity-title', context)
            prediction_progress_start_date = fetch_data_from_http_post(request, 'prediction-progress-start-date',
                                                                       context)
            prediction_progress_end_date = fetch_data_from_http_post(request, 'prediction-progress-end-date', context)
            real_progress_start_date = fetch_data_from_http_post(request, 'real-progress-start-date',
                                                                 context)
            real_progress_end_date = fetch_data_from_http_post(request, 'real-progress-end-date', context)
            activity_completion_percentage = fetch_data_from_http_post(request, 'activity-completion-percentage',
                                                                       context)
            if not director_id:
                context['alert'] = 'مجری بدرستی وارد نشده است'
                return render(request, 'tasks/task-edit.html', context)
            try:
                director = User.objects.get(id=director_id)
            except Exception as e:
                print(str(e))
                context['alert'] = 'مجری بدرستی وارد نشده است'
                return render(request, 'tasks/task-edit.html', context)
            if not activity_title:
                context['alert'] = 'عنوان فعالیت بدرستی وارد نشده است'
                return render(request, 'tasks/task-edit.html', context)
            if not prediction_progress_start_date:
                context['alert'] = 'تاریخ شروع پیش بینی وارد نشده است'
                return render(request, 'tasks/task-edit.html', context)
            if not prediction_progress_end_date:
                context['alert'] = 'تاریخ پایان پیش بینی وارد نشده است'
                return render(request, 'tasks/task-edit.html', context)

            try:
                task = Task.objects.get(id=task_id, created_by=request.user)
            except:
                context['alert'] = 'فعالیت یافت نشد'
                return render(request, 'tasks/task-edit.html', context)
            task.director = director
            task.activity = activity_title
            task.prediction_progress_start_date = str_date_to_datetime(prediction_progress_start_date)
            task.prediction_progress_end_date = str_date_to_datetime(prediction_progress_end_date)
            task.real_progress_start_date = str_date_to_datetime(real_progress_start_date)
            task.real_progress_end_date = str_date_to_datetime(real_progress_end_date)
            task.activity_completion_percentage = activity_completion_percentage
            task.save()
            return redirect(reverse('tasks:task-detail-with-id', kwargs={'task_id': task.id}))
        return render(request, 'tasks/task-edit.html', context)
    else:
        return redirect('accounts:login')


def task_remove_view(request, task_id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            try:
                task = Task.objects.get(id=task_id, created_by=request.user)
                task.delete()
            except:
                pass
        else:
            pass
        return redirect('tasks:my-task-list-table')
    else:
        return redirect('accounts:login')
