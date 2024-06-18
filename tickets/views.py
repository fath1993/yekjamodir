import threading

from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse
from django.urls import reverse
from django.shortcuts import render, redirect

from accounts.custom_decorator import CheckLogin, RequireMethod
from accounts.models import UserNotification
from custom_logs.models import custom_log
from gallery.models import FileGallery
from tickets.models import Ticket, Message, Notification
from tickets.serializer import MessageSerializer
from utilities.http_metod import fetch_data_from_http_post, \
    fetch_files_from_http_post_data, fetch_data_from_http_get


class TicketView:
    def __init__(self):
        super().__init__()

    @CheckLogin()
    def list(self, request, box_status, *args, **kwargs):
        q = Q()
        if box_status == 'sent':
            q &= (
                Q(**{'owner': request.user})
            )
            context = {'page_title': 'صندوق پیام های ارسالی', 'get_params': request.GET.urlencode(), 'err': request.GET.get('err', None), 'message': request.GET.get('message', None)}
        elif box_status == 'received':
            q &= (
                Q(**{'receiver': request.user})
            )
            context = {'page_title': 'صندوق پیام های دریافتی', 'get_params': request.GET.urlencode(), 'err': request.GET.get('err', None), 'message': request.GET.get('message', None)}
        elif box_status == 'all':
            if not request.user.is_superuser:
                return render(request, '404.html')
            context = {'page_title': 'مدیریت پیام های کاربران سامانه', 'get_params': request.GET.urlencode(), 'err': request.GET.get('err', None), 'message': request.GET.get('message', None)}
        else:
            return render(request, '404.html')

        tickets = Ticket.objects.filter(q).order_by('-created_at')
        context['tickets'] = tickets

        items_per_page = 50
        paginator = Paginator(tickets, items_per_page)
        page_number = request.GET.get('page')
        page = paginator.get_page(page_number)
        context['page'] = page

        return render(request, 'tickets/ticket-list.html', context)

    @CheckLogin()
    def detail(self, request, ticket_id, *args, **kwargs):
        try:
            q = Q()
            q &= Q(
                Q(**{'id': ticket_id})
            )
            if not request.user.is_superuser:
                q &= Q(
                    Q(**{'owner': request.user}) |
                    Q(**{'receiver': request.user})
                )
            ticket = Ticket.objects.get(q)

            z = Q()
            z &= Q(
                Q(**{'ticket__id': ticket_id})
            )
            if not request.user.is_superuser:
                z &= Q(
                    Q(**{'ticket__owner': request.user}) |
                    Q(**{'ticket__receiver': request.user})
                )

            messages = Message.objects.filter(z).order_by('created_at')
            context = {'page_title': f'جزئیات پیام با موضوع *{ticket.subject}*',
                       'ticket': ticket, 'messages': messages, 'get_params': request.GET.urlencode()}
            return render(request, 'tickets/ticket-detail.html', context)
        except Exception as e:
            custom_log(f'{e}')
            return render(request, '404.html')

    @CheckLogin()
    def filter(self, request, *args, **kwargs):
        pass

    @CheckLogin()
    @RequireMethod(allowed_method='POST')
    def create(self, request, *args, **kwargs):
        context = {'page_title': 'ساخت پیام جدید', 'get_params': request.GET.urlencode()}

        subject = fetch_data_from_http_post(request, 'subject', context)
        receiver = fetch_data_from_http_post(request, 'receiver', context)
        content = fetch_data_from_http_post(request, 'content', context)
        files = fetch_files_from_http_post_data(request, 'files', context)

        if not subject:
            err = 'موضوع پیام بدرستی وارد نشده است'
            return redirect(
                reverse('ticket:ticket-list-with-box-status',
                        kwargs={'box_status': 'sent'}) + f'?err={err}&{request.GET.urlencode()}')
        if not receiver:
            err = 'شناسه گیرنده بدرستی وارد نشده است'
            return redirect(
                reverse('ticket:ticket-list-with-box-status',
                        kwargs={'box_status': 'sent'}) + f'?err={err}&{request.GET.urlencode()}')
        else:
            username = str(receiver).replace('#', '')
        if not content:
            err = 'محتوای پیام بدرستی وارد نشده است'
            return redirect(
                reverse('ticket:ticket-list-with-box-status',
                        kwargs={'box_status': 'sent'}) + f'?err={err}&{request.GET.urlencode()}')

        try:
            receiver = User.objects.get(username=username)
        except:
            err = f'شناسه پیام رسانی گیرنده با مقدار {username} یافت نشد'
            return redirect(
                reverse('ticket:ticket-list-with-box-status',
                        kwargs={'box_status': 'sent'}) + f'?err={err}&{request.GET.urlencode()}')

        new_ticket = Ticket.objects.create(
            status='created',
            subject=subject,
            owner=request.user,
            receiver=receiver,
            has_seen_by_owner=True,
            has_seen_by_receiver=False,
            created_by=request.user,
            updated_by=request.user,
        )

        new_message = Message.objects.create(
            ticket=new_ticket,
            content=content,
            created_by=request.user,
        )

        if files:
            for file in files:
                try:
                    new_file = FileGallery.objects.create(
                        alt=file.name,
                        file=file,
                        created_by=request.user,
                    )
                    new_message.attachments.add(new_file)
                except:
                    pass

        message = f'پیام با شناسه یکتای {new_ticket.id} ایجاد گردید'
        return redirect(
            reverse('ticket:ticket-list-with-box-status',
                    kwargs={'box_status': 'sent'}) + f'?message={message}&{request.GET.urlencode()}')


    @CheckLogin()
    def delete(self, request, ticket_id, *args, **kwargs):
        try:
            ticket = Ticket.objects.get(id=ticket_id)
            context = {'page_title': f'حذف تیکت با ایدی {ticket_id}'}
            if ticket.owner == request.user or ticket.receiver == request.user or request.user.is_superuser:
                message = 'با موفقیت حذف گردید'
                ticket.delete()
                return redirect(reverse(
                    'ticket:ticket-list-with-box-status'
                    , kwargs={'box_status': 'sent'}) + f'?message={message}')
            else:
                return render(request, '404.html')

        except Exception as e:
            print(e)
            return render(request, '404.html')

    @CheckLogin()
    def change_state(self, request, teaser_maker_id, *args, **kwargs):
        pass


class NotificationView:
    def __init__(self):
        super().__init__()

    @CheckLogin()
    def list(self, request, *args, **kwargs):
        context = {'page_title': 'اطلاعیه ها', 'get_params': request.GET.urlencode()}
        q = Q()
        if not request.user.is_superuser:
            q &= (
                Q(**{'user': request.user})
            )
        notifications = UserNotification.objects.filter(q).order_by('-created_at')
        context['notifications'] = notifications

        items_per_page = 50
        paginator = Paginator(notifications, items_per_page)
        page_number = request.GET.get('page')
        page = paginator.get_page(page_number)
        context['page'] = page

        return render(request, 'notifications/notification-list.html', context)

    @CheckLogin()
    def detail(self, request, notification_id, *args, **kwargs):
        try:
            user_notification = UserNotification.objects.get(id=notification_id)
            if user_notification.user != request.user:
                if not request.user.is_superuser:
                    return render(request, '404.html')
            context = {'page_title': f'جزئیات اطلاعیه با شماره *{user_notification.notification.id}*',
                       'user_notification': user_notification, 'get_params': request.GET.urlencode()}
            return render(request, 'notifications/notification-detail.html', context)
        except Exception as e:
            return render(request, '404.html')

    @CheckLogin()
    def filter(self, request, *args, **kwargs):
        pass

    @CheckLogin()
    @RequireMethod(allowed_method='POST')
    def create(self, request, *args, **kwargs):
        context = {'page_title': 'ساخت اطلاعیه جدید', 'get_params': request.GET.urlencode()}

        content = fetch_data_from_http_post(request, 'content', context)
        files = fetch_files_from_http_post_data(request, 'files', context)

        if not content:
            context['err'] = 'پیام اطلاعیه بدرستی وارد نشده است'
            return render(request, 'notifications/notification-list.html', context)

        new_notification = Notification.objects.create(
            content=content,
            created_by=request.user,
        )

        if files:
            for file in files:
                try:
                    new_file = FileGallery.objects.create(
                        alt=file.name,
                        file=file,
                        created_by=request.user,
                    )
                    new_notification.attachments.add(new_file)
                except:
                    pass
        SendNotificationThread(notification=new_notification).start()

        context['message'] = f'اطلاعیه با شماره {new_notification.id} ایجاد گردید'
        return redirect('ticket:notification-list')

    @CheckLogin()
    def change_state(self, request, notification_id, *args, **kwargs):
        try:
            notification = UserNotification.objects.get(id=notification_id)
            if notification.user != request.user:
                return JsonResponse({"notification_has_seen_by_user": 'false'})
            if not notification.has_seen_by_user:
                notification.has_seen_by_user = True
                notification_has_seen_by_user = 'true'
                notification.save()
            else:
                notification_has_seen_by_user = 'false'
            return JsonResponse({"notification_has_seen_by_user": notification_has_seen_by_user})
        except:
            return render(request, '404.html')


class SendNotificationThread(threading.Thread):
    def __init__(self, notification):
        super().__init__()
        self.notification = notification

    def run(self):
        for user in User.objects.all():
            try:
                UserNotification.objects.create(
                    user=user,
                    notification=self.notification,
                )
            except:
                pass


class MessageView:
    def __init__(self):
        super().__init__()

    @CheckLogin()
    def list(self, request, ticket_id, *args, **kwargs):
        q = Q()
        q &= Q(
            Q(**{'ticket__id': ticket_id})
        )
        if not request.user.is_superuser:
            q &= Q(
                Q(**{'ticket__owner': request.user}) |
                Q(**{'ticket__receiver': request.user})
            )

        messages = Message.objects.filter(q).order_by('created_at')

        serializer = MessageSerializer(messages, many=True)
        json_response_body = {
            "method": "post",
            "request": f"لیست پیام های تیکت با ایدی {ticket_id}",
            "result": "موفق",
            "data": serializer.data
        }
        return JsonResponse(json_response_body)

    @CheckLogin()
    def detail(self, request, message_id, *args, **kwargs):
        try:
            message = Message.objects.filter(id=message_id)
            if message.count() == 0:
                return render(request, '404.html')
            if not request.user.is_superuser:
                if message.ticket.belong_to != request.user:
                    return render(request, '404.html')
            serializer = MessageSerializer(message, many=True)

            json_response_body = {
                "method": "post",
                "request": f"محتوای پیام با ایدی {message_id}",
                "result": "موفق",
                "data": serializer.data
            }
            return JsonResponse(json_response_body)
        except Exception as e:
            return render(request, '404.html')

    @CheckLogin()
    def create(self, request, ticket_id, *args, **kwargs):
        try:
            q = Q()
            q &= Q(
                Q(**{'id': ticket_id})
            )
            if not request.user.is_superuser:
                q &= Q(
                    Q(**{'owner': request.user}) |
                    Q(**{'receiver': request.user})
                )
            ticket = Ticket.objects.get(q)

            context = {'page_title': f'ساخت پیام جدید ذیل تیکت {ticket_id}', 'get_params': request.GET.urlencode()}

            content = fetch_data_from_http_post(request, 'content', context)
            files = fetch_files_from_http_post_data(request, 'files', context)

            if not content:
                context['err'] = 'محتوا بدرستی وارد نشده است'
                return redirect('ticket:ticket-detail-with-id', ticket_id=ticket_id)

            owner = ticket.owner
            receiver = ticket.receiver

            new_message = Message.objects.create(
                ticket=ticket,
                content=content,
                created_by=request.user,
            )

            if files:
                for file in files:
                    new_file = FileGallery.objects.create(
                        alt=file.name,
                        file=file,
                        created_by=request.user,
                    )
                    new_message.attachments.add(new_file)

            if request.user == owner:
                ticket.has_seen_by_owner = True
                ticket.has_seen_by_receiver = False
                ticket.status = 'owner_response'
            elif request.user == receiver:
                ticket.has_seen_by_owner = False
                ticket.has_seen_by_receiver = True
                ticket.status = 'receiver_response'
            else:
                ticket.has_seen_by_owner = False
                ticket.has_seen_by_receiver = False
                ticket.status = 'admin_response'
            ticket.save()

            context['message'] = f'پیام با موفقیت ایجاد گردید'
            return redirect('ticket:ticket-detail-with-id', ticket_id=ticket_id)
        except Exception as e:
            print(e)
            return render(request, '404.html')
