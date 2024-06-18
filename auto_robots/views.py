import json
import threading

import jdatetime
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View

from accounts.models import Profile
from auto_robots.models import Bot, MetaPost
from calendar_event.views import date_string_to_date_format
from subscription.templatetags.subscription_tag import has_user_active_licence
from utilities.http_metod import fetch_data_from_http_post, fetch_datalist_from_http_post
from utilities.messengers.messenger import messenger
from utilities.telegram_message_handler import telegram_http_send_message_via_post_method


class AutoRobotList(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.context = {'page_title': 'ربات های من',
                        'navigation_icon_menu_id': 'service',
                        'navigation_menu_body_id': 'navigationService',
                        'navigation_menu_body_sub_item_id': 'auto-robot-list',
                        'breadcrumb_1': 'خانه',
                        'breadcrumb_2': 'ارسال پیشرفته',
                        'breadcrumb_3': 'لیست ربات ها',
                        }

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if not has_user_active_licence(request, 'social_licence'):
                return redirect('subscription:change-vip-plan')

            bots = Bot.objects.filter(created_by=request.user)
            self.context['bots'] = bots
            return render(request, 'auto-robots/auto-robot-list.html', self.context)
        else:
            return redirect('accounts:login')

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return render(request, '404.html')
        else:
            return redirect('accounts:login')


class AutoRobotNew(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.context = {'page_title': 'ثبت ربات جدید',
                        'navigation_icon_menu_id': 'service',
                        'navigation_menu_body_id': 'navigationService',
                        'navigation_menu_body_main_item_id': 'metapost',
                        'breadcrumb_1': 'خانه',
                        'breadcrumb_2': 'ارسال پیشرفته',
                        'breadcrumb_3': 'ثبت ربات جدید',
                        }

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if not has_user_active_licence(request, 'social_licence'):
                return redirect('subscription:change-vip-plan')
            return render(request, 'auto-robots/auto-robot-new.html', self.context)
        else:
            return redirect('accounts:login')

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if not has_user_active_licence(request, 'social_licence'):
                return redirect('subscription:change-vip-plan')

            auto_robot_type = fetch_data_from_http_post(request, 'auto_robot_type',  self.context)
            auto_robot_name = fetch_data_from_http_post(request, 'auto_robot_name', self.context)
            auto_robot_token = fetch_data_from_http_post(request, 'auto_robot_token', self.context)
            auto_robot_belong_to = fetch_data_from_http_post(request, 'auto_robot_belong_to', self.context)
            auto_robot_has_access_to = fetch_data_from_http_post(request, 'auto_robot_has_access_to', self.context)

            if auto_robot_type is None:
                self.context['alert'] = 'نوع ربات انتخاب نشده است'
                return render(request, 'auto-robots/auto-robot-new.html', self.context)
            if auto_robot_name is None:
                self.context['alert'] = 'نام ربات بدرستی وارد نشده است'
                return render(request, 'auto-robots/auto-robot-new.html', self.context)

            new_social = Bot(
                bot_type=auto_robot_type,
                bot_name=auto_robot_name,
                bot_token=auto_robot_token,
                bot_token_belongs_to=auto_robot_belong_to,
                has_access_to_channels=auto_robot_has_access_to,
                created_by=request.user,
            )
            new_social.save()
            return redirect('auto_robots:auto-robots-list')
        else:
            return redirect('accounts:login')


class AutoRobotEdit(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.context = {'navigation_icon_menu_id': 'service',
                        'navigation_menu_body_id': 'navigationService',
                        'navigation_menu_body_main_item_id': 'metapost',
                        'breadcrumb_1': 'خانه',
                        'breadcrumb_2': 'ارسال پیشرفته',
                        'breadcrumb_3': 'ویرایش ربات',
                        }

    def get(self, request, auto_robot_id, *args, **kwargs):
        if request.user.is_authenticated:
            if not has_user_active_licence(request, 'social_licence'):
                return redirect('subscription:change-vip-plan')

            try:
                bot = Bot.objects.get(id=auto_robot_id, created_by=request.user)
                self.context['page_title'] = f'ویرایش ربات {bot.bot_name}'
                self.context['breadcrumb_3'] = f'ویرایش ربات {bot.bot_name}'
                self.context['bot'] = bot
                return render(request, 'auto-robots/auto-robot-edit.html', self.context)
            except Exception as e:
                return render(request, '404.html')
        else:
            return redirect('accounts:login')

    def post(self, request, auto_robot_id, *args, **kwargs):
        if request.user.is_authenticated:
            if not has_user_active_licence(request, 'social_licence'):
                return redirect('subscription:change-vip-plan')

            try:
                bot = Bot.objects.get(id=auto_robot_id, created_by=request.user)
                self.context['bot'] = bot
            except Exception as e:
                return render(request, '404.html')

            auto_robot_type = fetch_data_from_http_post(request, 'auto_robot_type', self.context)
            auto_robot_name = fetch_data_from_http_post(request, 'auto_robot_name', self.context)
            auto_robot_token = fetch_data_from_http_post(request, 'auto_robot_token', self.context)
            auto_robot_belong_to = fetch_data_from_http_post(request, 'auto_robot_belong_to',
                                                                       self.context)
            auto_robot_has_access_to = fetch_data_from_http_post(request, 'auto_robot_has_access_to',
                                                                           self.context)
            if auto_robot_type is None:
                self.context['alert'] = 'نوع ربات انتخاب نشده است'
                return render(request, 'auto-robots/auto-robot-edit.html', self.context)
            if auto_robot_name is None:
                self.context['alert'] = 'نام ربات بدرستی وارد نشده است'
                return render(request, 'auto-robots/auto-robot-edit.html', self.context)

            bot.bot_type = auto_robot_type
            bot.bot_name = auto_robot_name
            bot.bot_token = auto_robot_token
            bot.bot_token_belongs_to = auto_robot_belong_to
            bot.has_access_to_channels = auto_robot_has_access_to
            bot.save()

            return redirect('auto_robots:auto-robots-edit-with-id', auto_robot_id=bot.id)

        else:
            return redirect('accounts:login')


class AutoRobotRemove(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.context = {'navigation_icon_menu_id': 'service',
                        'navigation_menu_body_id': 'navigationService',
                        'navigation_menu_body_main_item_id': 'metapost',
                        }

    def get(self, request, auto_robot_id, *args, **kwargs):
        return render(request, '404.html')

    def post(self, request, auto_robot_id, *args, **kwargs):
        if request.user.is_authenticated:
            if not has_user_active_licence(request, 'social_licence'):
                return redirect('subscription:change-vip-plan')

            if request.method == 'POST':
                try:
                    bot = Bot.objects.get(id=auto_robot_id, created_by=request.user)
                    bot.delete()
                except:
                    pass
            return redirect('auto_robots:auto-robots-list')
        else:
            return redirect('accounts:login')


class MetaPostList(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.context = {'page_title': 'متا های من',
                        'navigation_icon_menu_id': 'service',
                        'navigation_menu_body_id': 'navigationService',
                        'navigation_menu_body_sub_item_id': 'metapost-list',
                        'breadcrumb_1': 'خانه',
                        'breadcrumb_2': 'ارسال پیشرفته',
                        'breadcrumb_3': 'لیست متا های من',
                        }

    def get(self, request, auto_robot_id, *args, **kwargs):
        if request.user.is_authenticated:
            if not has_user_active_licence(request, 'social_licence'):
                return redirect('subscription:change-vip-plan')

            bots = Bot.objects.filter(created_by=request.user)
            self.context['bots'] = bots
            if bots.count() == 0:
                return redirect('auto_robots:auto-robots-new')
            if auto_robot_id == 0:
                metaposts = MetaPost.objects.filter(created_by=request.user)
                self.context['metaposts'] = metaposts
                metaposts_summary = get_metaposts_summery(metaposts)
                self.context['metaposts_summary'] = metaposts_summary
                return render(request, 'auto-robots/metapost-list.html', self.context)
            try:
                bot = Bot.objects.get(id=auto_robot_id, created_by=request.user)
                self.context['bot'] = bot
            except:
                return render(request, '404.html')

            metaposts = MetaPost.objects.filter(bot=bot, created_by=request.user)
            self.context['metaposts'] = metaposts

            metaposts_summary = get_metaposts_summery(metaposts)
            self.context['metaposts_summary'] = metaposts_summary

            return render(request, 'auto-robots/metapost-list.html', self.context)
        else:
            return redirect('accounts:login')

    def post(self, request, auto_robot_id, *args, **kwargs):
        if request.user.is_authenticated:
            if not has_user_active_licence(request, 'social_licence'):
                return redirect('subscription:change-vip-plan')

            bots = Bot.objects.filter(created_by=request.user)
            self.context['bots'] = bots
            if bots.count() == 0:
                return redirect('auto_robots:auto-robots-new')
            date_from = fetch_data_from_http_post(request, 'date_from', self.context)
            date_to = fetch_data_from_http_post(request, 'date_to', self.context)
            metapost_send_at_type = fetch_data_from_http_post(request, 'metapost_send_at_type', self.context)
            metapost_message_status = fetch_data_from_http_post(request, 'metapost_message_status', self.context)

            if date_from:
                self.context['date_from'] = date_from
                date_from = str(date_from).split('/')
                date_from = jdatetime.datetime(year=int(date_from[0]), month=int(date_from[1]), day=int(date_from[2]))
            if date_to:
                self.context['date_to'] = date_to
                date_to = str(date_to).split('/')
                date_to = jdatetime.datetime(year=int(date_to[0]), month=int(date_to[1]), day=int(date_to[2]))
            q = Q()
            if date_from and date_to:
                q &= Q(created_at__range=[date_from, date_to])
            elif date_from and not date_to:
                q &= Q(created_at__gte=date_from)
            elif not date_from and date_to:
                q &= Q(created_at__lte=date_to)
            else:
                pass
            if metapost_send_at_type:
                self.context['metapost_send_at_type'] = metapost_send_at_type
                if metapost_send_at_type != 'nothing':
                    q &= Q(send_at_type=metapost_send_at_type)
            if metapost_message_status:
                self.context['metapost_message_status'] = metapost_message_status
                if metapost_message_status != 'nothing':
                    q &= Q(message_status=metapost_message_status)
            q &= Q(created_by=request.user)

            if auto_robot_id == 0:
                metaposts = MetaPost.objects.filter(q)
                self.context['metaposts'] = metaposts
                metaposts_summary = get_metaposts_summery(metaposts)
                self.context['metaposts_summary'] = metaposts_summary
                return render(request, 'auto-robots/metapost-list.html', self.context)
            try:
                bot = Bot.objects.get(id=auto_robot_id, created_by=request.user)
                self.context['bot'] = bot
                q &= Q(bot=bot)
                metaposts = MetaPost.objects.filter(q)
                self.context['metaposts'] = metaposts
                metaposts_summary = get_metaposts_summery(metaposts)
                self.context['metaposts_summary'] = metaposts_summary
                return render(request, 'auto-robots/metapost-list.html', self.context)
            except:
                return render(request, '404.html')
        else:
            return redirect('accounts:login')


class MetaPostNew(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.context = {'page_title': 'متا جدید',
                        'navigation_icon_menu_id': 'service',
                        'navigation_menu_body_id': 'navigationService',
                        'navigation_menu_body_sub_item_id': 'metapost-new',
                        'breadcrumb_1': 'خانه',
                        'breadcrumb_2': 'ارسال پیشرفته',
                        'breadcrumb_3': 'متا جدید',
                        }

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if not has_user_active_licence(request, 'social_licence'):
                return redirect('subscription:change-vip-plan')

            bots = Bot.objects.filter(created_by=request.user)
            self.context['bots'] = bots
            if bots.count() == 0:
                return redirect('auto_robots:auto-robots-new')
            return render(request, 'auto-robots/metapost-new.html', self.context)
        else:
            return redirect('accounts:login')

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if not has_user_active_licence(request, 'social_licence'):
                return redirect('subscription:change-vip-plan')

            bots = Bot.objects.filter(created_by=request.user)
            self.context['bots'] = bots
            if bots.count() == 0:
                return redirect('auto_robots:auto-robots-new')

            publish_with_bots = fetch_datalist_from_http_post(request, 'publish_with_bots',  self.context)
            message_action_situation = fetch_data_from_http_post(request, 'message_action_situation', self.context)
            event_remind_me_at_once = fetch_data_from_http_post(request, 'event_remind_me_at_once', self.context)
            event_remind_me_at_once_date = fetch_data_from_http_post(request, 'event_remind_me_at_once_date',
                                                                     self.context)
            event_remind_me_at_once_time = fetch_data_from_http_post(request, 'event_remind_me_at_once_time',
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
            metapost_title = fetch_data_from_http_post(request, 'metapost_title', self.context)
            metapost_sub_title = fetch_data_from_http_post(request, 'metapost_sub_title', self.context)
            metapost_categories = fetch_data_from_http_post(request, 'metapost_categories', self.context)
            metapost_keywords = fetch_data_from_http_post(request, 'metapost_keywords', self.context)
            metapost_attached_file_link = fetch_data_from_http_post(request, 'metapost_attached_file_link', self.context)
            metapost_content = fetch_data_from_http_post(request, 'metapost_content', self.context)
            metapost_view_type = fetch_data_from_http_post(request, 'metapost_view_type', self.context)

            is_remind_me_at_once_active = False
            is_send_daily_at_active = False
            is_send_monthly_at_active = False
            is_send_yearly_at_active = False

            if publish_with_bots is None:
                self.context['alert'] = 'ربات های ارسال انتخاب نشده است'
                return render(request, 'auto-robots/metapost-new.html', self.context)

            if message_action_situation is None:
                self.context['alert'] = 'زمانبندی ارسال انتخاب نشده است'
                return render(request, 'auto-robots/metapost-new.html', self.context)
            else:
                if message_action_situation == '':
                    self.context['alert'] = 'محوه عملیات ارسال بدرستی ارسال نشده است'
                    return render(request, 'auto-robots/metapost-new.html', self.context)
                else:
                    if event_remind_me_at_once:
                        is_remind_me_at_once_active = True
                        if not event_remind_me_at_once_date:
                            self.context['alert'] = 'تاریخ وارد نشده است'
                            return render(request, 'auto-robots/metapost-new.html', self.context)
                        if not event_remind_me_at_once_time:
                            self.context['alert'] = 'زمان وارد نشده است'
                            return render(request, 'auto-robots/metapost-new.html', self.context)
                    if event_daily_remind_me_at:
                        is_send_daily_at_active = True
                        if not event_daily_remind_me_at_time:
                            self.context['alert'] = 'زمان یاداوری روزانه وارد نشده است'
                            return render(request, 'auto-robots/metapost-new.html', self.context)
                    if event_monthly_remind_me_at:
                        is_send_monthly_at_active = True
                        if not event_monthly_remind_me_at_day:
                            self.context['alert'] = 'روز یاداوری ماهانه وارد نشده است'
                            return render(request, 'auto-robots/metapost-new.html', self.context)
                        if not event_monthly_remind_me_at_time:
                            self.context['alert'] = 'زمان یاداوری ماهانه وارد نشده است'
                            return render(request, 'auto-robots/metapost-new.html', self.context)
                    if event_yearly_remind_me_at:
                        is_send_yearly_at_active = True
                        if not event_yearly_remind_me_at_month:
                            self.context['alert'] = 'ماه یاداوری سالانه وارد نشده است'
                            return render(request, 'auto-robots/metapost-new.html', self.context)
                        if not event_yearly_remind_me_at_day:
                            self.context['alert'] = 'روز یاداوری سالانه وارد نشده است'
                            return render(request, 'auto-robots/metapost-new.html', self.context)
                        if not event_yearly_remind_me_at_time:
                            self.context['alert'] = 'زمان یاداوری سالانه وارد نشده است'
                            return render(request, 'auto-robots/metapost-new.html', self.context)
            if metapost_title is None:
                self.context['alert'] = 'عنوان متا انتخاب نشده است'
                return render(request, 'auto-robots/metapost-new.html', self.context)

            for bot_id in publish_with_bots:
                try:
                    bot = Bot.objects.get(id=bot_id, created_by=request.user)
                    if message_action_situation == 'just_in_time':
                        new_metapost = MetaPost(
                            bot=bot,
                            action='new_send',
                            send_at_type='در لحظه یکباره',
                            send_at_date_time=jdatetime.datetime.now(),
                            title=metapost_title,
                            sub_title=metapost_sub_title,
                            categories=metapost_categories,
                            keywords=metapost_keywords,
                            attached_file_link=metapost_attached_file_link,
                            content=metapost_content,
                            metapost_view_type=metapost_view_type,
                            message_status='sent',
                            created_by=request.user,
                            updated_by=request.user,
                        )
                        new_metapost.save()
                        messenger(new_metapost)
                    else:
                        if is_remind_me_at_once_active:
                            new_metapost = MetaPost(
                                bot=bot,
                                action='new_send',
                                send_at_type='زمانبندی شده یکباره',
                                send_at_date_time=date_string_to_date_format(f'{event_remind_me_at_once_date}/{event_remind_me_at_once_time}'),
                                title=metapost_title,
                                sub_title=metapost_sub_title,
                                categories=metapost_categories,
                                keywords=metapost_keywords,
                                attached_file_link=metapost_attached_file_link,
                                content=metapost_content,
                                metapost_view_type=metapost_view_type,
                                message_status='queued',
                                created_by=request.user,
                                updated_by=request.user,
                            )
                            new_metapost.save()
                        if is_send_daily_at_active:
                            new_metapost = MetaPost(
                                bot=bot,
                                action='new_send',
                                send_at_type='روزانه',
                                send_at_date_time=date_string_to_date_format(f'1402/01/01/{event_daily_remind_me_at_time}'),
                                title=metapost_title,
                                sub_title=metapost_sub_title,
                                categories=metapost_categories,
                                keywords=metapost_keywords,
                                attached_file_link=metapost_attached_file_link,
                                content=metapost_content,
                                metapost_view_type=metapost_view_type,
                                message_status='queued',
                                created_by=request.user,
                                updated_by=request.user,
                            )
                            new_metapost.save()
                        if is_send_monthly_at_active:
                            new_metapost = MetaPost(
                                bot=bot,
                                action='new_send',
                                send_at_type='ماهانه',
                                send_at_date_time=date_string_to_date_format(
                                    f'1402/01/{event_monthly_remind_me_at_day}/{event_monthly_remind_me_at_time}'),
                                title=metapost_title,
                                sub_title=metapost_sub_title,
                                categories=metapost_categories,
                                keywords=metapost_keywords,
                                attached_file_link=metapost_attached_file_link,
                                content=metapost_content,
                                metapost_view_type=metapost_view_type,
                                message_status='queued',
                                created_by=request.user,
                                updated_by=request.user,
                            )
                            new_metapost.save()
                        if is_send_yearly_at_active:
                            new_metapost = MetaPost(
                                bot=bot,
                                action='new_send',
                                send_at_type='سالانه',
                                send_at_date_time=date_string_to_date_format(
                                    f'1402/{event_yearly_remind_me_at_month}/{event_yearly_remind_me_at_day}/{event_yearly_remind_me_at_time}'),
                                title=metapost_title,
                                sub_title=metapost_sub_title,
                                categories=metapost_categories,
                                keywords=metapost_keywords,
                                attached_file_link=metapost_attached_file_link,
                                content=metapost_content,
                                metapost_view_type=metapost_view_type,
                                message_status='queued',
                                created_by=request.user,
                                updated_by=request.user,
                            )
                            new_metapost.save()
                except Exception as e:
                    print(str(e))

            return redirect('auto_robots:metapost-list-with-bot-id', auto_robot_id=0)
        else:
            return redirect('accounts:login')


class MetaPostEdit(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.context = {'navigation_icon_menu_id': 'service',
                        'navigation_menu_body_id': 'navigationService',
                        'navigation_menu_body_main_item_id': 'metapost',
                        'breadcrumb_1': 'خانه',
                        'breadcrumb_2': 'ارسال پیشرفته',
                        }

    def get(self, request, metapost_id, *args, **kwargs):
        if request.user.is_authenticated:
            if not has_user_active_licence(request, 'social_licence'):
                return redirect('subscription:change-vip-plan')

            try:
                metapost = MetaPost.objects.get(id=metapost_id, created_by=request.user)
                self.context['page_title'] = f'ویرایش متا {metapost.title}'
                self.context['breadcrumb_3'] = f'ویرایش متا {metapost.title}'
                self.context['metapost'] = metapost
                return render(request, 'auto-robots/metapost-edit.html', self.context)
            except Exception as e:
                return render(request, '404.html')
        else:
            return redirect('accounts:login')

    def post(self, request, metapost_id, *args, **kwargs):
        if request.user.is_authenticated:
            if not has_user_active_licence(request, 'social_licence'):
                return redirect('subscription:change-vip-plan')

            try:
                metapost = MetaPost.objects.get(id=metapost_id, created_by=request.user)
                self.context['page_title'] = f'ویرایش متا {metapost.title}'
                self.context['breadcrumb_3'] = f'ویرایش متا {metapost.title}'
                self.context['metapost'] = metapost
            except Exception as e:
                return render(request, '404.html')
            new_action = fetch_data_from_http_post(request, 'new_action', self.context)
            if metapost.message_status == 'sent':
                if new_action == 'delete':
                    metapost.action = 'delete'
                    metapost.message_status = 'deleted'
                    metapost.save()
                    messenger(metapost)

            return redirect('auto_robots:metapost-edit-with-metapost-id', metapost_id=metapost.id)

        else:
            return redirect('accounts:login')


class MetaPostRemoveSingle(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.context = {'navigation_icon_menu_id': 'service',
                        'navigation_menu_body_id': 'navigationService',
                        'navigation_menu_body_main_item_id': 'metapost',
                        }

    def get(self, request, metapost_id, *args, **kwargs):
        return render(request, '404.html')

    def post(self, request, metapost_id, *args, **kwargs):
        if request.user.is_authenticated:
            if not has_user_active_licence(request, 'social_licence'):
                return redirect('subscription:change-vip-plan')

            if request.method == 'POST':
                try:
                    metapost = MetaPost.objects.get(id=metapost_id, created_by=request.user)
                    metapost.delete()
                    return redirect('auto_robots:metapost-list-with-bot-id', auto_robot_id=metapost.bot.id)
                except:
                    pass
            return render(request, '404.html')
        else:
            return redirect('accounts:login')


class MetaPostRemoveAllRelated(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.context = {'navigation_icon_menu_id': 'service',
                        'navigation_menu_body_id': 'navigationService',
                        'navigation_menu_body_main_item_id': 'metapost',
                        }

    def get(self, request, metapost_id, *args, **kwargs):
        return render(request, '404.html')

    def post(self, request, metapost_id, *args, **kwargs):
        if request.user.is_authenticated:
            if not has_user_active_licence(request, 'social_licence'):
                return redirect('subscription:change-vip-plan')

            if request.method == 'POST':
                try:
                    metapost = MetaPost.objects.get(id=metapost_id, created_by=request.user)
                    all_related_metaposts = MetaPost.objects.filter(id=metapost_id, created_by=request.user)
                    metapost.delete()
                    return redirect('auto_robots:metapost-list-with-bot-id', auto_robot_id=metapost.bot.id)
                except:
                    pass
            return render(request, '404.html')
        else:
            return redirect('accounts:login')


def get_metaposts_summery(metaposts):
    sent_metaposts = metaposts.filter(message_status='sent')
    queued_metaposts = metaposts.filter(message_status='queued')
    total_metapost = metaposts.count()
    total_sent_metapost = sent_metaposts.count()
    total_queued_metapost = queued_metaposts.count()
    return total_metapost, total_sent_metapost, total_queued_metapost


def gap_new_message_view(request, bot_id):
    if request.user.is_authenticated:
        try:
            send_text_response = 1
            # igap_bot = Bot.objects.get(id=4)
            #
            # send_text_response = igap_send_text_message_to_channels(
            #     bot_token=igap_bot.bot_token,
            #     room_id=f"{igap_bot.has_access_to_channels}", user_message="سلام این اولین پیام من در ایگپ هست")
            print(send_text_response)

        except Exception as e:
            return JsonResponse({"message": f"{str(e)}"})

        if request.method == 'POST':
            pass
        return JsonResponse({'message': send_text_response})
    else:
        return redirect('accounts:login')


class RequestFile(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.context = {'detail': 'ثبت نام کاربر جدید'}
        self.today = jdatetime.datetime.now()

    def get(self, request, *args, **kwargs):
        return JsonResponse({'message': 'not allowed'})

    def post(self, request, *args, **kwargs):
        try:
            telegram_response_check_result = telegram_response_check(request, True)
            if not telegram_response_check_result:
                return JsonResponse({'message': 'telegram_response_has_error'})
            else:
                user_unique_id = telegram_response_check_result[0]
                user_first_name = telegram_response_check_result[1]
                message_text = telegram_response_check_result[2]
                user_phone_number = telegram_response_check_result[3]

            try:
                profile = Profile.objects.get(telegram_user_id=user_unique_id)
            except Exception as e:
                if user_phone_number:
                    try:
                        user_phone_number = str(user_phone_number).replace('+', '')
                        user = User.objects.get(username=user_phone_number)
                        user_profile = user.profile_user
                        user_profile.telegram_user_id = user_unique_id
                        user_profile.save()
                        telegram_message_need_to_create_account(user_unique_id)
                        return JsonResponse({'message': 'telegram_message_start_first_time'})
                    except:
                        telegram_message_start_first_time(user_unique_id)
                        return JsonResponse({'message': 'telegram_message_start_first_time'})
                else:
                    telegram_message_confirm_phone_number_warning(user_unique_id)
                    return JsonResponse({'message': 'telegram_message_confirm_phone_number_warning'})
            if message_text == '/start':
                telegram_message_start(user_unique_id)
                return JsonResponse({'message': 'telegram_message_start'})

            if message_text == "🔙 بازگشت":
                telegram_message_start(user_unique_id)
                return JsonResponse({'message': 'telegram_message_start'})

            if message_text == "🏡 صفحه اصلی":
                telegram_message_start(user_unique_id)
                return JsonResponse({'message': 'telegram_message_start'})

            RequestHandler().start()

            return JsonResponse({'message': 'process_links_and_send_message_to_telegram'})

        except Exception as e:
            custom_log(f'{e}')
            return JsonResponse({'message': f'{e}'})


class RequestHandler(threading.Thread):
    def __init__(self, user, message_text):
        super().__init__()
        self.user = user
        self.message_text = message_text

    def run(self):
        try:
            new_user_request_history = UserRequestHistory.objects.create(user=self.user,
                                                                         data_track=self.data_track)
            text = f'''موارد زیر توسط ربات تایید و درحال بررسی می باشند: \n\n'''
            for file_page_link in self.file_page_link_list:
                try:
                    custom_log(file_page_link)
                    file_type = file_page_link[0]
                    link = file_page_link[1]
                    file_unique_code = file_page_link[2]
                    try:
                        file = File.objects.get(file_type=file_type, unique_code=file_unique_code)
                        if file.download_percentage == 100 and str(file.file_storage_link) != '' and not file.file:
                            file.download_percentage = 0
                            file.is_acceptable_file = True
                            file.in_progress = False
                            file.failed_repeat = 0
                            file.save()
                        else:
                            if not file.is_acceptable_file and not file.in_progress and file.failed_repeat == 10:
                                file.is_acceptable_file = True
                                file.failed_repeat = 0
                                file.save()
                            else:
                                pass
                    except:
                        file = File.objects.create(file_type=file_type, page_link=link, unique_code=file_unique_code)
                    if file_type == 'envato':
                        text += f'سرویس دهنده: EnvatoElement'
                    if file_type == 'motion_array':
                        text += f'سرویس دهنده: MotionArray'
                    text += f'\n'
                    text += f'کد 🔁: {file_unique_code}'
                    text += f'\n'
                    text += f'____________________'
                    text += f'\n\n'
                    new_user_request_history.files.add(file)
                    new_user_request_history.save()
                except Exception as e:
                    custom_log('RequestHandler->forloop of file_page_link_list try/except. err: ' + str(e))
            text += f'🔷🔶🔶🔶🔶🔶🔶🔷'
            text += f'\n\n'
            telegram_response = telegram_http_send_message_via_post_method(chat_id=self.user, text=text,
                                                                           parse_mode='HTML')
            response = json.loads(telegram_response['message'])
            message_id = response['result']['message_id']
            chat_id = response['result']['chat']['id']
            UserRequestHistoryDetail.objects.create(
                user_request_history=new_user_request_history,
                telegram_chat_id=chat_id,
                telegram_message_id=message_id,
            )
        except Exception as e:
            custom_log('RequestHandler->try/except. err: ' + str(e))
        return


def telegram_response_check(request, custom_log_print: bool):
    try:
        secret_key = request.META['HTTP_X_TELEGRAM_BOT_API_SECRET_TOKEN']
        if secret_key is not None and str(secret_key) == '12587KFlk54NCJDmvn8541':
            if custom_log_print:
                custom_log('secret_key: confirmed')
            try:
                front_input = json.loads(request.body)
                if custom_log_print:
                    custom_log(str(front_input))
                try:
                    try:
                        user_unique_id = front_input['callback_query']['from']['id']
                        user_first_name = front_input['callback_query']['from']['first_name']
                        message_text = front_input['callback_query']['data']
                        response_list = [user_unique_id, user_first_name, message_text, None]
                    except:
                        try:
                            user_unique_id = front_input['message']['from']['id']
                            user_first_name = front_input['message']['from']['first_name']
                            message_text = str(front_input['message']['text'])
                            response_list = [user_unique_id, user_first_name, message_text, None]
                        except:
                            user_unique_id = front_input['message']['contact']['user_id']
                            user_first_name = front_input['message']['contact']['first_name']
                            message_text = str(front_input['message']['reply_to_message']['text'])
                            user_phone_number = front_input['message']['contact']['phone_number']
                            response_list = [user_unique_id, user_first_name, message_text, user_phone_number]
                    return response_list
                except Exception as e:
                    if custom_log_print:
                        custom_log('RequestFile->try/except. err: ' + str(e))
                    return False
            except:
                if custom_log_print:
                    custom_log('input format is not correct')
                return False
        else:
            if custom_log_print:
                custom_log('wrong secret_key')
            return False
    except:
        if custom_log_print:
            custom_log('unauthorized access')
        return False


def telegram_message_start_first_time(user_unique_id):
    message_text = "ثبت نام شما با موفقیت انجام شد. \n به ربات تلگرام یکجا مدیر خوش آمدید. در این ربات می توانید پیام های خود را ارسال نمایید"
    telegram_http_send_message_via_post_method(chat_id=user_unique_id, text=message_text, parse_mode='HTML')



def telegram_message_need_to_create_account(user_unique_id):
    message_text = "ابتدا در وبسایت https://yekjamodir.ir اکانت بسازید"
    telegram_http_send_message_via_post_method(chat_id=user_unique_id, text=message_text, parse_mode='HTML')


def telegram_message_start(user_unique_id):
    # Define the menu buttons
    menu_buttons = [
        ["راهنمای دانلود", "دانلود فایل"],
        ["شارژ حساب", "پروفایل کاربری"]
    ]

    # Create the keyboard markup
    keyboard_markup = {
        "keyboard": menu_buttons,
        "resize_keyboard": True,
        "one_time_keyboard": True
    }

    # Convert the markup to a JSON string
    reply_markup = json.dumps(keyboard_markup)

    message_text = "صفحه اصلی"
    telegram_http_send_message_via_post_method(chat_id=user_unique_id, text=message_text,
                                               reply_markup=reply_markup, parse_mode='Markdown')


def telegram_message_confirm_phone_number_warning(user_unique_id):
    reply_markup = {'keyboard': [
        [
            {'text': 'تایید شماره تلفن',
             'request_contact': True
             }
        ]
    ],
        'one_time_keyboard': True
    }

    reply_markup = json.dumps(reply_markup)

    message_text = "برای تایید عضویت لازم هست دکمه تایید شماره تلفن را انتخاب نمایید"
    telegram_http_send_message_via_post_method(chat_id=user_unique_id, text=message_text,
                                               reply_markup=reply_markup, parse_mode='Markdown')
