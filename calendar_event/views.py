import json
import jdatetime
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View

from calendar_event.models import Event
from utilities.http_metod import fetch_data_from_http_post, fetch_datalist_from_http_post


class CalendarView(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.context = {'page_title': 'تقویم',
                        'navigation_icon_menu_id': 'service',
                        'navigation_menu_body_id': 'navigationService',
                        'navigation_menu_body_main_item_id': 'calender-event',
                        'navigation_menu_body_sub_item_id': 'event-manager',
                        'breadcrumb_1': 'خانه',
                        'breadcrumb_2': 'خدمات',
                        'breadcrumb_3': 'تقویم',
                        }

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:

            return render(request, 'calendar-event/calendar.html', self.context)
        else:
            return redirect('accounts:login')

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return render(request, '404.html')
        else:
            return redirect('accounts:login')


class NewEventView(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.context = {'page_title': 'رویداد جدید',
                        'navigation_icon_menu_id': 'service',
                        'navigation_menu_body_id': 'navigationService',
                        'navigation_menu_body_sub_item_id': 'new-event',
                        }

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return render(request, '404.html')
        else:
            return redirect('accounts:login')

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            event_title = fetch_data_from_http_post(request, 'event_title', self.context)
            event_start_date = fetch_data_from_http_post(request, 'event_start_date', self.context)
            event_start_time = fetch_data_from_http_post(request, 'event_start_time', self.context)
            event_end_date = fetch_data_from_http_post(request, 'event_end_date', self.context)
            event_end_time = fetch_data_from_http_post(request, 'event_end_time', self.context)
            publish_with_bots = fetch_datalist_from_http_post(request, 'publish_with_bots', self.context)
            event_remind_me_at_once = fetch_data_from_http_post(request, 'event_remind_me_at_once', self.context)
            event_remind_me_at_once_date = fetch_data_from_http_post(request, 'event_remind_me_at_once_date',
                                                                     self.context)
            event_remind_me_at_once_time = fetch_data_from_http_post(request, 'event_remind_me_at_once_time',
                                                                     self.context)
            event_hourly_remind_me_at = fetch_data_from_http_post(request, 'event_hourly_remind_me_at', self.context)
            event_hourly_remind_me_at_number = fetch_data_from_http_post(request, 'event_hourly_remind_me_at_number',
                                                                         self.context)
            event_daily_remind_me_at = fetch_data_from_http_post(request, 'event_daily_remind_me_at', self.context)
            event_daily_remind_me_at_time = fetch_data_from_http_post(request, 'event_daily_remind_me_at_time',
                                                                      self.context)
            event_monthly_remind_me_at = fetch_data_from_http_post(request, 'event_monthly_remind_me_at', self.context)
            event_monthly_remind_me_at_day = fetch_data_from_http_post(request, 'event_monthly_remind_me_at_day',
                                                                       self.context)
            event_monthly_remind_me_at_time = fetch_data_from_http_post(request, 'event_monthly_remind_me_at_time',
                                                                        self.context)
            event_yearly_remind_me_at = fetch_data_from_http_post(request, 'event_yearly_remind_me_at', self.context)
            event_yearly_remind_me_at_month = fetch_data_from_http_post(request, 'event_yearly_remind_me_at_month',
                                                                        self.context)
            event_yearly_remind_me_at_day = fetch_data_from_http_post(request, 'event_yearly_remind_me_at_day',
                                                                      self.context)
            event_yearly_remind_me_at_time = fetch_data_from_http_post(request, 'event_yearly_remind_me_at_time',
                                                                       self.context)
            event_description = fetch_data_from_http_post(request, 'event_description', self.context)

            if not event_title:
                return JsonResponse({'message': 'عنوان وارد نشده است'})
            if not event_start_time:
                event_start_time = '00:00'
            if not event_end_time:
                event_end_time = '00:00'
            if event_remind_me_at_once:
                if not event_remind_me_at_once_date:
                    return JsonResponse({'message': 'تاریخ وارد نشده است'})
                if not event_remind_me_at_once_time:
                    return JsonResponse({'message': 'زمان وارد نشده است'})
            if event_hourly_remind_me_at:
                if not event_hourly_remind_me_at_number:
                    return JsonResponse({'message': 'دقیقه یاداوری وارد نشده است'})
                try:
                    event_hourly_remind_me_at_number = int(event_hourly_remind_me_at_number)
                except:
                    return JsonResponse({'message': 'دقیقه یاداوری بدرستی وارد نشده است'})
            if event_daily_remind_me_at:
                if not event_daily_remind_me_at_time:
                    return JsonResponse({'message': 'زمان یاداوری روزانه وارد نشده است'})
            if event_monthly_remind_me_at:
                if not event_monthly_remind_me_at_day:
                    return JsonResponse({'message': 'روز یاداوری ماهانه وارد نشده است'})
                if not event_monthly_remind_me_at_time:
                    return JsonResponse({'message': 'زمان یاداوری ماهانه وارد نشده است'})
            if event_yearly_remind_me_at:
                if not event_yearly_remind_me_at_month:
                    return JsonResponse({'message': 'ماه یاداوری سالانه وارد نشده است'})
                if not event_yearly_remind_me_at_day:
                    return JsonResponse({'message': 'روز یاداوری سالانه وارد نشده است'})
                if not event_yearly_remind_me_at_time:
                    return JsonResponse({'message': 'زمان یاداوری سالانه وارد نشده است'})

            new_event = Event.objects.create(
                name=event_title,
                description=event_description,
                start_date=date_string_to_date_format(f'{event_start_date}/{event_start_time}'),
                end_date=date_string_to_date_format(f'{event_end_date}/{event_end_time}'),
                remind_me_at=date_string_to_date_format(
                    f'{event_remind_me_at_once_date}/{event_remind_me_at_once_time}'),
                remind_me_hourly_at=event_hourly_remind_me_at_number,
                remin_me_daily_at=date_string_to_date_format(f'1402/01/01/{event_daily_remind_me_at_time}'),
                remind_me_monthly_at=date_string_to_date_format(f'1402/01/{event_monthly_remind_me_at_day}/{event_monthly_remind_me_at_time}'),
                remind_me_yearly_at=date_string_to_date_format(f'1402/{event_yearly_remind_me_at_month}/{event_yearly_remind_me_at_day}/{event_yearly_remind_me_at_time}'),
                created_by=request.user,
            )
            return JsonResponse({'message': 'با موفقیت انجام شد'})
        else:
            return redirect('accounts:login')


def event_list_view(request):
    context = {'page_title': 'لیست یاداوری ها - ',
               'navigation_icon_menu_id': 'service',
               'navigation_menu_body_id': 'navigationService',
               'navigation_menu_body_sub_item_id': 'list-event',
               }
    if request.user.is_authenticated:
        if request.method == 'GET':
            events = EventRemind.objects.filter(created_by=request.user)
            context['events'] = events
            return render(request, 'calendar-event/event-list.html', context)
        else:
            return JsonResponse({'message': 'not allowed'})
    else:
        return redirect('accounts:login')


def event_edit_view(request, event_id):
    context = {'page_title': 'ویرایش رویداد - ',
               'navigation_icon_menu_id': 'service',
               'navigation_menu_body_id': 'navigationService',
               'navigation_menu_body_sub_item_id': 'list-event',
               }
    if request.user.is_authenticated:
        if request.method == 'GET':
            try:
                event = EventRemind.objects.get(id=int(event_id), created_by=request.user)
                context['event'] = event
            except:
                return JsonResponse({'message': 'no such item'})
            return render(request, 'calendar-event/edit-event.html', context)
        else:
            try:
                event_title = request.POST['event-title']
                if event_title == '':
                    event_title = None
            except:
                event_title = None
            try:
                event_description = request.POST['event-description']
                if event_description == '':
                    event_description = None
            except:
                event_description = None
            try:
                checkbox = request.POST['checkbox']
                if checkbox == '':
                    checkbox = None
            except:
                checkbox = None
            try:
                date_picker_shamsi = request.POST['date-picker-shamsi']
                if date_picker_shamsi == '':
                    date_picker_shamsi = None
                date_list = str(date_picker_shamsi).replace('-', ' ').replace(':', ' ').split()
                date_picker_shamsi = jdatetime.datetime(year=int(date_list[0]), month=int(date_list[1]),
                                                        day=int(date_list[2])
                                                        , hour=int(date_list[4]), minute=int(date_list[3]))
            except:
                date_picker_shamsi = None
            event = EventRemind.objects.get(id=int(event_id), created_by=request.user)
            event_object = event.event
            event_object.event_name = event_title
            event_object.event_description = event_description
            event_object.save()
            if checkbox == 'on' and date_picker_shamsi is not None:
                if jdatetime.datetime.now() < date_picker_shamsi:
                    event.date = date_picker_shamsi
                    event.has_been_reminded = False
                    event.save()
            else:
                event.date = event.created_at
                event.has_been_reminded = True
                event.save()
            return redirect('events:event-list')
    else:
        return redirect('accounts:login')


def event_delete_view(request, event_id):
    event = EventRemind.objects.get(id=int(event_id), created_by=request.user)
    event_object = event.event
    event_object.delete()
    return redirect('events:event-list')


#
#
# class ReminderSingle(APIView):
#     authentication_classes = (SessionAuthentication,)
#     permission_classes = (CustomIsAuthenticated,)
#
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.context = {}
#
#     def get(self, request, *args, **kwargs):
#         json_response_body = {
#             'request': 'جزئیات آبجکت یاداوری',
#             'راهنمایی استفاده از متد های REST': {
#                 'پیش فرض': {
#                     'توضیحات': 'احراز هویت بر اساس متد سشن می باشد. کاربر با لاگین موفق تا 10 روز اجازه دسترسی به محتوا را خواهد داشت',
#                 },
#                 'GET': {
#                     'توضیحات': 'راهنمایی های لازم در خصوص استفاده از API مربوطه',
#                     'سبک داده مورد پذیرش': 'وارد کردن لینک API بصورت مستقیم از طریق مرورگر',
#                 },
#                 'POST': {
#                     'توضیحات': 'از طریق این متد امکان بررسی جزئیات آبجکت یاداوری فراهم شده است',
#                     'سبک داده مورد پذیرش': 'json جیسون',
#                     'داده های ارسالی': {
#                         'reminder_object_id': 'آیدی آبجکت یاداوری'
#                     },
#                     'خطا های احتمالی': {
#                         'فرمت ورودی صحیح نمی باشد': 'جیسون ارسالی شامل مقادیر از پیش مشخص شده نیست',
#                         'ناموفق. رویداد با آیدی ارائه شده وجود ندارد': 'آبجکت یاداوری با آیدی ارائه شده وجود ندارد',
#                     }
#                 },
#                 'DELETE': {
#                     'توضیحات': 'از طریق این متد امکان حذف آبجکت یاداوری فراهم شده است',
#                     'سبک داده مورد پذیرش': 'json جیسون',
#                     'داده های ارسالی': {
#                         'reminder_object_id': 'آیدی آبجکت یاداوری'
#                     },
#                     'خطا های احتمالی': {
#                         'فرمت ورودی صحیح نمی باشد': 'جیسون ارسالی شامل مقادیر از پیش مشخص شده نیست',
#                         'ناموفق. رویداد با آیدی ارائه شده وجود ندارد': 'آبجکت یاداوری با آیدی ارائه شده وجود ندارد',
#                     }
#                 },
#             }
#         }
#         return JsonResponse(json_response_body)
#
#     def post(self, request, *args, **kwargs):
#         front_input = json.loads(request.body)
#         try:
#             reminder_object_id = front_input['reminder_object_id']
#             try:
#                 reminder_objects = EventRemind.objects.filter(created_by=request.user, id=reminder_object_id)
#                 if reminder_objects.count() == 0:
#                     raise Exception
#                 serializer = EventRemindSerializer(reminder_objects, many=True)
#                 return Response(serializer.data)
#             except Exception as e:
#                 print(str(e))
#                 json_response_body = {
#                     'method': 'post',
#                     'request': 'نمایش آبجکت یاداوری',
#                     'result': 'ناموفق. آبجکت یاداوری با آیدی ارائه شده وجود ندارد',
#                     'event id': reminder_object_id,
#                 }
#
#             return JsonResponse(json_response_body)
#         except:
#             json_response_body = {
#                 'method': 'post',
#                 'request': 'نمایش آبجکت یاداوری',
#                 'result': 'ناموفق',
#                 'message': 'فرمت ورودی صحیح نمی باشد'
#             }
#             return JsonResponse(json_response_body)
#
#     def delete(self, request, *args, **kwargs):
#         front_input = json.loads(request.body)
#         try:
#             reminder_object_id = front_input['reminder_object_id']
#             try:
#                 reminder_object = EventRemind.objects.get(created_by=request.user, id=reminder_object_id)
#                 reminder_object.delete()
#                 json_response_body = {
#                     'method': 'delete',
#                     'request': 'حذف آبجکت یاداوری',
#                     'result': 'آبجکت یاداوری با موفقیت حذف شد',
#                 }
#                 return JsonResponse(json_response_body)
#             except:
#                 json_response_body = {
#                     'method': 'post',
#                     'request': 'حذف آبجکت یاداوری',
#                     'result': 'ناموفق. آبجکت یاداوری با آیدی ارائه شده وجود ندارد',
#                     'reminder id': reminder_object_id,
#                 }
#                 return JsonResponse(json_response_body)
#
#         except:
#             json_response_body = {
#                 'method': 'post',
#                 'request': 'حذف آبجکت یاداوری',
#                 'result': 'ناموفق',
#                 'message': 'فرمت ورودی صحیح نمی باشد'
#             }
#             return JsonResponse(json_response_body)
#
#
# class ReminderList(APIView):
#     authentication_classes = (SessionAuthentication,)
#     permission_classes = (CustomIsAuthenticated,)
#
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.context = {'detail': 'لیست آبجکت های یاداوری'}
#
#     def get(self, request, *args, **kwargs):
#         json_response_body = {
#             'request': 'لیست آبجکت های یاداوری',
#             'راهنمایی استفاده از متد های REST': {
#                 'پیش فرض': {
#                     'توضیحات': 'ضمیمه هدر توکن فعال کاربر می باشد',
#                     'نمونه': 'Authorization: Token a4a3b0b69cca4c4ce4ae58023be4b4f601a604ed3be9cc0797ec53d3e01a6551',
#                 },
#                 'GET': {
#                     'توضیحات': 'راهنمایی های لازم در خصوص استفاده از API مربوطه',
#                     'سبک داده مورد پذیرش': 'وارد کردن لینک API بصورت مستقیم از طریق مرورگر',
#                 },
#                 'POST': {
#                     'توضیحات': 'از طریق این متد امکان دریافت لیست آبجکت های یاداوری فراهم شده است',
#                     'سبک داده مورد پذیرش': 'json جیسون',
#                     'داده های ارسالی': 'ندارد',
#                     'خطا های احتمالی': {
#                         'نامشخص': 'خطای سیستم'
#                     }
#                 },
#             }
#         }
#         return JsonResponse(json_response_body)
#
#     def post(self, request, *args, **kwargs):
#         reminder_objects = EventRemind.objects.filter(created_by=request.user)
#         serializer = EventRemindSerializer(reminder_objects, many=True)
#         return Response(serializer.data)
#
#
# class ReminderNew(APIView):
#     authentication_classes = (SessionAuthentication,)
#     permission_classes = (CustomIsAuthenticated,)
#
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.context = {'detail': 'ساخت آبجکت یاداوری'}
#
#     def get(self, request, *args, **kwargs):
#         json_response_body = {
#             'request': 'ایجاد آبجکت یاداوری',
#             'راهنمایی استفاده از متد های REST': {
#                 'پیش فرض': {
#                     'توضیحات': 'ضمیمه هدر توکن فعال کاربر می باشد',
#                     'نمونه': 'Authorization: Token a4a3b0b69cca4c4ce4ae58023be4b4f601a604ed3be9cc0797ec53d3e01a6551',
#                 },
#                 'GET': {
#                     'توضیحات': 'راهنمایی های لازم در خصوص استفاده از API مربوطه',
#                     'سبک داده مورد پذیرش': 'وارد کردن لینک API بصورت مستقیم از طریق مرورگر',
#                 },
#                 'POST': {
#                     'توضیحات': 'از طریق این متد امکان ایجاد آبجکت یاداوری فراهم شده است',
#                     'سبک داده مورد پذیرش': 'json جیسون',
#                     'داده های ارسالی': {
#                         'date': "1403_01_01_12_00_00",
#                     },
#                     'خطا های احتمالی': {
#                         'فرمت ورودی صحیح نمی باشد': 'داده ارسالی شامل موارد از پیش تعیین شده نیست یا بدرستی ارسال نشده است'
#                     }
#                 },
#             }
#         }
#         return JsonResponse(json_response_body)
#
#     def post(self, request, *args, **kwargs):
#         front_input = json.loads(request.body)
#         try:
#             date = front_input['date']
#             reminder = str(date).replace('_', ' ')
#             reminder = reminder.split()
#             year = reminder[0]
#             month = reminder[1]
#             day = reminder[2]
#             hour = reminder[3]
#             minute = reminder[4]
#             second = reminder[5]
#             date = jdatetime.datetime(year=int(year), month=int(month), day=int(day), hour=int(hour),
#                                       minute=int(minute), second=int(second))
#
#             new_preferred_date = EventRemind(
#                 date=date,
#                 created_by=request.user
#             )
#             new_preferred_date.save()
#             reminders = EventRemind.objects.filter(created_by=request.user, id=new_preferred_date.id)
#             serializer = EventRemindSerializer(reminders, many=True)
#             return Response(serializer.data)
#         except Exception as e:
#             print(str(e))
#             json_response_body = {
#                 'method': 'post',
#                 'request': 'ایجاد آبجکت یاداوری',
#                 'result': 'ناموفق',
#                 'message': 'فرمت ورودی صحیح نمی باشد'
#             }
#             return JsonResponse(json_response_body)
#
#
# class EventSingle(APIView):
#     authentication_classes = (SessionAuthentication,)
#     permission_classes = (CustomIsAuthenticated,)
#
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.context = {}
#
#     def get(self, request, *args, **kwargs):
#         json_response_body = {
#             'request': 'جزئیات رویداد',
#             'راهنمایی استفاده از متد های REST': {
#                 'پیش فرض': {
#                     'توضیحات': 'ضمیمه هدر توکن فعال کاربر می باشد',
#                     'نمونه': 'Authorization: Token a4a3b0b69cca4c4ce4ae58023be4b4f601a604ed3be9cc0797ec53d3e01a6551',
#                 },
#                 'GET': {
#                     'توضیحات': 'راهنمایی های لازم در خصوص استفاده از API مربوطه',
#                     'سبک داده مورد پذیرش': 'وارد کردن لینک API بصورت مستقیم از طریق مرورگر',
#                 },
#                 'POST': {
#                     'توضیحات': 'از طریق این متد امکان بررسی جزئیات رویداد فراهم شده است',
#                     'سبک داده مورد پذیرش': 'json جیسون',
#                     'داده های ارسالی': {
#                         'event_id': 'آیدی رویداد'
#                     },
#                     'خطا های احتمالی': {
#                         'فرمت ورودی صحیح نمی باشد': 'جیسون ارسالی شامل مقادیر از پیش مشخص شده نیست',
#                         'ناموفق. رویداد با آیدی ارائه شده وجود ندارد': 'رویداد با آیدی ارائه شده وجود ندارد',
#                     }
#                 },
#                 'PUT': {
#                     'توضیحات': 'از طریق این متد امکان ویرایش رویداد فراهم شده است',
#                     'سبک داده مورد پذیرش': 'json جیسون',
#                     'داده های ارسالی': {
#                         'event_id': 'آیدی رویداد',
#                         'event_name': "نام رویداد",
#                         'event_description': "توضیحات رویداد",
#                         'remind_me_at_ids': {
#                             0: "آیدی آبجکت یاداوری",
#                             1: "آیدی آبجکت یاداوری",
#                             2: "...",
#                         },
#                     },
#                     'خطا های احتمالی': {
#                         'فرمت ورودی صحیح نمی باشد': 'جیسون ارسالی شامل مقادیر از پیش مشخص شده نیست',
#                         'ناموفق. رویداد با آیدی ارائه شده وجود ندارد': 'رویداد با آیدی ارائه شده وجود ندارد',
#                     }
#                 },
#                 'DELETE': {
#                     'توضیحات': 'از طریق این متد امکان حذف رویداد فراهم شده است',
#                     'سبک داده مورد پذیرش': 'json جیسون',
#                     'داده های ارسالی': {
#                         'event_id': 'آیدی رویداد'
#                     },
#                     'خطا های احتمالی': {
#                         'فرمت ورودی صحیح نمی باشد': 'جیسون ارسالی شامل مقادیر از پیش مشخص شده نیست',
#                         'ناموفق. رویداد با آیدی ارائه شده وجود ندارد': 'رویداد با آیدی ارائه شده وجود ندارد',
#                     }
#                 },
#             }
#         }
#         return JsonResponse(json_response_body)
#
#     def post(self, request, *args, **kwargs):
#         front_input = json.loads(request.body)
#         try:
#             event_id = front_input['event_id']
#             try:
#                 events = CustomEvent.objects.filter(created_by=request.user, id=event_id)
#                 if events.count() == 0:
#                     raise Exception
#                 serializer = CustomEventSerializer(events, many=True)
#                 return Response(serializer.data)
#             except Exception as e:
#                 print(str(e))
#                 json_response_body = {
#                     'method': 'post',
#                     'request': 'نمایش جزئیات رویداد',
#                     'result': 'ناموفق. رویداد با آیدی ارائه شده وجود ندارد',
#                     'event id': event_id,
#                 }
#
#             return JsonResponse(json_response_body)
#         except:
#             json_response_body = {
#                 'method': 'post',
#                 'request': 'نمایش جزئیات رویداد',
#                 'result': 'ناموفق',
#                 'message': 'فرمت ورودی صحیح نمی باشد'
#             }
#             return JsonResponse(json_response_body)
#
#     def put(self, request, *args, **kwargs):
#         front_input = json.loads(request.body)
#         try:
#             event_id = front_input['event_id']
#             try:
#                 event = CustomEvent.objects.get(created_by=request.user, id=event_id)
#                 try:
#                     event_name = front_input['event_name']
#                     event.event_name = event_name
#                     event.save()
#                 except:
#                     pass
#                 try:
#                     event_description = front_input['event_description']
#                     event.event_description = event_description
#                     event.save()
#                 except:
#                     pass
#                 try:
#                     remind_me_at_ids = front_input['remind_me_at_ids']
#                     if remind_me_at_ids is not None:
#                         event.remind_me_at.clear()
#                     i = 0
#                     for remind_me_at_id in remind_me_at_ids:
#                         try:
#                             remind_me_at = EventRemind.objects.get(created_by=request.user,
#                                                                    id=int(remind_me_at_ids[str(i)]))
#                             event.remind_me_at.add(remind_me_at)
#                             event.save()
#                         except:
#                             pass
#                         i += 1
#                 except Exception as e:
#                     print(str(e))
#                     pass
#                 events = CustomEvent.objects.filter(created_by=request.user, id=event_id)
#                 serializer = CustomEventSerializer(events, many=True)
#                 return Response(serializer.data)
#             except:
#                 json_response_body = {
#                     'method': 'post',
#                     'request': 'ویرایش رویداد',
#                     'result': 'ناموفق. رویداد با آیدی ارائه شده وجود ندارد',
#                     'event id': event_id,
#                 }
#                 return JsonResponse(json_response_body)
#
#         except:
#             json_response_body = {
#                 'method': 'post',
#                 'request': 'ویرایش رویداد',
#                 'result': 'ناموفق',
#                 'message': 'فرمت ورودی صحیح نمی باشد'
#             }
#             return JsonResponse(json_response_body)
#
#     def delete(self, request, *args, **kwargs):
#         front_input = json.loads(request.body)
#         try:
#             event_id = front_input['event_id']
#             try:
#                 event = CustomEvent.objects.get(created_by=request.user, id=event_id)
#                 event.delete()
#                 json_response_body = {
#                     'method': 'delete',
#                     'request': 'حذف رویداد',
#                     'result': 'رویداد با موفقیت حذف شد',
#                 }
#                 return JsonResponse(json_response_body)
#             except:
#                 json_response_body = {
#                     'method': 'post',
#                     'request': 'حذف رویداد',
#                     'result': 'ناموفق. رویداد با آیدی ارائه شده وجود ندارد',
#                     'event id': event_id,
#                 }
#                 return JsonResponse(json_response_body)
#
#         except:
#             json_response_body = {
#                 'method': 'post',
#                 'request': 'حذف رویداد',
#                 'result': 'ناموفق',
#                 'message': 'فرمت ورودی صحیح نمی باشد'
#             }
#             return JsonResponse(json_response_body)
#
#
# class EventList(APIView):
#     authentication_classes = (SessionAuthentication,)
#     permission_classes = (CustomIsAuthenticated,)
#
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.context = {'detail': 'لیست رویداد ها'}
#
#     def get(self, request, *args, **kwargs):
#         json_response_body = {
#             'request': 'لیست رویداد ها',
#             'راهنمایی استفاده از متد های REST': {
#                 'پیش فرض': {
#                     'توضیحات': 'ضمیمه هدر توکن فعال کاربر می باشد',
#                     'نمونه': 'Authorization: Token a4a3b0b69cca4c4ce4ae58023be4b4f601a604ed3be9cc0797ec53d3e01a6551',
#                 },
#                 'GET': {
#                     'توضیحات': 'راهنمایی های لازم در خصوص استفاده از API مربوطه',
#                     'سبک داده مورد پذیرش': 'وارد کردن لینک API بصورت مستقیم از طریق مرورگر',
#                 },
#                 'POST': {
#                     'توضیحات': 'از طریق این متد امکان دریافت لیست رویداد ها فراهم شده است',
#                     'سبک داده مورد پذیرش': 'json جیسون',
#                     'داده های ارسالی': 'ندارد',
#                     'خطا های احتمالی': {
#                         'نامشخص': 'خطای سیستم'
#                     }
#                 },
#             }
#         }
#         return JsonResponse(json_response_body)
#
#     def post(self, request, *args, **kwargs):
#         events = CustomEvent.objects.filter(created_by=request.user)
#         serializer = CustomEventSerializer(events, many=True)
#         return Response(serializer.data)
#
#
# class EventNew(APIView):
#     authentication_classes = (SessionAuthentication,)
#     permission_classes = (CustomIsAuthenticated,)
#
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.context = {'detail': 'ساخت رویداد'}
#
#     def get(self, request, *args, **kwargs):
#         json_response_body = {
#             'request': 'ایجاد رویداد',
#             'راهنمایی استفاده از متد های REST': {
#                 'پیش فرض': {
#                     'توضیحات': 'ضمیمه هدر توکن فعال کاربر می باشد',
#                     'نمونه': 'Authorization: Token a4a3b0b69cca4c4ce4ae58023be4b4f601a604ed3be9cc0797ec53d3e01a6551',
#                 },
#                 'GET': {
#                     'توضیحات': 'راهنمایی های لازم در خصوص استفاده از API مربوطه',
#                     'سبک داده مورد پذیرش': 'وارد کردن لینک API بصورت مستقیم از طریق مرورگر',
#                 },
#                 'POST': {
#                     'توضیحات': 'از طریق این متد امکان ایجاد رویداد فراهم شده است',
#                     'سبک داده مورد پذیرش': 'json جیسون',
#                     'داده های ارسالی': {
#                         'event_name': "نام رویداد",
#                         'event_description': "توضیحات رویداد",
#                         'remind_me_at_ids': {
#                             0: "آیدی آبجکت یاداوری",
#                             1: "آیدی آبجکت یاداوری",
#                             2: "...",
#                         },
#                     },
#                     'خطا های احتمالی': {
#                         'نامشخص': 'خطای سیستم'
#                     }
#                 },
#             }
#         }
#         return JsonResponse(json_response_body)
#
#     def post(self, request, *args, **kwargs):
#         front_input = json.loads(request.body)
#         try:
#             event_name = front_input['event_name']
#             event_description = front_input['event_description']
#             remind_me_at_ids = front_input['remind_me_at_ids']
#             new_event = CustomEvent(
#                 event_name=event_name,
#                 event_description=event_description,
#             )
#             new_event.save()
#             for remind_me_at_id in remind_me_at_ids:
#                 try:
#                     remind_me_at = PreferredDate.objects.get(created_by=request.user, id=remind_me_at_id)
#                     new_event.remind_me_at.add(remind_me_at)
#                     new_event.save()
#                 except:
#                     pass
#             events = CustomEvent.objects.filter(created_by=request.user, id=new_event.id)
#             serializer = CustomEventSerializer(events, many=True)
#             return Response(serializer.data)
#         except:
#             json_response_body = {
#                 'method': 'post',
#                 'request': 'ایجاد رویداد',
#                 'result': 'ناموفق',
#                 'message': 'فرمت ورودی صحیح نمی باشد'
#             }
#             return JsonResponse(json_response_body)


def ajax_event_list(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            user_events = Event.objects.filter(created_by=request.user)
            event_list = []
            for user_event in user_events:
                if user_event.start_date and user_event.end_date:
                    event = {
                        'title': user_event.name,
                        'start': str(jdatetime.date.togregorian(user_event.start_date)),
                        'end': str(jdatetime.date.togregorian(user_event.end_date + jdatetime.timedelta(days=1))),
                    }
                    event_list.append(event)
            return JsonResponse(event_list, safe=False)
        else:
            return JsonResponse({'message': 'not allowed'})
    else:
        return JsonResponse({'message': 'not authorized'})


def date_string_to_date_format(date):
    print(date)
    if str(date).find('None') != -1:
        return None
    date_list = str(date).replace('/', ' ').replace(':', ' ').split()
    date_shamsi = jdatetime.datetime(year=int(date_list[0]), month=int(date_list[1]), day=int(date_list[2]),
                                     hour=int(date_list[3]), minute=int(date_list[4]))
    return date_shamsi
