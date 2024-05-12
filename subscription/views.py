import json

import jdatetime
import requests
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from accounts.models import Invoice, VIPPlan
from utilities.http_metod import fetch_data_from_http_post
from yekjamodir.settings import ZARINPAL_API_KEY, BASE_URL


class InvoiceView(View):
    def __init__(self):
        super().__init__()
        self.context = {'page_title': 'صورت حساب',
                        'navigation_icon_menu_id': 'pricing',
                        'navigation_menu_body_id': 'navigationSubscription',
                        'breadcrumb_1': 'خانه',
                        'breadcrumb_2': 'مالی',
                        }

    def get(self, request, invoice_id=None, *args, **kwargs):
        try:
            authority = request.GET('Authority')
            invoice = Invoice.objects.get(authority=authority)
            self.context['invoice'] = invoice
            if invoice.status == 'پرداخت شده':
                return redirect('accounts:invoice-with-id', invoice_id=invoice.id)
            try:
                url = 'https://api.zarinpal.com/pg/v4/payment/verify.json'
                header = {'Content-Type': 'application/json', 'accept': 'application/json'}
                data = {
                    "merchant_id": ZARINPAL_API_KEY,
                    "amount": invoice.amount * 10,
                    "authority": authority
                }
                response = requests.post(url=url, json=data, headers=header)
                result = response.json()
                try:
                    if int(result['data']['code']) == 100 or int(result['data']['code']) == 101:
                        ref_id = result['data']['ref_id']
                        invoice.status = 'پرداخت شده'
                        invoice.description = f'{result}'
                        invoice.ref_id = ref_id
                        invoice.save()
                        profile = invoice.user.profile_user
                        profile.vip_plan = invoice.vip_plan
                        now = jdatetime.datetime.now()
                        if profile.vip_plan_expiry_date > now:
                            profile.vip_plan_expiry_date += jdatetime.timedelta(days=invoice.vip_plan.expiry_days)
                        else:
                            profile.vip_plan_expiry_date = now + jdatetime.timedelta(
                                days=invoice.vip_plan.expiry_days)
                        profile.save()
                    else:
                        invoice.description = f'{result}'
                        invoice.save()
                except Exception as e:
                    invoice.description = f'{result}'
                    invoice.save()
            except Exception as e:
                invoice.description = 'اشکال در احراز پرداخت'
                invoice.save()
            return render(request, 'subscription/invoice.html', self.context)
        except:
            if request.user.is_authenticated:
                try:
                    invoice = Invoice.objects.get(id=invoice_id, user=request.user)
                    self.context['invoice'] = invoice
                    return render(request, 'subscription/invoice.html', self.context)
                except:
                    return render(request, '404.html')
            else:
                return redirect('accounts:login')

    def post(self, request, invoice_id=None, *args, **kwargs):
        if request.user.is_authenticated:
            vip_plan_id = fetch_data_from_http_post(request, 'vip_plan_id', self.context)
            vip_plan = VIPPlan.objects.get(id=vip_plan_id)
            new_invoice = Invoice.objects.create(
                user=request.user,
                vip_plan=vip_plan,
                amount=vip_plan.price,
                description='',
                authority='',
                ref_id='',
                status='پرداخت نشده',
                created_by=request.user,
            )
            self.context['invoice'] = new_invoice
            return render(request, 'subscription/invoice.html', self.context)
        else:
            return redirect('accounts:login')


class InvoiceList(View):
    def __init__(self):
        super().__init__()
        self.context = {'page_title': 'سوابق خرید',
                        'navigation_icon_menu_id': 'invoices-list',
                        'navigation_menu_body_id': 'navigationSubscription',
                        'breadcrumb_1': 'خانه',
                        'breadcrumb_2': 'مالی',
                        }

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return render(request, 'subscription/invoice.html', self.context)
        else:
            return redirect('accounts:login')

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return render(request, '404.html')
        else:
            return redirect('accounts:login')


class ChargeWalletView:
    def __init__(self):
        super().__init__()
        self.context = {'page_title': 'شارژ اعتبار حساب',
                        'breadcrumb_1': 'خانه',
                        'breadcrumb_2': 'مالی',}

    def charge_credit(self, request, *args, **kwargs):
        if request.method == 'GET':
            return render(request, 'subscription/charge-account.html', self.context)

        if request.method == 'POST':
            charge_amount = fetch_data_from_http_post(request, 'charge_amount', self.context)
            try:
                charge_amount = int(charge_amount)
                charge_amount_allowed_list = [55000, 110000, 220000, 330000, 550000, 1100000]
                if not charge_amount in charge_amount_allowed_list:
                    return JsonResponse({'message': 'not allowed'})
            except:
                return JsonResponse({'message': 'not allowed'})

            new_invoice = Invoice.objects.create(
                user=request.user,
                amount=charge_amount,
                description='شارژ اعتبار حساب',
                authority='',
                ref_id='',
                status='پرداخت نشده',
                created_by=request.user,
            )

            try:
                url = 'https://api.zarinpal.com/pg/v4/payment/request.json'
                header = {'Content-Type': 'application/json', 'accept': 'application/json'}
                data = {
                    "merchant_id": ZARINPAL_API_KEY,
                    "amount": new_invoice.amount * 10,
                    # "callback_url": f'{BASE_URL}{reverse("subscription:charge-wallet-callback")}',
                    "callback_url": f'http://127.0.0.1:8000{reverse("subscription:charge-wallet-callback")}',
                    "description": f"فاکتور پرداختی توسط {request.user.username}",
                    "metadata": {"mobile": request.user.username}
                }
                pay_request = requests.post(url=url, data=json.dumps(data), headers=header)
                if pay_request.status_code == 200:
                    authority = pay_request.json()['data']["authority"]
                    new_invoice.authority = authority
                    new_invoice.save()
                    return redirect(f'https://www.zarinpal.com/pg/StartPay/{new_invoice.authority}')
                else:
                    self.context['invoice'] = new_invoice
                    self.context['error'] = 'ارتباط با درگاه پرداخت زرین پال ممکن نیست'
                    return render(request, 'subscription/charge-account.html', self.context)
            except Exception as e:
                print(e)
                return render(request, '404.html', self.context)

    def charge_credit_callback(self, request, *args, **kwargs):
        try:
            print(1)
            authority = request.GET('Authority')
            invoice = Invoice.objects.get(authority=authority)
            self.context['invoice'] = invoice
            print(2)
            if invoice.status == 'پرداخت شده':
                return render(request, 'subscription/pay-result/pay-success.html', self.context)
            try:
                url = 'https://api.zarinpal.com/pg/v4/payment/verify.json'
                header = {'Content-Type': 'application/json', 'accept': 'application/json'}
                print(3)
                data = {
                    "merchant_id": ZARINPAL_API_KEY,
                    "amount": invoice.amount * 10,
                    "authority": authority
                }
                response = requests.post(url=url, json=data, headers=header)
                result = response.json()
                print(4)
                try:
                    if int(result['data']['code']) == 100 or int(result['data']['code']) == 101:
                        ref_id = result['data']['ref_id']
                        invoice.status = 'پرداخت شده'
                        invoice.description = f'{result}'
                        invoice.ref_id = ref_id
                        print(5)
                        invoice.save()
                        return render(request, 'subscription/pay-result/pay-success.html', self.context)
                    else:
                        invoice.description = f'{result}'
                        invoice.save()
                        self.context['error'] = f"{result['data']['code']}"
                        print(6)
                        return render(request, 'subscription/pay-result/pay-fail.html', self.context)
                except Exception as e:
                    print(7)
                    invoice.description = f'{result}'
                    invoice.save()
                    self.context['error'] = f'{result}'
                    return render(request, 'subscription/pay-result/pay-fail.html', self.context)
            except Exception as e:
                print(8)
                invoice.description = 'اشکال در احراز پرداخت'
                invoice.save()
                self.context['error'] = 'اشکال در احراز پرداخت'
                return render(request, 'subscription/pay-result/pay-fail.html', self.context)
        except Exception as e:
            print(e)
            return JsonResponse({'message': 'wrong argument'})
