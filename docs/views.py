# from django.http import JsonResponse
# from django.shortcuts import render
# from rest_framework.permissions import AllowAny
# from rest_framework.views import APIView
#
# from yekjamodir.settings import BASE_FRONT_URL
# from yekjamodir.settings import BASE_URL
#
#
# class Docs(APIView):
#     authentication_classes = ()
#     permission_classes = (AllowAny,)
#
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.context = {'detail': 'داکیومنت ها'}
#
#     def get(self, request, *args, **kwargs):
#         json_response_body = {
#             'راهنمایی استفاده از متد های REST': {
#                 'base': f'{BASE_URL}',
#
#                 'account/api/auth-simple/': {
#                     'درخواست': 'دریافت توکن با استفاده از نام کاربری و کلمه عبور',
#                     'GET': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                     'POST': {
#                         'توضیحات': 'از طریق این متد امکان دریافت توکن با استفاده از نام کاربری و کلمه عبور فراهم شده است',
#                         'سبک داده مورد پذیرش': 'json جیسون',
#                         'داده های ارسالی': {
#                             'username': 'نام کاربری',
#                             'password': 'کلمه عبور',
#                         },
#                         'داده بازگشتی در صورت موفقیت': {
#                             'method': 'post',
#                             'request': 'دریافت توکن',
#                             'result': 'موفق',
#                             'token': 'مقدار توکن',
#                             'message': 'مدت زمان اعتبار توکن',
#                         },
#                         'لیست خطا های احتمالی': {
#                             '1': 'ورودی صحیح نیست',
#                             '2': 'نام کاربری یا رمز عبور بدرستی ارسال نشده است',
#                             '3': 'نام کاربری خالی است',
#                             '4': 'کلمه عبور خالی است',
#                             '5': 'نام کاربری ارائه شده در سامانه موجود نیست',
#                             '6': 'رمز عبور صحیح نیست',
#                         }
#                     },
#                     'PUT': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                     'DELETE': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                 },
#                 'account/api/auth-sms-request/': {
#                     'درخواست': 'ارسال درخواست دریافت توکن از طریق شماره همراه',
#                     'GET': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                     'POST': {
#                         'توضیحات': 'از طریق این متد امکان ارسال درخواست دریافت توکن با استفاده از شماره همراه فراهم شده است',
#                         'سبک داده مورد پذیرش': 'json جیسون',
#                         'داده های ارسالی': {
#                             'phone_number': 'شماره همراه',
#                         },
#                         'داده بازگشتی در صورت موفقیت': {
#                             'method': 'post',
#                             'request': 'ارسال درخواست دریافت توکن با شماره همراه',
#                             'result': 'موفق',
#                             'message': 'کد تایید به شماره همراه پیامک شد',
#                         },
#                         'لیست خطا های احتمالی': {
#                             '1': 'ورودی صحیح نیست',
#                             '2': 'داده های ورودی کامل نیست یا بدرستی ارسال نشده است',
#                             '3': 'شماره همراه خالی است',
#                             '4': 'شماره همراه در سامانه یافت نشد',
#                             '5': 'ارسال درخواست مجدد پس از 120 ثانیه مجاز می باشد ',
#                         }
#                     },
#                     'PUT': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                     'DELETE': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                 },
#                 'account/api/auth-sms-validate/': {
#                     'درخواست': 'دریافت توکن با استفاده از شماره همراه و کد پیامکی',
#                     'GET': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                     'POST': {
#                         'توضیحات': 'از طریق این متد امکان دریافت توکن با استفاده از شماره همراه و کد پیامکی فراهم شده است',
#                         'سبک داده مورد پذیرش': 'json جیسون',
#                         'داده های ارسالی': {
#                             'phone_number': 'شماره همراه',
#                             'validate_code': 'کد پیامکی',
#                         },
#                         'داده بازگشتی در صورت موفقیت': {
#                             'method': 'post',
#                             'request': 'دریافت توکن',
#                             'result': 'موفق',
#                             'token': 'مقدار توکن',
#                             'message': 'مدت زمان اعتبار توکن',
#                         },
#                         'لیست خطا های احتمالی': {
#                             '1': 'ورودی صحیح نیست',
#                             '2': 'داده های ورودی کامل نیست یا بدرستی ارسال نشده است',
#                             '3': 'شماره همراه خالی است',
#                             '4': 'کد پیامکی خالی است',
#                             '5': 'شماره همراه ارائه شده در سامانه موجود نیست',
#                             '6': 'کد پیامکی اشتباه است',
#                             '7': 'کد پیامکی منقضی شده است',
#                         }
#                     },
#                     'PUT': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                     'DELETE': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                 },
#                 'account/api/auth-eliminate-all/': {
#                     'درخواست': 'ابطال توکن های فعال کاربر',
#                     'GET': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                     'POST': {
#                         'توضیحات': 'از طریق این متد امکان ابطال یکجا یا تکی توکن های کاربر فراهم شده است',
#                         'سبک داده مورد پذیرش': 'json جیسون',
#                         'داده های ارسالی': {
#                             'eliminate_all': 'true or false',
#                         },
#                         'داده بازگشتی در صورت موفقیت': {
#                             'method': 'post',
#                             'request': 'ابطال توکن',
#                             'result': 'موفق',
#                         },
#                         'لیست خطا های احتمالی': {
#                             '1': 'ورودی صحیح نیست',
#                             '2': 'ورودی صحیح نیست یا بدرستی ارسال نشده است',
#                             '3': 'نوع ابطال مشخص نشده است',
#                             '4': 'تنها عبارات true یا false برای نوع ابطال مجاز می باشد',
#
#                         }
#                     },
#                     'PUT': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                     'DELETE': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                 },
#                 'account/api/register/': {
#                     'درخواست': 'درخواست ثبت نام',
#                     'GET': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                     'POST': {
#                         'توضیحات': 'از طریق این متد امکان ارسال درخواست ثبت نام فراهم شده است',
#                         'سبک داده مورد پذیرش': 'json جیسون',
#                         'داده های ارسالی': {
#                             'phone_number': 'شماره همراه - (اجباری)',
#                             'password': 'کلمه عبور - (حداقل 8 کاراکتر - اجباری)',
#                             'full_name': 'نام و نام خانوادگی',
#                             'email': 'ایمیل',
#                             'birthday': 'تاریخ تولد (در قالب 1372/05/23)',
#                             'province': 'استان',
#                             'city': 'شهر',
#                             'address': 'ادرس',
#                             'zip_code': 'کد پستی',
#
#                         },
#                         'داده بازگشتی در صورت موفقیت': {
#                             'method': 'post',
#                             'request': 'درخواست ثبت نام',
#                             'result': 'موفق',
#                             'message': 'پیامک تایید به شماره همراه پیامک شد',
#                         },
#                         'لیست خطا های احتمالی': {
#                             '1': 'نام کاربری خالی است',
#                             '2': 'کلمه عبور خالی است',
#                             '3': 'تاریخ تولد ارسالی صحیح نیست',
#                             '4': 'کلمه عبور کمتر از 8 کاراکتر است',
#                             '5': 'اکانت مورد درخواست در سامانه ثبت شده است',
#                             '6': 'ارسال درخواست مجدد پس از 120 ثانیه',
#
#                         }
#                     },
#                     'PUT': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                     'DELETE': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                 },
#                 'account/api/register-confirm/': {
#                     'درخواست': 'درخواست تایید ثبت نام',
#                     'GET': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                     'POST': {
#                         'توضیحات': 'از طریق این متد امکان تایید ثبت نام کاربر فراهم شده است',
#                         'سبک داده مورد پذیرش': 'json جیسون',
#                         'داده های ارسالی': {
#                             'phone_number': 'شماره همراه',
#                             'verify_code': 'کد پیامکی',
#                         },
#                         'داده بازگشتی در صورت موفقیت': {
#                             'method': 'post',
#                             'request': 'درخواست تایید ثبت نام',
#                             'result': 'موفق',
#                             'token': 'توکن',
#                             'message': 'مدت زمان اعتبار توکن',
#                         },
#                         'لیست خطا های احتمالی': {
#                             '1': 'ورودی صحیح نیست',
#                             '2': 'ورودی صحیح نیست یا بدرستی ارسال نشده است',
#                             '3': 'شماره همراه خالی است',
#                             '4': 'کد پیامکی خالی است',
#                             '5': 'کد پیامکی منقضی شده است',
#                             '6': 'کد پیامکی صحیح نیست',
#                             '7': 'شماره همراه در سامانه موجود نیست',
#                             '8': 'درخواست ثبت نام ثبت نشده است',
#                         }
#                     },
#                     'PUT': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                     'DELETE': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                 },
#                 'account/api/account/': {
#                     'GET': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                     'POST': {
#                         'درخواست': 'دریافت جزئیات حساب کاربری',
#                         'توضیحات': 'از طریق این متد امکان دریافت جزئیات کامل حساب کاربری فراهم شده است',
#                         'سبک داده مورد پذیرش': 'json جیسون',
#                         'HTTP HEADER': {
#                             'Authorization': 'BatoboxToken xxx',
#                         },
#                         'داده های ارسالی': {
#                             '0': 'ندارد',
#                         },
#                         'داده بازگشتی در صورت موفقیت': {
#                             'method': 'post',
#                             'request': 'درخواست اطلاعات حساب',
#                             'result': 'موفق',
#                             'username': 'نام کاربری',
#                             'email': 'ایمیل',
#                             'mobile_phone_number': 'شماره موبایل',
#                             'landline': 'شماره ثابت',
#                             'birthday': 'تاریخ تولد',
#                             'province': 'استان',
#                             'city': 'شهر',
#                             'address': 'آدرس',
#                             'zip_code': 'کد پستی',
#                             'wallet_balance': 'اعتبار حساب',
#                             'like_list': 'لیست علاقه مندی ها',
#                             'wish_list': 'لیست ویش ها',
#                             'temp_card': 'سبد خرید موقت',
#                         },
#                         'لیست خطا های احتمالی': {
#                             '0': 'ندارد',
#                         }
#                     },
#                     'PUT': {
#                         'درخواست': 'ویرایش جزئیات حساب کاربری',
#                         'توضیحات': {
#                             '0': 'از طریق این متد امکان ویرایش اطلاعات حساب کاربری فراهم شده است',
#                             '1': 'از طریق این متد امکان تغییر اعتبار حساب وجود ندارد',
#                         },
#                         'سبک داده مورد پذیرش': 'json جیسون',
#                         'HTTP HEADER': {
#                             'Authorization': 'BatoboxToken xxx',
#                         },
#                         'داده های ارسالی - ارسال هر کدام به تنهایی مجاز می باشد': {
#                             'phone_number': 'شماره موبایل',
#                             'password': 'کلمه عبور',
#                             'email': 'ایمیل',
#                             'landline': 'شماره ثابت',
#                             'birthday': 'تاریخ تولد (در قالب 1372/05/23)',
#                             'province': 'استان',
#                             'city': 'شهر',
#                             'address': 'آدرس',
#                             'zip_code': 'کد پستی',
#                             'like_list': 'لیست علاقه مندی ها',
#                             'wish_list': 'لیست ویش ها',
#                             'temp_card': 'سبد خرید موقت',
#                         },
#                         'داده بازگشتی در صورت موفقیت': {
#                             'method': 'put',
#                             'request': 'درخواست ویرایش اطلاعات حساب',
#                             'result': 'موفق',
#                             'username': 'نام کاربری',
#                             'email': 'ایمیل',
#                             'mobile_phone_number': 'شماره موبایل',
#                             'landline': 'شماره ثابت',
#                             'birthday': 'تاریخ تولد',
#                             'province': 'استان',
#                             'city': 'شهر',
#                             'address': 'آدرس',
#                             'zip_code': 'کد پستی',
#                             'wallet_balance': 'اعتبار حساب',
#                             'like_list': 'لیست علاقه مندی ها',
#                             'wish_list': 'لیست ویش ها',
#                             'temp_card': 'سبد خرید موقت',
#                         },
#                         'لیست خطا های احتمالی': {
#                             '0': 'کلمه عبور خالی است',
#                             '1': 'کلمه عبور کمتر از 8 کاراکتر است',
#                             '2': 'تاریخ تولد ارسالی صحیح نیست',
#                         }
#                     },
#                     'DELETE': {
#                         'درخواست': 'حذف حساب کاربری',
#                         'توضیحات': 'از طریق این متد امکان حذف کامل حساب کاربری فراهم شده است',
#                         'سبک داده مورد پذیرش': 'json جیسون',
#                         'HTTP HEADER': {
#                             'Authorization': 'BatoboxToken xxx',
#                         },
#                         'داده های ارسالی': {
#                             '0': 'ندارد',
#                         },
#                         'داده بازگشتی در صورت موفقیت': {
#                             'method': 'delete',
#                             'request': 'حذف حساب کاربری',
#                             'result': 'موفق',
#                         },
#                         'لیست خطا های احتمالی': {
#                             '0': 'ندارد',
#                         }
#                     },
#                 },
#                 'account/api/wallet-charge/': {
#                     'GET': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                     'POST': {
#                         'درخواست': 'درخواست شارژ اعتبار حساب',
#                         'توضیحات': 'از طریق این متد امکان درخواست شارژ اعتبار حساب فراهم شده است',
#                         'سبک داده مورد پذیرش': 'json جیسون',
#                         'HTTP HEADER': {
#                             'Authorization': 'BatoboxToken xxx',
#                         },
#                         'داده های ارسالی': {
#                             'amount': 'مبلغ - تومان',
#                         },
#                         'داده بازگشتی در صورت موفقیت': {
#                             'method': 'post',
#                             'request': 'درخواست شارژ اعتبار حساب',
#                             'result': 'موفق',
#                             'order_detail': {
#                                 'products': 'شارژ اعتبار حساب',
#                                 'order_status': 'در حال بررسی',
#                                 'created_at': 'زمان ایجاد',
#                                 'updated_at': 'زمان بروزرسانی',
#                                 'created_by': 'ایجاد شده توسط',
#                                 'updated_by': 'بروز شده توسط',
#                             },
#                             'transaction_detail': {
#                                 'transaction_id': 'آیدی صورت حساب',
#                                 'payment_unique_code': 'کد یکتای پرداخت',
#                             }
#                         },
#                         'لیست خطا های احتمالی': {
#                             '1': 'ورودی صحیح نیست',
#                             '2': 'داده ورودی کامل ارسال نشده است',
#                             '3': 'ارتباط با درگاه پرداخت زرین پال ممکن نیست',
#                             '4': 'خطای بازگشتی از درگاه پرداخت زرین پال با کد xxx',
#                             '5': 'amount ارسالی با مقدار xxx صحیح نیست',
#                             '6': 'حداقل میزان شارژ اعتبار حساب 10 هزار تومان می باشد',
#                         }
#                     },
#                     'PUT': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                     'DELETE': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                 },
#                 'store/api/product-price-calculator/': {
#                     'GET': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                     'POST': {
#                         'درخواست': 'محاسبه قیمت محصول درخواستی',
#                         'توضیحات': {
#                             '0': 'از طریق این متد امکان محاسبه قیمت نهایی محصول درخواستی فراهم شده است',
#                             '1': 'جهت تضمین امنیت، درخواست به این api هر 200 ثانیه یک بار مجاز است',
#                             '2': 'ارسال تنها یکی از پارامتر های product_link یا amazon_asin مجاز است که می تواند مرتبط به آمازون باشد یا نباشد',
#                             '3': 'در صورتی که لینک یا asin ارسالی ارتباطی به امازون نداشته باشد بر اساس قیمت و وزن و ارز درخواستی کاربر محاسبات صورت می گیرد',
#                             '4': 'در صورتی که لینک یا asin ارسالی مربوط به آمازون باشد اما صحیح  نباشد یا در api موجود نباشد بر اساس قیمت و وزن و ارز درخواستی کاربر محاسبات صورت می گیرد و batobox_product_id ارائه نمی شود',
#                             '5': 'در صورتی که لینک یا asin ارسالی مربوط به آمازون بوده و صحیح باشد دریافت اطلاعات زمانبر بوده(15 ثانیه) و سپس محصول مرتبط درسایت باتوباکس ایجاد می شود که با batobox_product_id ارائه شده قابل دسترس است',
#                             '6': 'در صورتی که لینک یا asin ارسالی مربوط به آمازون بوده و صحیح باشد دریافت اطلاعات زمانبر بوده(15 ثانیه) و پس از دریافت، محسبات قیمت بر اساس ارز، وزن و قیمت دریافتی api صورت می گیرد نه موارد ارائه شده توسط کاربر',
#                             '7': 'در صورتی که لینک یا asin ارسالی مربوط به آمازون بوده و صحیح باشد دریافت اطلاعات زمانبر بوده(15 ثانیه) اما پس از دریافت یکی از پارامتر های ارز، وزن یا قیمت موجود نباشد محاسبات بر اساس قیمت و وزن و ارز درخواستی کاربر صورت می گیرد',
#                         },
#                         'سبک داده مورد پذیرش': 'json جیسون',
#                         'HTTP HEADER': {
#                             'Authorization': 'BatoboxToken xxx',
#                         },
#                         'داده های ارسالی': {
#                             'product_link': 'لینک محصول درخواستی',
#                             'amazon_asin': 'شناسه یکتای محصول آمازون',
#                             'currency_unique_code': 'کد یکتای ارز',
#                             'batobox_shipping_unique_code': 'کد یکتای حمل و نقل',
#                             'batobox_currency_exchange_unique_code': 'کد یکتای کمیسیون',
#                             'weight': 'وزن به واحد گرم',
#                             'price': 'قیمت مطابق با واحد درخواست شده',
#                             'description': 'توضیحات کاربر در خصوص محصول درخواستی',
#                         },
#                         'داده بازگشتی در صورت موفقیت': {
#                             'method': 'post',
#                             'request': 'محاسبه قیمت',
#                             'result': 'موفق',
#                             'product_detail': {
#                                 'requested_product_id': 'آیدی محصول درخواستی (افزودن به سبد خرید توسط این آیدی است)',
#                                 'link': 'شناسه asin یا لینک درخواستی کاربر',
#                                 'currency': {
#                                     'name': 'نام ارز',
#                                     'badge': 'نماد ارز',
#                                     'currency_equivalent_price_in_toman': 'قیمت واحد ارز به تومان',
#                                     'is_active': 'وضعیت',
#                                     'unique_code': 'کد یکتا',
#                                 },
#                                 'batobox_shipping': {
#                                     'currency': 'نماد ارز',
#                                     'weight_from': 'وزن از - واحد گرم',
#                                     'weight_to': 'وزن تا - واحد گرم',
#                                     'price': 'قیمت به واحد ارز',
#                                     'unique_code': 'کد یکتا',
#                                 },
#                                 'batobox_currency_exchange_commission': {
#                                     'currency': 'نماد ارز',
#                                     'price_from': 'قیمت از - به واحد ارز',
#                                     'price_to': 'قیمت تا - به واحد ارز',
#                                     'exchange_percentage': 'درصد کمیسیون',
#                                     'unique_code': 'کد یکتا',
#                                 },
#                                 'weight': 'وزن - گرم',
#                                 'description': 'توضیحات',
#                                 'product_price': 'قیمت محصول - به واحد ارز',
#                                 'batobox_shipping_price': 'هزینه حمل و نقل باتوباکس - به واحد ارز',
#                                 'final_price': 'قیمت نهایی - به واحد ارز',
#                                 'currency_equivalent_price_in_toman': 'قیمت واحد ارز به تومان',
#                                 'currency_exchange_percentage': 'کمیسیون تبدیل ارز - به درصد',
#                                 'final_price_in_toman': 'قیمت نهایی محصول - به تومان',
#
#                                 'batobox_product_id': 'شناسه محصول در باتوباکس',
#                             }
#                         },
#                         'لیست خطا های احتمالی': {
#                             '0': 'ورودی صحیح نیست (ارسال بر اساس جیسون نیست یا صحیح پیکر بندی نشده است)',
#                             '1': 'درخواست مجدد پس از گذشت 200 ثانیه امکان پذیر است',
#                             '2': 'ارسال یکی از پارامتر های amazon_asin یا product_link ضروری است',
#                             '3': 'ارسال پارامتر currency_unique_code ضروری است',
#                             '4': 'ارسال پارامتر batobox_shipping_unique_code ضروری است',
#                             '5': 'ارسال پارامتر batobox_currency_exchange_unique_code ضروری است',
#                             '6': 'ارسال تنها یکی از پارامتر های amazon_asin یا product_link مجاز است',
#                             '7': 'وزن بدرستی ارسال نشده است',
#                             '8': 'قیمت بدرستی ارسال نشده است',
#                             '9': 'ارسال نماد ارز برای محصولات غیر از آمازون ضروری است',
#                             '10': 'ارسال وزن برای محصولات غیر از آمازون ضروری است',
#                             '11': 'ارسال قیمت برای محصولات غیر از آمازون ضروری است',
#                             '12': 'ارتباط بر خط برای دریافت اطلاعات محصول ممکن نیست. ارسال نماد ارز برای محاسبه قیمت ضروری است',
#                             '13': 'ارتباط بر خط برای دریافت اطلاعات محصول ممکن نیست. ارسال وزن برای محاسبه قیمت ضروری است',
#                             '14': 'ارتباط بر خط برای دریافت اطلاعات محصول ممکن نیست. ارسال قیمت برای محاسبه قیمت نهایی ضروری است',
#                             '15': 'محصول آمازون یافت نشد. ارسال نماد ارز برای محاسبه قیمت ضروری است',
#                             '16': 'محصول آمازون یافت نشد. ارسال وزن برای محاسبه قیمت ضروری است',
#                             '17': 'محصول آمازون یافت نشد. ارسال قیمت برای محاسبه قیمت نهایی ضروری است',
#                             '18': 'not allowed متد غیر مجاز',
#                         }
#                     },
#                     'PUT': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                     'DELETE': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                 },
#                 'store/api/product/': {
#                     'GET': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                     'POST': {
#                         'درخواست': 'دریافت جزئیات محصول',
#                         'توضیحات': {
#                             '0': 'از طریق این متد امکان دریافت جزئیات محصول فراهم شده است',
#                             '1': 'ارسال product_id و amazon_product_asin محصول جهت دریافت اطلاعات ضروری است',
#                         },
#                         'سبک داده مورد پذیرش': 'json جیسون',
#                         'HTTP HEADER': {},
#                         'داده های ارسالی': {
#                             'product_id': 'آیدی محصول',
#                             'amazon_product_asin': 'شناسه محصول آمازون',
#                         },
#                         'داده بازگشتی نمونه در صورت موفقیت': {
#                             'id': '1',
#                             'asin': 'B09WW2589Z',
#                             'amazon_product_root_domain': 'amazon.ae',
#                             'product_root_url': 'https://www.amazon.ae/dp/B09WW2589Z?th=1&psc=1',
#                             'product_main_url': 'https://www.amazon.ae/Native-Projector-Cinema-Portable-Compatible/dp/B09WW2589Z',
#                             'product_type': 'product',
#                             'title_fa': 'بومی 1920 x 1080p پروژکتور Full HD Home Projector LED پروژکتور قابل حمل سازگار با Fire TV Stick ، PS4 ، HDMI ، VGA ، AV و USB',
#                             'title_en': 'Native 1920 x 1080P Projector Full HD Home Cinema Projector Led Portable Projector Compatible with Fire TV Stick,PS4, HDMI, VGA, AV and USB',
#                             'slug_title': 'PS4-HDMI-VGA-AV-USB',
#                             'description': 'Packed with a host of features, it scores high on the aspect of functionality. The fact that it ensures a seamless user-interface makes it worth the buy.',
#                             'brand': '通用',
#                             'product_brand_url': 'https://www.amazon.ae/s/ref=bl_dp_s_web_0?ie=UTF8&search-alias=aps&field-keywords=%E9%80%9A%E7%94%A8',
#                             'user_rating_count': '64',
#                             'rating_score': '4.1',
#                             'main_image': '/media/product-image/B09WW2589Z-main-image.jpg',
#                             'feature_bullets': 'Full hd native 1080p projectorthe gimisonic projector comes with native 1920x1080p with full hd resolution that provides clear color and crisp images for home theater and outdoor movie. Contrast ratio of 10000: 1 it will ...',
#                             'attributes': '[{"name": "Brand", "value": "\\u901a\\u7528"}, {"name": "Recommended uses for product", "value": "\\u5bb6\\u5ead\\u5f71\\u9662"}, {"name": "Special features", "value": "\\u5185\\u7f6e\\u626c\\u58f0\\u5668"}, {"name": "Connectivity technology", "value": "HDMI"}, {"name": "Display resolution", "value": "1920 x 1080"}]',
#                             'weight': '1280',
#                             'specifications': '[{"name": "Brand", "value": "\\u200e\\u901a\\u7528"}, {"name": "Product Dimensions", "value": "\\u200e19.8 x 15.5 x 7.5 cm; 1.28 Kilograms"}, {"name": "Manufacturer", "value": "\\u200eGIMISONIC"}, {"name": "Form Factor", "value": "\\u200ePortable"}, {"name": "Screen Resolution", "value": "\\u200e1920 x 1080"}, {"name": "Voltage", "value": "\\u200e240 Volts"}, {"name": "Wattage", "value": "\\u200e70 watts"}, {"name": "Item Weight", "value": "\\u200e1.28 Kilograms"}, {"name": "ASIN", "value": "B09WW2589Z"}, {"name": "Customer Reviews", "value": "4.1 4.1 out of 5 stars         64 ratings          4.1 out of 5 stars"}, {"name": "Best Sellers Rank", "value": "#4,853 in Electronics (See Top 100 in Electronics) #44 in Home Video Projectors"}, {"name": "Date First Available", "value": "30 March 2022"}, {"name": "Brand", "value": "\\u901a\\u7528"}, {"name": "Recommended uses for product", "value": "\\u5bb6\\u5ead\\u5f71\\u9662"}, {"name": "Special features", "value": "\\u5185\\u7f6e\\u626c\\u58f0\\u5668"}, {"name": "Connectivity technology", "value": "HDMI"}, {"name": "Display resolution", "value": "1920 x 1080"}]',
#                             'currency': 'AED',
#                             'base_price': '289',
#                             'shipping_price': '0',
#                             'total_price': '289',
#                             'is_product_available': 'true',
#                             'is_product_special': 'false',
#                             'created_at': "1402-09-10T13:07:34.766682",
#                             'updated_at': "1402-09-10T13:07:34.766682",
#                             'created_by': 2,
#                             'updated_by': 2,
#                             'categories': [],
#                             'keywords': [],
#                             'documents': {
#                                 '0': '18',
#                             },
#                             'images': {
#                                 '0': '25',
#                                 '1': '24',
#                                 '2': '23',
#                                 '3': '22',
#                                 '4': '21',
#                                 '5': '20',
#                                 '6': '19',
#                             },
#                         },
#                         'لیست خطا های احتمالی': {
#                             '0': 'ورودی صحیح نیست.',
#                             '1': 'داده ورودی کامل ارسال نشده است',
#                             '2': 'آیدی محصول خالی است',
#                             '3': 'شناسه محصول آمازون خالی است',
#                             '4': 'اطلاعات محصول آمازون با آیدی product_id و شناسه amazon_product_asin یافت نشد.',
#                         }
#                     },
#                     'PUT': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                     'DELETE': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                 },
#                 'store/api/product-list/': {
#                     'GET': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                     'POST': {
#                         'درخواست': 'دریافت لیست محصولات',
#                         'توضیحات': {
#                             '0': 'از طریق این متد امکان دریافت لیست محصولات بر اساس فیلتر های دلخواه فراهم شده است',
#                             '1': 'ارسال product_label ضروری و سایر فیلد ها اختیاری است',
#                             '2': 'در صورت ارسال date_range_from و date_range_to لیست محصولات در بازه تاریخ ارائه می شود',
#                             '3': 'ارسال تاریخ با فرمت مجاز مانند: 1402/10/05/14:00',
#                             '4': 'در صورت ارسال price_range_from و price_range_to لیست محصولات در بازه قیمت ارائه می شود',
#                             '5': 'در صورت ارسال score_range_from و score_range_to لیست محصولات در بازه امتیازی ارائه می شود',
#                             '6': 'در صورت ارسال category_words_list لیست محصولات با دسته های مشخص ارائه می شود',
#                             '7': 'در صورت ارسال keyword_words_list لیست محصولات با کلمات کلیدی مشخص ارائه می شود',
#                             '8': 'ارسال لیست با فرمت مجاز مانند: cat1,cat2,key1,key2,...',
#                             '9': 'در صورت ارسال brand لیست محصولات با برند مشخص ارائه می شود',
#                             '10': 'در صورت ارسال is_available لیست محصولات موجود ارائه می شود',
#                             '11': 'در صورت ارسال is_special لیست محصولات ویژه ارائه می شود',
#                             '12': 'ارسال is_available و is_special با فرمت مجاز مانند: true or false',
#                             '13': 'در صورت ارسال searched_word لیست محصولات شامل عبارت سرچ شده ارائه می شود',
#                         },
#                         'سبک داده مورد پذیرش': 'json جیسون',
#                         'HTTP HEADER': {},
#                         'داده های ارسالی نمونه': {
#                             'product_label': 'amazon',
#                             'date_range_from': '1402/10/05/14:00',
#                             'date_range_to': '1402/10/05/14:00',
#                             'price_range_from': '100',
#                             'price_range_to': '200',
#                             'score_range_from': '3',
#                             'score_range_to': '5',
#                             'category_words_list': 'cat1,cat2,...',
#                             'keyword_words_list': 'key1,key2,...',
#                             'brand': 'x',
#                             'is_available': 'true',
#                             'is_special': 'false',
#                             'searched_word': 'sample',
#                         },
#                         'داده بازگشتی نمونه در صورت موفقیت': {
#                             '0': {
#                                 'id': '1',
#                                 'asin': 'B09WW2589Z',
#                                 'title_fa': 'بومی 1920 x 1080p پروژکتور Full HD Home Projector LED پروژکتور قابل حمل سازگار با Fire TV Stick ، PS4 ، HDMI ، VGA ، AV و USB',
#                                 'title_en': 'Native 1920 x 1080P Projector Full HD Home Cinema Projector Led Portable Projector Compatible with Fire TV Stick,PS4, HDMI, VGA, AV and USB',
#                                 'slug_title': 'PS4-HDMI-VGA-AV-USB',
#                                 'description': 'Packed with a host of features, it scores high on the aspect of functionality. The fact that it ensures a seamless user-interface makes it worth the buy.',
#                                 'brand': '通用',
#                                 'main_image': '/media/product-image/B09WW2589Z-main-image.jpg',
#                                 'currency': 'AED',
#                                 'total_price': '289',
#                             },
#                             '1': {
#                                 'id': '1',
#                                 'asin': 'B09WW2589Z',
#                                 'title_fa': 'بومی 1920 x 1080p پروژکتور Full HD Home Projector LED پروژکتور قابل حمل سازگار با Fire TV Stick ، PS4 ، HDMI ، VGA ، AV و USB',
#                                 'title_en': 'Native 1920 x 1080P Projector Full HD Home Cinema Projector Led Portable Projector Compatible with Fire TV Stick,PS4, HDMI, VGA, AV and USB',
#                                 'slug_title': 'PS4-HDMI-VGA-AV-USB',
#                                 'description': 'Packed with a host of features, it scores high on the aspect of functionality. The fact that it ensures a seamless user-interface makes it worth the buy.',
#                                 'brand': '通用',
#                                 'main_image': '/media/product-image/B09WW2589Z-main-image.jpg',
#                                 'currency': 'AED',
#                                 'total_price': '289',
#                             },
#                             '2': {
#                                 'id': '1',
#                                 'asin': 'B09WW2589Z',
#                                 'title_fa': 'بومی 1920 x 1080p پروژکتور Full HD Home Projector LED پروژکتور قابل حمل سازگار با Fire TV Stick ، PS4 ، HDMI ، VGA ، AV و USB',
#                                 'title_en': 'Native 1920 x 1080P Projector Full HD Home Cinema Projector Led Portable Projector Compatible with Fire TV Stick,PS4, HDMI, VGA, AV and USB',
#                                 'slug_title': 'PS4-HDMI-VGA-AV-USB',
#                                 'description': 'Packed with a host of features, it scores high on the aspect of functionality. The fact that it ensures a seamless user-interface makes it worth the buy.',
#                                 'brand': '通用',
#                                 'main_image': '/media/product-image/B09WW2589Z-main-image.jpg',
#                                 'currency': 'AED',
#                                 'total_price': '289',
#                             }
#                         },
#                         'لیست خطا های احتمالی': {
#                             '0': 'ورودی صحیح نیست',
#                             '1': 'داده ورودی کامل ارسال نشده است',
#                             '2': 'در حال حاضر تنها محصولات آمازون بتوباکس پشتیبانی می شود',
#                         }
#                     },
#                     'PUT': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                     'DELETE': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                 },
#                 'store/api/product-list/?=page=1': {
#                     'GET': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                     'POST': {
#                         'درخواست': 'دریافت لیست محصولات با شماره صفحه',
#                         'توضیحات': {
#                             '0': 'منطبق با store/api/product-list/',
#                             '1': 'هر صفحه حاوی حداکثر 40 محصول است',
#                         },
#                         'داده بازگشتی': {
#                             "count": 40,
#                             "next": "https://api.example.org/accounts/?page=5",
#                             "previous": "https://api.example.org/accounts/?page=3",
#                             "results": 'منطبق با store/api/product-list/',
#                         }
#                     },
#                     'PUT': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                     'DELETE': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                 },
#                 'store/api/currency-list/': {
#                     'درخواست': 'دریافت لیست ارز',
#                     'GET': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                     'POST': {
#                         'توضیحات': 'از طریق این متد امکان دریافت لیست ارز فراهم شده است',
#                         'سبک داده مورد پذیرش': 'ندارد',
#                         'داده های ارسالی': 'ندارد',
#                         'داده بازگشتی در صورت موفقیت': {
#                             'method': 'post',
#                             'request': 'لیست ارز',
#                             'result': 'موفق',
#                             'data': {
#                                 '0': {
#                                     'id': 'آیدی',
#                                     'name': 'نام ارز',
#                                     'badge': 'نشان ارز',
#                                     'currency_equivalent_price_in_toman': 'قیمت واحد معادل ارز به تومان',
#                                     'is_active': 'فعال یا غیر فعال',
#                                     'unique_code': 'کد یکتا',
#                                 },
#                                 '1': {
#                                     'id': 'آیدی',
#                                     'name': 'نام ارز',
#                                     'badge': 'نشان ارز',
#                                     'currency_equivalent_price_in_toman': 'قیمت واحد معادل ارز به تومان',
#                                     'is_active': 'فعال یا غیر فعال',
#                                     'unique_code': 'کد یکتا',
#                                 },
#                                 '2': {
#                                     'id': 'آیدی',
#                                     'name': 'نام ارز',
#                                     'badge': 'نشان ارز',
#                                     'currency_equivalent_price_in_toman': 'قیمت واحد معادل ارز به تومان',
#                                     'is_active': 'فعال یا غیر فعال',
#                                     'unique_code': 'کد یکتا',
#                                 },
#                                 '3': '...'
#                             }
#                         },
#                         'لیست خطا های احتمالی': {
#                             '1': 'لیست ارز یافت نشد',
#                         }
#                     },
#                     'PUT': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                     'DELETE': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                 },
#                 'store/api/batobox-shipping-list/': {
#                     'درخواست': 'دریافت لیست هزینه های حمل و نقل',
#                     'GET': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                     'POST': {
#                         'توضیحات': 'از طریق این متد امکان دریافت لیست هزینه های حمل و نقل فراهم شده است',
#                         'سبک داده مورد پذیرش': 'ندارد',
#                         'داده های ارسالی': 'ندارد',
#                         'داده بازگشتی در صورت موفقیت': {
#                             'method': 'post',
#                             'request': 'لیست هزینه های حمل و نقل',
#                             'result': 'موفق',
#                             'data': {
#                                 '0': {
#                                     'id': 'آیدی',
#                                     'currency': 'نماد ارز',
#                                     'weight_from': 'وزن از - گرم',
#                                     'weight_to': 'وزن تا - گرم',
#                                     'price': 'قیمت به واحد ارز',
#                                     'unique_code': 'کد یکتا',
#                                 },
#                                 '1': {
#                                     'id': 'آیدی',
#                                     'currency': 'نماد ارز',
#                                     'weight_from': 'وزن از - گرم',
#                                     'weight_to': 'وزن تا - گرم',
#                                     'price': 'قیمت به واحد ارز',
#                                     'unique_code': 'کد یکتا',
#                                 },
#                                 '2': {
#                                     'id': 'آیدی',
#                                     'currency': 'نماد ارز',
#                                     'weight_from': 'وزن از - گرم',
#                                     'weight_to': 'وزن تا - گرم',
#                                     'price': 'قیمت به واحد ارز',
#                                     'unique_code': 'کد یکتا',
#                                 },
#                                 '3': '...'
#                             }
#
#                         },
#                         'لیست خطا های احتمالی': {
#                             '1': 'لیست هزینه های حمل و نقل',
#                         }
#                     },
#                     'PUT': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                     'DELETE': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                 },
#                 'store/api/batobox-currency-exchange-commission-list/': {
#                     'درخواست': 'دریافت لیست کمیسیون تبدیل ارز',
#                     'GET': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                     'POST': {
#                         'توضیحات': 'از طریق این متد امکان دریافت لیست کمیسیون تبدیل ارز فراهم شده است',
#                         'سبک داده مورد پذیرش': 'ندارد',
#                         'داده های ارسالی': 'ندارد',
#                         'داده بازگشتی در صورت موفقیت': {
#                             'method': 'post',
#                             'request': 'لیست کمیسیون تبدیل ارز',
#                             'result': 'موفق',
#                             'data': {
#                                 '0': {
#                                     'id': 'آیدی',
#                                     'currency': 'نماد ارز',
#                                     'price_from': 'قیمت از - به واحد ارز',
#                                     'price_to': 'قیمت تا - به واحد ارز',
#                                     'exchange_percentage': 'درصد کارمزد',
#                                     'unique_code': 'کد یکتا',
#                                 },
#                                 '1': {
#                                     'id': 'آیدی',
#                                     'currency': 'نماد ارز',
#                                     'price_from': 'قیمت از - به واحد ارز',
#                                     'price_to': 'قیمت تا - به واحد ارز',
#                                     'exchange_percentage': 'درصد کارمزد',
#                                     'unique_code': 'کد یکتا',
#                                 },
#                                 '2': {
#                                     'id': 'آیدی',
#                                     'currency': 'نماد ارز',
#                                     'price_from': 'قیمت از - به واحد ارز',
#                                     'price_to': 'قیمت تا - به واحد ارز',
#                                     'exchange_percentage': 'درصد کارمزد',
#                                     'unique_code': 'کد یکتا',
#                                 },
#                                 '3': '...'
#                             }
#
#                         },
#                         'لیست خطا های احتمالی': {
#                             '1': 'لیست کمیسیون تبدیل ارز یافت نشد',
#                         }
#                     },
#                     'PUT': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                     'DELETE': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                 },
#                 'store/api/categories/': {
#                     'درخواست': 'دریافت لیست دسته',
#                     'GET': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                     'POST': {
#                         'توضیحات': 'از طریق این متد امکان دریافت لیست دسته فراهم شده است',
#                         'سبک داده مورد پذیرش': 'ندارد',
#                         'داده های ارسالی': 'ندارد',
#                         'داده بازگشتی در صورت موفقیت': {
#                             'method': 'post',
#                             'request': 'لیست دسته',
#                             'result': 'موفق',
#                             'data': {
#                                 '0': {
#                                     'id': 'آیدی',
#                                     'parent': 'دسته مادر',
#                                     'parent_tree': 'یک رشته جیسون حاوی اطلاعات مادر های این دسته تا اخر',
#                                     'title_fa': 'عنوان فارسی',
#                                     'title_en': 'عنوان انگلیسی',
#                                     'title_slug': 'اسلاگ عنوان',
#                                     'cat_image': 'لینک تصویر دسته',
#                                 },
#                                 '1': {
#                                     'id': 'آیدی',
#                                     'parent': 'دسته مادر',
#                                     'parent_tree': 'یک رشته جیسون حاوی اطلاعات مادر های این دسته تا اخر',
#                                     'title_fa': 'عنوان فارسی',
#                                     'title_en': 'عنوان انگلیسی',
#                                     'title_slug': 'اسلاگ عنوان',
#                                     'cat_image': 'لینک تصویر دسته',
#                                 },
#                                 '2': {
#                                     'id': 'آیدی',
#                                     'parent': 'دسته مادر',
#                                     'parent_tree': 'یک رشته جیسون حاوی اطلاعات مادر های این دسته تا اخر',
#                                     'title_fa': 'عنوان فارسی',
#                                     'title_en': 'عنوان انگلیسی',
#                                     'title_slug': 'اسلاگ عنوان',
#                                     'cat_image': 'لینک تصویر دسته',
#                                 },
#                                 '3': '...'
#                             }
#                         },
#                         'لیست خطا های احتمالی': {
#                             '1': 'لیست دسته یافت نشد',
#                         }
#                     },
#                     'PUT': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                     'DELETE': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                 },
#                 'store/api/order/': {
#                     'درخواست': 'ثبت سفارش',
#                     'GET': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                     'POST': {
#                         'توضیحات': 'از طریق این متد امکان ثبت سفارش فراهم شده است',
#                         'HTTP HEADER': {
#                             'Authorization': 'BatoboxToken xxx',
#                         },
#                         'سبک داده مورد پذیرش': 'جیسون json',
#                         'داده های ارسالی': {
#                             'pay_type': 'wallet or direct',
#                             'requested_products_id_list': 'لیست آیدی های محصولات درخواستی'
#                         },
#                         'داده بازگشتی در صورت موفقیت': {
#                             'method': 'post',
#                             'request': 'ثبت سفارش',
#                             'result': 'موفق',
#                             'order_detail': {
#                                 'products': {
#                                     '0': {
#                                         'link': 'لینک محصول',
#                                         'currency': 'اطلاعات ارز',
#                                         'batobox_shipping': 'اطلاعات حمل و نقل',
#                                         'batobox_currency_exchange_commission': 'اطلاعات کمیسیون',
#                                         'weight': 'وزن به گرم',
#                                         'description': 'توضیحات کاربر',
#                                         'product_price': 'قیمت محصول به واحد ارز',
#                                         'batobox_shipping_price': 'قیمت حمل و نقل به واحد ارز',
#                                         'final_price': 'قیمت نهایی به واحد ارز',
#                                         'currency_equivalent_price_in_toman': 'قیمت واحد ارز به تومان',
#                                         'currency_exchange_percentage': 'درصد کمیسیون تبدیل ارز',
#                                         'final_price_in_toman': 'قیمت نهایی به تومان',
#                                         'created_at': 'تاریخ ایجاد',
#                                         'created_by': 'کاربر ثبت کننده',
#                                     },
#                                     '1': {
#                                         'link': 'لینک محصول',
#                                         'currency': 'اطلاعات ارز',
#                                         'batobox_shipping': 'اطلاعات حمل و نقل',
#                                         'batobox_currency_exchange_commission': 'اطلاعات کمیسیون',
#                                         'weight': 'وزن به گرم',
#                                         'description': 'توضیحات کاربر',
#                                         'product_price': 'قیمت محصول به واحد ارز',
#                                         'batobox_shipping_price': 'قیمت حمل و نقل به واحد ارز',
#                                         'final_price': 'قیمت نهایی به واحد ارز',
#                                         'currency_equivalent_price_in_toman': 'قیمت واحد ارز به تومان',
#                                         'currency_exchange_percentage': 'درصد کمیسیون تبدیل ارز',
#                                         'final_price_in_toman': 'قیمت نهایی به تومان',
#                                         'created_at': 'تاریخ ایجاد',
#                                         'created_by': 'کاربر ثبت کننده',
#                                     },
#                                     '2': {
#                                         'link': 'لینک محصول',
#                                         'currency': 'اطلاعات ارز',
#                                         'batobox_shipping': 'اطلاعات حمل و نقل',
#                                         'batobox_currency_exchange_commission': 'اطلاعات کمیسیون',
#                                         'weight': 'وزن به گرم',
#                                         'description': 'توضیحات کاربر',
#                                         'product_price': 'قیمت محصول به واحد ارز',
#                                         'batobox_shipping_price': 'قیمت حمل و نقل به واحد ارز',
#                                         'final_price': 'قیمت نهایی به واحد ارز',
#                                         'currency_equivalent_price_in_toman': 'قیمت واحد ارز به تومان',
#                                         'currency_exchange_percentage': 'درصد کمیسیون تبدیل ارز',
#                                         'final_price_in_toman': 'قیمت نهایی به تومان',
#                                         'created_at': 'تاریخ ایجاد',
#                                         'created_by': 'کاربر ثبت کننده',
#                                     },
#                                     '3': '...',
#                                 },
#                                 'order_status': 'وضعیت سفارش',
#                                 'created_at': 'زمان ثبت سفارش',
#                                 'updated_at': 'زمان بروزرسانی سفارش',
#                                 'created_by': 'ایجاد شده توسط',
#                                 'updated_by': 'بروز شده توسط',
#                             },
#                             'transaction_detail': {
#                                 'transaction_id': 'آیدی صورت حساب قابل پرداخت',
#                                 'payment_unique_code': 'کد یکتای پرداخت',
#                             }
#                         },
#                         'لیست خطا های احتمالی': {
#                             '1': 'ورودی صحیح نیست',
#                             '2': 'داده ورودی کامل ارسال نشده است',
#                             '3': 'ارتباط با درگاه پرداخت زرین پال ممکن نیست',
#                             '4': 'خطای بازگشتی از درگاه پرداخت زرینپال با کد 000',
#                             '5': 'محصول درخواستی با ایدی xxx یافت نشد',
#                             '6': 'محصول درخواستی با ایدی xxx منقضی شده است',
#                             '7': ' اعتبار حساب کافی نیست. مبلغ نهایی محصولات درخواستی برابر xxx تومان میباشد و اعتبار حساب برابر xxx تومان می باشد. معادل xxx تومان کسری اعتبار وجود دارد',
#                             '8': 'محصولی انتخاب نشده است',
#                         }
#                     },
#                     'PUT': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                     'DELETE': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                 },
#                 'store/api/request-pay/': {
#                     'درخواست': 'درخواست پرداخت',
#                     'GET': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                     'POST': {
#                         'توضیحات': 'از طریق این متد امکان درخواست پرداخت فراهم شده است',
#                         'HTTP HEADER': {
#                             'Authorization': 'BatoboxToken xxx',
#                         },
#                         'سبک داده مورد پذیرش': 'جیسون json',
#                         'داده های ارسالی': {
#                             'pay_type': 'wallet or direct',
#                             'payment_unique_code': 'کد یکتای تغییر اعتبار حساب',
#                             'transaction_id': 'آیدی صورت حساب'
#                         },
#                         'داده بازگشتی در صورت موفقیت': {
#                             'method': 'post',
#                             'request': 'درخواست پرداخت',
#                             'result': 'موفق',
#                             'transaction_detail': {
#                                 'need_pay': 'نیاز به پرداخت از طریق درگاه',
#                                 'message': 'پیام',
#                                 'payment_gate_link': 'لینک پرداخت',
#                             }
#                         },
#                         'لیست خطا های احتمالی': {
#                             '1': 'ورودی صحیح نیست',
#                             '2': 'داده ورودی کامل ارسال نشده است',
#                             '3': 'صورت حساب با ایدی xxx  وجود ندارد',
#                             '4': 'صورت حساب با ایدی xxx  منقضی شده است',
#                             '5': 'روش پرداخت با مقدار xxx پشتیبانی نمی شود',
#                             '6': 'مقدار payment_unique_code بدرستی ارسال نشده است',
#                             '7': 'payment_unique_code ارسالی با مقدار xxx وجود ندارد',
#                             '8': 'payment_unique_code ارسالی با مقدار xxx امکان پرداخت ندارد. مجدد ثبت درخواست نمایید',
#                             '9': 'payment_unique_code ارسالی با مقدار xxx استفاده شده است',
#                             '10': 'اعتبار حساب کافی نیست',
#                             '11': 'امکان شارژ حساب از طریق شارژ حساب وجود ندارد',
#                         }
#                     },
#                     'PUT': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                     'DELETE': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                 },
#                 'store/api/pay-confirm/': {
#                     'درخواست': 'درخواست تایید پرداخت',
#                     'GET': {
#                         'توضیحات': {
#                             '0': 'از طریق این متد امکان درخواست تایید پرداخت فراهم شده است',
#                             '1': 'این متد به عنوان ادرس بازگشتی از درگاه زرین پال بصورت خودکار فراخوانی می شود',
#                             '2': 'امکان فراخوانی این متد توسط کاربر وجود دارد',
#                             '3': 'پرداخت ها بلافاصله توسط این متد بررسی و اعمال می گردد',
#                             '4': 'این متد تنها یکبار قابلیت تایید پرداخت را به کاربر می دهد',
#                         },
#                         'سبک داده مورد پذیرش': 'ندارد',
#                         'داده های ارسالی': {
#                             'Authority': 'کد یکتای پرداخت',
#                             'Status': 'OK or NOK تایید یا عدم تایید پرداخت'
#                         },
#                         'ادرس انتقال نهایی کاربر': {
#                             'redirect_url': f'{BASE_FRONT_URL}',
#                         },
#                         'پارامتر های بازگشتی': {
#                             'tab': 'wallet',
#                             'status': 'ok or nok',
#                             'message': {
#                                 '0': 'not-valid-status',
#                                 '1': 'not-valid-authority',
#                                 '2': 'authority-not-found',
#                                 '3': 'authority-can-accept-once',
#                                 '4': 'authority-problem-request-pay-again',
#                                 '5': 'no-valid-authority-0',
#                                 '6': 'no-valid-authority-2',
#                                 '7': 'transaction-not-payed',
#                                 '8': 'zarinpal-verification-problem',
#                             },
#                             'ref-id': 'شماره سفارش',
#                         }
#                     },
#                     'POST': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                     'PUT': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                     'DELETE': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                 },
#                 'store/api/order-list/': {
#                     'درخواست': 'لیست سفارشات',
#                     'GET': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                     'POST': {
#                         'توضیحات': 'از طریق این متد امکان دریافت لیست سفارشات فراهم شده است',
#                         'HTTP HEADER': {
#                             'Authorization': 'BatoboxToken xxx',
#                         },
#                         'سبک داده مورد پذیرش': 'ندارد',
#                         'داده های ارسالی': 'ندارد',
#                         'داده بازگشتی در صورت موفقیت': {
#                             'method': 'post',
#                             'request': 'لیست سفارشات',
#                             'result': 'موفق',
#                             'data': {
#                                 '0': {
#                                     'products': {
#                                     '0': {
#                                         'link': 'لینک محصول',
#                                         'currency': 'اطلاعات ارز',
#                                         'batobox_shipping': 'اطلاعات حمل و نقل',
#                                         'batobox_currency_exchange_commission': 'اطلاعات کمیسیون',
#                                         'weight': 'وزن به گرم',
#                                         'description': 'توضیحات کاربر',
#                                         'product_price': 'قیمت محصول به واحد ارز',
#                                         'batobox_shipping_price': 'قیمت حمل و نقل به واحد ارز',
#                                         'final_price': 'قیمت نهایی به واحد ارز',
#                                         'currency_equivalent_price_in_toman': 'قیمت واحد ارز به تومان',
#                                         'currency_exchange_percentage': 'درصد کمیسیون تبدیل ارز',
#                                         'final_price_in_toman': 'قیمت نهایی به تومان',
#                                         'created_at': 'تاریخ ایجاد',
#                                         'created_by': 'کاربر ثبت کننده',
#                                     },
#                                     '1': {
#                                         'link': 'لینک محصول',
#                                         'currency': 'اطلاعات ارز',
#                                         'batobox_shipping': 'اطلاعات حمل و نقل',
#                                         'batobox_currency_exchange_commission': 'اطلاعات کمیسیون',
#                                         'weight': 'وزن به گرم',
#                                         'description': 'توضیحات کاربر',
#                                         'product_price': 'قیمت محصول به واحد ارز',
#                                         'batobox_shipping_price': 'قیمت حمل و نقل به واحد ارز',
#                                         'final_price': 'قیمت نهایی به واحد ارز',
#                                         'currency_equivalent_price_in_toman': 'قیمت واحد ارز به تومان',
#                                         'currency_exchange_percentage': 'درصد کمیسیون تبدیل ارز',
#                                         'final_price_in_toman': 'قیمت نهایی به تومان',
#                                         'created_at': 'تاریخ ایجاد',
#                                         'created_by': 'کاربر ثبت کننده',
#                                     },
#                                     '2': {
#                                         'link': 'لینک محصول',
#                                         'currency': 'اطلاعات ارز',
#                                         'batobox_shipping': 'اطلاعات حمل و نقل',
#                                         'batobox_currency_exchange_commission': 'اطلاعات کمیسیون',
#                                         'weight': 'وزن به گرم',
#                                         'description': 'توضیحات کاربر',
#                                         'product_price': 'قیمت محصول به واحد ارز',
#                                         'batobox_shipping_price': 'قیمت حمل و نقل به واحد ارز',
#                                         'final_price': 'قیمت نهایی به واحد ارز',
#                                         'currency_equivalent_price_in_toman': 'قیمت واحد ارز به تومان',
#                                         'currency_exchange_percentage': 'درصد کمیسیون تبدیل ارز',
#                                         'final_price_in_toman': 'قیمت نهایی به تومان',
#                                         'created_at': 'تاریخ ایجاد',
#                                         'created_by': 'کاربر ثبت کننده',
#                                     },
#                                     '3': '...',
#                                 },
#                                     'order_status': 'وضعیت سفارش',
#                                     'created_at': 'زمان ثبت سفارش',
#                                     'updated_at': 'زمان بروزرسانی سفارش',
#                                     'created_by': 'ایجاد شده توسط',
#                                     'updated_by': 'بروز شده توسط',
#                                 },
#                                 '1': {
#                                     'products': {
#                                     '0': {
#                                         'link': 'لینک محصول',
#                                         'currency': 'اطلاعات ارز',
#                                         'batobox_shipping': 'اطلاعات حمل و نقل',
#                                         'batobox_currency_exchange_commission': 'اطلاعات کمیسیون',
#                                         'weight': 'وزن به گرم',
#                                         'description': 'توضیحات کاربر',
#                                         'product_price': 'قیمت محصول به واحد ارز',
#                                         'batobox_shipping_price': 'قیمت حمل و نقل به واحد ارز',
#                                         'final_price': 'قیمت نهایی به واحد ارز',
#                                         'currency_equivalent_price_in_toman': 'قیمت واحد ارز به تومان',
#                                         'currency_exchange_percentage': 'درصد کمیسیون تبدیل ارز',
#                                         'final_price_in_toman': 'قیمت نهایی به تومان',
#                                         'created_at': 'تاریخ ایجاد',
#                                         'created_by': 'کاربر ثبت کننده',
#                                     },
#                                     '1': {
#                                         'link': 'لینک محصول',
#                                         'currency': 'اطلاعات ارز',
#                                         'batobox_shipping': 'اطلاعات حمل و نقل',
#                                         'batobox_currency_exchange_commission': 'اطلاعات کمیسیون',
#                                         'weight': 'وزن به گرم',
#                                         'description': 'توضیحات کاربر',
#                                         'product_price': 'قیمت محصول به واحد ارز',
#                                         'batobox_shipping_price': 'قیمت حمل و نقل به واحد ارز',
#                                         'final_price': 'قیمت نهایی به واحد ارز',
#                                         'currency_equivalent_price_in_toman': 'قیمت واحد ارز به تومان',
#                                         'currency_exchange_percentage': 'درصد کمیسیون تبدیل ارز',
#                                         'final_price_in_toman': 'قیمت نهایی به تومان',
#                                         'created_at': 'تاریخ ایجاد',
#                                         'created_by': 'کاربر ثبت کننده',
#                                     },
#                                     '2': {
#                                         'link': 'لینک محصول',
#                                         'currency': 'اطلاعات ارز',
#                                         'batobox_shipping': 'اطلاعات حمل و نقل',
#                                         'batobox_currency_exchange_commission': 'اطلاعات کمیسیون',
#                                         'weight': 'وزن به گرم',
#                                         'description': 'توضیحات کاربر',
#                                         'product_price': 'قیمت محصول به واحد ارز',
#                                         'batobox_shipping_price': 'قیمت حمل و نقل به واحد ارز',
#                                         'final_price': 'قیمت نهایی به واحد ارز',
#                                         'currency_equivalent_price_in_toman': 'قیمت واحد ارز به تومان',
#                                         'currency_exchange_percentage': 'درصد کمیسیون تبدیل ارز',
#                                         'final_price_in_toman': 'قیمت نهایی به تومان',
#                                         'created_at': 'تاریخ ایجاد',
#                                         'created_by': 'کاربر ثبت کننده',
#                                     },
#                                     '3': '...',
#                                 },
#                                     'order_status': 'وضعیت سفارش',
#                                     'created_at': 'زمان ثبت سفارش',
#                                     'updated_at': 'زمان بروزرسانی سفارش',
#                                     'created_by': 'ایجاد شده توسط',
#                                     'updated_by': 'بروز شده توسط',
#                                 },
#                                 '2': {
#                                     'products': {
#                                     '0': {
#                                         'link': 'لینک محصول',
#                                         'currency': 'اطلاعات ارز',
#                                         'batobox_shipping': 'اطلاعات حمل و نقل',
#                                         'batobox_currency_exchange_commission': 'اطلاعات کمیسیون',
#                                         'weight': 'وزن به گرم',
#                                         'description': 'توضیحات کاربر',
#                                         'product_price': 'قیمت محصول به واحد ارز',
#                                         'batobox_shipping_price': 'قیمت حمل و نقل به واحد ارز',
#                                         'final_price': 'قیمت نهایی به واحد ارز',
#                                         'currency_equivalent_price_in_toman': 'قیمت واحد ارز به تومان',
#                                         'currency_exchange_percentage': 'درصد کمیسیون تبدیل ارز',
#                                         'final_price_in_toman': 'قیمت نهایی به تومان',
#                                         'created_at': 'تاریخ ایجاد',
#                                         'created_by': 'کاربر ثبت کننده',
#                                     },
#                                     '1': {
#                                         'link': 'لینک محصول',
#                                         'currency': 'اطلاعات ارز',
#                                         'batobox_shipping': 'اطلاعات حمل و نقل',
#                                         'batobox_currency_exchange_commission': 'اطلاعات کمیسیون',
#                                         'weight': 'وزن به گرم',
#                                         'description': 'توضیحات کاربر',
#                                         'product_price': 'قیمت محصول به واحد ارز',
#                                         'batobox_shipping_price': 'قیمت حمل و نقل به واحد ارز',
#                                         'final_price': 'قیمت نهایی به واحد ارز',
#                                         'currency_equivalent_price_in_toman': 'قیمت واحد ارز به تومان',
#                                         'currency_exchange_percentage': 'درصد کمیسیون تبدیل ارز',
#                                         'final_price_in_toman': 'قیمت نهایی به تومان',
#                                         'created_at': 'تاریخ ایجاد',
#                                         'created_by': 'کاربر ثبت کننده',
#                                     },
#                                     '2': {
#                                         'link': 'لینک محصول',
#                                         'currency': 'اطلاعات ارز',
#                                         'batobox_shipping': 'اطلاعات حمل و نقل',
#                                         'batobox_currency_exchange_commission': 'اطلاعات کمیسیون',
#                                         'weight': 'وزن به گرم',
#                                         'description': 'توضیحات کاربر',
#                                         'product_price': 'قیمت محصول به واحد ارز',
#                                         'batobox_shipping_price': 'قیمت حمل و نقل به واحد ارز',
#                                         'final_price': 'قیمت نهایی به واحد ارز',
#                                         'currency_equivalent_price_in_toman': 'قیمت واحد ارز به تومان',
#                                         'currency_exchange_percentage': 'درصد کمیسیون تبدیل ارز',
#                                         'final_price_in_toman': 'قیمت نهایی به تومان',
#                                         'created_at': 'تاریخ ایجاد',
#                                         'created_by': 'کاربر ثبت کننده',
#                                     },
#                                     '3': '...',
#                                 },
#                                     'order_status': 'وضعیت سفارش',
#                                     'created_at': 'زمان ثبت سفارش',
#                                     'updated_at': 'زمان بروزرسانی سفارش',
#                                     'created_by': 'ایجاد شده توسط',
#                                     'updated_by': 'بروز شده توسط',
#                                 },
#                                 '3': '...'
#                             }
#                         },
#                         'لیست خطا های احتمالی': {
#                             '1': 'لیست سفارشات یافت نشد',
#                         }
#                     },
#                     'PUT': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                     'DELETE': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                 },
#                 'store/api/transaction-list/': {
#                     'درخواست': 'لیست صورت حساب',
#                     'GET': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                     'POST': {
#                         'توضیحات': 'از طریق این متد امکان دریافت لیست صورت حساب فراهم شده است',
#                         'HTTP HEADER': {
#                             'Authorization': 'BatoboxToken xxx',
#                         },
#                         'سبک داده مورد پذیرش': 'ندارد',
#                         'داده های ارسالی': 'ندارد',
#                         'داده بازگشتی در صورت موفقیت': {
#                             'method': 'post',
#                             'request': 'لیست هزینه های حمل و نقل',
#                             'result': 'موفق',
#                             'data': {
#                                 '0': {
#                                     'order_id': 'آیدی سفارش',
#                                     'amount': 'مبلغ به تومان',
#                                     'description': 'توضیحات',
#                                     'email': 'ایمیل',
#                                     'mobile': 'موبایل',
#                                     'authority': 'شناسه پرداخت',
#                                     'ref_id': 'شماره سفارش',
#                                     'status': 'وضعیت پرداخت',
#                                     'created_at': 'زمان ایجاد',
#                                     'updated_at': 'زمان بروزرسانی',
#                                 },
#                                 '1': {
#                                     'order_id': 'آیدی سفارش',
#                                     'amount': 'مبلغ به تومان',
#                                     'description': 'توضیحات',
#                                     'email': 'ایمیل',
#                                     'mobile': 'موبایل',
#                                     'authority': 'شناسه پرداخت',
#                                     'ref_id': 'شماره سفارش',
#                                     'status': 'وضعیت پرداخت',
#                                     'created_at': 'زمان ایجاد',
#                                     'updated_at': 'زمان بروزرسانی',
#                                 },
#                                 '2': {
#                                     'order_id': 'آیدی سفارش',
#                                     'amount': 'مبلغ به تومان',
#                                     'description': 'توضیحات',
#                                     'email': 'ایمیل',
#                                     'mobile': 'موبایل',
#                                     'authority': 'شناسه پرداخت',
#                                     'ref_id': 'شماره سفارش',
#                                     'status': 'وضعیت پرداخت',
#                                     'created_at': 'زمان ایجاد',
#                                     'updated_at': 'زمان بروزرسانی',
#                                 },
#                                 '3': '...'
#                             }
#
#                         },
#                         'لیست خطا های احتمالی': {
#                             '1': 'لیست صورت حساب یافت نشد',
#                         }
#                     },
#                     'PUT': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                     'DELETE': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                 },
#                 'website/api/banner-top-header/': {
#                     'درخواست': 'دریافت بنر های هدر',
#                     'GET': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                     'POST': {
#                         'توضیحات': 'از طریق این متد امکان دریافت بنر های هدر فراهم شده است',
#                         'سبک داده مورد پذیرش': 'ندارد',
#                         'داده های ارسالی': 'ندارد',
#                         'داده بازگشتی در صورت موفقیت': {
#                             'method': 'post',
#                             'request': 'بنر هدر',
#                             'result': 'موفق',
#                             'data': {
#                                 '0': {
#                                     'title': 'عنوان',
#                                     'link': 'لینک',
#                                     'link_text': 'متن لینک',
#                                     'image': 'لینک تصویر',
#                                     'title_color': 'رنگ عنوان',
#                                     'btn_text_color': 'رنگ متن دکمه',
#                                     'btn_color': 'رنگ دکمه',
#                                 },
#                                 '1': {
#                                     'title': 'عنوان',
#                                     'link': 'لینک',
#                                     'link_text': 'متن لینک',
#                                     'image': 'لینک تصویر',
#                                     'title_color': 'رنگ عنوان',
#                                     'btn_text_color': 'رنگ متن دکمه',
#                                     'btn_color': 'رنگ دکمه',
#                                 },
#                                 '2': {
#                                     'title': 'عنوان',
#                                     'link': 'لینک',
#                                     'link_text': 'متن لینک',
#                                     'image': 'لینک تصویر',
#                                     'title_color': 'رنگ عنوان',
#                                     'btn_text_color': 'رنگ متن دکمه',
#                                     'btn_color': 'رنگ دکمه',
#                                 },
#                                 '3': '...'
#                             }
#
#                         },
#                         'لیست خطا های احتمالی': {
#                             '1': 'بنر هدر یافت نشد',
#                         }
#                     },
#                     'PUT': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                     'DELETE': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                 },
#                 'website/api/banner-top-footer/': {
#                     'درخواست': 'دریافت بنر بالای فوتر',
#                     'GET': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                     'POST': {
#                         'توضیحات': 'از طریق این متد امکان دریافت بنر بالای فوتر فراهم شده است',
#                         'سبک داده مورد پذیرش': 'ندارد',
#                         'داده های ارسالی': 'ندارد',
#                         'داده بازگشتی در صورت موفقیت': {
#                             'method': 'post',
#                             'request': 'بنر بالای فوتر',
#                             'result': 'موفق',
#                             'data': {
#                                 '0': {
#                                     'link': 'لینک',
#                                     'image': 'لینک تصویر',
#                                 },
#                                 '1': {
#                                     'link': 'لینک',
#                                     'image': 'لینک تصویر',
#                                 },
#                                 '2': {
#                                     'link': 'لینک',
#                                     'image': 'لینک تصویر',
#                                 },
#                                 '3': '...'
#                             }
#
#                         },
#                         'لیست خطا های احتمالی': {
#                             '1': 'بنر بالای فوتر یافت نشد',
#                         }
#                     },
#                     'PUT': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                     'DELETE': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                 },
#                 'website/api/banner-middle-footer/': {
#                     'درخواست': 'دریافت بنر میانه فوتر',
#                     'GET': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                     'POST': {
#                         'توضیحات': 'از طریق این متد امکان دریافت بنر میانه فوتر فراهم شده است',
#                         'سبک داده مورد پذیرش': 'ندارد',
#                         'داده های ارسالی': 'ندارد',
#                         'داده بازگشتی در صورت موفقیت': {
#                             'method': 'post',
#                             'request': 'بنر میانه فوتر',
#                             'result': 'موفق',
#                             'data': {
#                                 '0': {
#                                     'link': 'لینک',
#                                     'image': 'لینک تصویر',
#                                 },
#                                 '1': {
#                                     'link': 'لینک',
#                                     'image': 'لینک تصویر',
#                                 },
#                                 '2': {
#                                     'link': 'لینک',
#                                     'image': 'لینک تصویر',
#                                 },
#                                 '3': '...'
#                             }
#
#                         },
#                         'لیست خطا های احتمالی': {
#                             '1': 'بنر میانه فوتر یافت نشد',
#                         }
#                     },
#                     'PUT': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                     'DELETE': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                 },
#                 'website/api/home-page-slider/': {
#                     'درخواست': 'دریافت اسلایدر صفحه اصلی',
#                     'GET': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                     'POST': {
#                         'توضیحات': 'از طریق این متد امکان دریافت اسلایدر صفحه اصلی فراهم شده است',
#                         'سبک داده مورد پذیرش': 'ندارد',
#                         'داده های ارسالی': 'ندارد',
#                         'داده بازگشتی در صورت موفقیت': {
#                             'method': 'post',
#                             'request': 'اسلایدر صفحه اصلی',
#                             'result': 'موفق',
#                             'data': {
#                                 '0': {
#                                     'title': 'عنوان',
#                                     'sub_title': 'زیر عنوان',
#                                     'description': 'توضیحات',
#                                     'link': 'لینک',
#                                     'link_text': 'متن لینک',
#                                     'image_desktop': 'لینک تصویر با ابعاد دسکتاپ',
#                                     'image_tablet': 'لینک تصویر با ابعاد تبلت',
#                                     'image_mobile': 'لینک تصویر با ابعاد موبایل',
#                                 },
#                                 '1': {
#                                     'title': 'عنوان',
#                                     'sub_title': 'زیر عنوان',
#                                     'description': 'توضیحات',
#                                     'link': 'لینک',
#                                     'link_text': 'متن لینک',
#                                     'image_desktop': 'لینک تصویر با ابعاد دسکتاپ',
#                                     'image_tablet': 'لینک تصویر با ابعاد تبلت',
#                                     'image_mobile': 'لینک تصویر با ابعاد موبایل',
#                                 },
#                                 '2': {
#                                     'title': 'عنوان',
#                                     'sub_title': 'زیر عنوان',
#                                     'description': 'توضیحات',
#                                     'link': 'لینک',
#                                     'link_text': 'متن لینک',
#                                     'image_desktop': 'لینک تصویر با ابعاد دسکتاپ',
#                                     'image_tablet': 'لینک تصویر با ابعاد تبلت',
#                                     'image_mobile': 'لینک تصویر با ابعاد موبایل',
#                                 },
#                                 '3': '...'
#                             }
#
#                         },
#                         'لیست خطا های احتمالی': {
#                             '1': 'اسلایدر صفحه اصلی یافت نشد',
#                         }
#                     },
#                     'PUT': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                     'DELETE': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                 },
#                 'website/api/why-us-reason/': {
#                     'درخواست': 'دریافت دلایل انتخاب ما',
#                     'GET': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                     'POST': {
#                         'توضیحات': 'از طریق این متد امکان دریافت دلایل انتخاب ما فراهم شده است',
#                         'سبک داده مورد پذیرش': 'ندارد',
#                         'داده های ارسالی': 'ندارد',
#                         'داده بازگشتی در صورت موفقیت': {
#                             'method': 'post',
#                             'request': 'دلایل انتخاب ما',
#                             'result': 'موفق',
#                             'data': {
#                                 '0': {
#                                     'reason': 'دلیل',
#                                     'description': 'توضیحات',
#                                     'image': 'لینک تصویر',
#                                 },
#                                 '1': {
#                                     'reason': 'دلیل',
#                                     'description': 'توضیحات',
#                                     'image': 'لینک تصویر',
#                                 },
#                                 '2': {
#                                     'reason': 'دلیل',
#                                     'description': 'توضیحات',
#                                     'image': 'لینک تصویر',
#                                 },
#                                 '3': '...'
#                             }
#
#                         },
#                         'لیست خطا های احتمالی': {
#                             '1': 'دلایل انتخاب ما یافت نشد',
#                         }
#                     },
#                     'PUT': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                     'DELETE': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                 },
#                 'website/api/frequently-asked-question/': {
#                     'درخواست': 'دریافت سوالات متداول',
#                     'GET': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                     'POST': {
#                         'توضیحات': 'از طریق این متد امکان دریافت سوالات متداول فراهم شده است',
#                         'سبک داده مورد پذیرش': 'ندارد',
#                         'داده های ارسالی': 'ندارد',
#                         'داده بازگشتی در صورت موفقیت': {
#                             'method': 'post',
#                             'request': 'سوالات متداول',
#                             'result': 'موفق',
#                             'data': {
#                                 '0': {
#                                     'question': 'سوال',
#                                     'answer': 'پاسخ',
#                                 },
#                                 '1': {
#                                     'question': 'سوال',
#                                     'answer': 'پاسخ',
#                                 },
#                                 '2': {
#                                     'question': 'سوال',
#                                     'answer': 'پاسخ',
#                                 },
#                                 '3': '...'
#                             }
#
#                         },
#                         'لیست خطا های احتمالی': {
#                             '1': 'سوالات متداول یافت نشد',
#                         }
#                     },
#                     'PUT': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                     'DELETE': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                 },
#                 'website/api/term-and-condition/': {
#                     'درخواست': 'دریافت شرایط و قوانین',
#                     'GET': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                     'POST': {
#                         'توضیحات': 'از طریق این متد امکان دریافت شرایط و قوانین فراهم شده است',
#                         'سبک داده مورد پذیرش': 'ندارد',
#                         'داده های ارسالی': 'ندارد',
#                         'داده بازگشتی در صورت موفقیت': {
#                             'method': 'post',
#                             'request': 'شرایط و قوانین',
#                             'result': 'موفق',
#                             'data': {
#                                 '0': {
#                                     'law': 'قانون',
#                                     'law_description': 'توضیحات',
#                                 },
#                                 '1': {
#                                     'law': 'قانون',
#                                     'law_description': 'توضیحات',
#                                 },
#                                 '2': {
#                                     'law': 'قانون',
#                                     'law_description': 'توضیحات',
#                                 },
#                                 '3': '...'
#                             }
#
#                         },
#                         'لیست خطا های احتمالی': {
#                             '1': 'شرایط و قوانین یافت نشد',
#                         }
#                     },
#                     'PUT': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                     'DELETE': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                 },
#                 'website/api/page-seo/': {
#                     'درخواست': 'دریافت جزئیات سئوی صفحات',
#                     'GET': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                     'POST': {
#                         'توضیحات': 'از طریق این متد امکان دریافت جزئیات سئوی صفحات فراهم شده است',
#                         'سبک داده مورد پذیرش': 'ندارد',
#                         'داده های ارسالی': 'ندارد',
#                         'داده بازگشتی در صورت موفقیت': {
#                             'method': 'post',
#                             'request': 'جزئیات سئوی صفحات',
#                             'result': 'موفق',
#                             'data': {
#                                 '0': {
#                                     'page': 'ادرس path صفحه',
#                                     'title': 'عنوان',
#                                     'keywords': 'کلمات کلیدی',
#                                     'description': 'توضیحات',
#                                     'canonical': 'کنونیکال',
#                                     'robots': 'دستورالعمل ربات',
#                                     'page_type': 'نوع صفحه',
#                                     'image': 'لینک تصویر صفحه',
#                                 },
#                                 '1': {
#                                     'page': 'ادرس path صفحه',
#                                     'title': 'عنوان',
#                                     'keywords': 'کلمات کلیدی',
#                                     'description': 'توضیحات',
#                                     'canonical': 'کنونیکال',
#                                     'robots': 'دستورالعمل ربات',
#                                     'page_type': 'نوع صفحه',
#                                     'image': 'لینک تصویر صفحه',
#                                 },
#                                 '2': {
#                                     'page': 'ادرس path صفحه',
#                                     'title': 'عنوان',
#                                     'keywords': 'کلمات کلیدی',
#                                     'description': 'توضیحات',
#                                     'canonical': 'کنونیکال',
#                                     'robots': 'دستورالعمل ربات',
#                                     'page_type': 'نوع صفحه',
#                                     'image': 'لینک تصویر صفحه',
#                                 },
#                                 '3': '...'
#                             }
#
#                         },
#                         'لیست خطا های احتمالی': {
#                             '1': 'جزئیات سئوی صفحات یافت نشد',
#                         }
#                     },
#                     'PUT': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                     'DELETE': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                 },
#                 'website/api/website/': {
#                     'درخواست': 'دریافت سایت ها',
#                     'GET': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                     'POST': {
#                         'توضیحات': 'از طریق این متد امکان دریافت سایت ها فراهم شده است',
#                         'سبک داده مورد پذیرش': 'ندارد',
#                         'داده های ارسالی': 'ندارد',
#                         'داده بازگشتی در صورت موفقیت': {
#                             'method': 'post',
#                             'request': 'سایت ها',
#                             'result': 'موفق',
#                             'data': {
#                                 '0': {
#                                     'site_type': 'متعلق به کشور ترکیه یا امارات یا ...',
#                                     'title': 'عنوان',
#                                     'description': 'توضیحات',
#                                     'image': 'لینک تصویر',
#                                     'link': 'لینک',
#                                 },
#                                 '1': {
#                                     'site_type': 'متعلق به کشور ترکیه یا امارات یا ...',
#                                     'title': 'عنوان',
#                                     'description': 'توضیحات',
#                                     'image': 'لینک تصویر',
#                                     'link': 'لینک',
#                                 },
#                                 '2': {
#                                     'site_type': 'متعلق به کشور ترکیه یا امارات یا ...',
#                                     'title': 'عنوان',
#                                     'description': 'توضیحات',
#                                     'image': 'لینک تصویر',
#                                     'link': 'لینک',
#                                 },
#                                 '3': '...'
#                             }
#
#                         },
#                         'لیست خطا های احتمالی': {
#                             '1': 'سایت ها یافت نشد',
#                         }
#                     },
#                     'PUT': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                     'DELETE': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                 },
#                 'website/api/brands/': {
#                     'درخواست': 'لیست برند',
#                     'GET': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                     'POST': {
#                         'توضیحات': 'از طریق این متد امکان دریافت لیست برند فراهم شده است',
#                         'سبک داده مورد پذیرش': 'ندارد',
#                         'داده های ارسالی': 'ندارد',
#                         'داده بازگشتی در صورت موفقیت': {
#                             'method': 'post',
#                             'request': 'لیست برند',
#                             'result': 'موفق',
#                             'data': {
#                                 '0': {
#                                     'title_fa': 'عنوان فارسی',
#                                     'title_en': 'عنوان انگلیسی',
#                                     'title_slug': 'اسلاگ عنوان',
#                                     'description': 'توضیحات',
#                                     'image': 'لینک تصویر',
#                                     'link': 'لینک',
#                                 },
#                                 '1': {
#                                     'title_fa': 'عنوان فارسی',
#                                     'title_en': 'عنوان انگلیسی',
#                                     'title_slug': 'اسلاگ عنوان',
#                                     'description': 'توضیحات',
#                                     'image': 'لینک تصویر',
#                                     'link': 'لینک',
#                                 },
#                                 '2': {
#                                     'title_fa': 'عنوان فارسی',
#                                     'title_en': 'عنوان انگلیسی',
#                                     'title_slug': 'اسلاگ عنوان',
#                                     'description': 'توضیحات',
#                                     'image': 'لینک تصویر',
#                                     'link': 'لینک',
#                                 },
#                                 '3': '...'
#                             }
#
#                         },
#                         'لیست خطا های احتمالی': {
#                             '1': 'لیست برند یافت نشد',
#                         }
#                     },
#                     'PUT': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                     'DELETE': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                 },
#                 'website/api/dynamic-data/': {
#                     'درخواست': 'دریافت داینامیک دیتا',
#                     'GET': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                     'POST': {
#                         'توضیحات': 'از طریق این متد امکان دریافت داینامیک دیتا فراهم شده است',
#                         'سبک داده مورد پذیرش': 'ندارد',
#                         'داده های ارسالی': 'ندارد',
#                         'داده بازگشتی در صورت موفقیت': {
#                             'method': 'post',
#                             'request': 'داینامیک دیتا',
#                             'result': 'موفق',
#                             'data': {
#                                 '0': {
#                                     'key': 'کلید',
#                                     'value': 'مقدار',
#                                 },
#                                 '1': {
#                                     'key': 'کلید',
#                                     'value': 'مقدار',
#                                 },
#                                 '2': {
#                                     'key': 'کلید',
#                                     'value': 'مقدار',
#                                 },
#                                 '3': '...'
#                             }
#
#                         },
#                         'لیست خطا های احتمالی': {
#                             '1': 'داینامیک دیتا یافت نشد',
#                         }
#                     },
#                     'PUT': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                     'DELETE': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                 },
#                 'ticket/api/new-ticket/': {
#                     'درخواست': 'ساخت تیکت',
#                     'GET': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                     'POST': {
#                         'توضیحات': 'از طریق این متد امکان ساخت تیکت فراهم شده است',
#                         'HTTP HEADER': {
#                             'Authorization': 'BatoboxToken xxx',
#                         },
#                         'سبک داده مورد پذیرش': 'جیسون json',
#                         'داده های ارسالی': {
#                             'ticket_title': 'عنوان تیکت',
#                         },
#                         'داده بازگشتی در صورت موفقیت': {
#                             'method': 'post',
#                             'request': 'ساخت تیکت',
#                             'result': 'موفق',
#                             'data': {
#                                 '0': {
#                                     'status': 'وضعیت',
#                                     'title': 'عنوان',
#                                     'created_at': 'زمان ایجاد',
#                                     'updated_at': 'زمان بروز رسانی',
#                                     'created_by': 'ساخته شده توسط',
#                                     'updated_by': 'بروز شده توسط',
#                                 },
#                                 '1': {
#                                     'status': 'وضعیت',
#                                     'title': 'عنوان',
#                                     'created_at': 'زمان ایجاد',
#                                     'updated_at': 'زمان بروز رسانی',
#                                     'created_by': 'ساخته شده توسط',
#                                     'updated_by': 'بروز شده توسط',
#                                 },
#                                 '2': {
#                                     'status': 'وضعیت',
#                                     'title': 'عنوان',
#                                     'created_at': 'زمان ایجاد',
#                                     'updated_at': 'زمان بروز رسانی',
#                                     'created_by': 'ساخته شده توسط',
#                                     'updated_by': 'بروز شده توسط',
#                                 },
#                                 '3': '...',
#                             }
#                         },
#                         'لیست خطا های احتمالی': {
#                             '1': 'ورودی صحیح نیست',
#                             '2': 'داده ورودی کامل ارسال نشده است',
#                             '3': 'عنوان تیکت بدرستی ارسال نشده است',
#                         }
#                     },
#                     'PUT': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                     'DELETE': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                 },
#                 'ticket/api/new-message/': {
#                     'درخواست': 'ساخت پیام تیکت',
#                     'GET': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                     'POST': {
#                         'توضیحات': 'از طریق این متد امکان ساخت پیام تیکت شده است',
#                         'HTTP HEADER': {
#                             'Authorization': 'BatoboxToken xxx',
#                         },
#                         'سبک داده مورد پذیرش': 'multipart/form-data',
#                         'داده های ارسالی': {
#                             'ticket_id': 'آیدی تیکت',
#                             'content': 'محتوای پیام',
#                             'attachments': 'لیست فایل های ارسالی',
#                         },
#                         'داده بازگشتی در صورت موفقیت': {
#                             'method': 'post',
#                             'request': 'ساخت پیام تیکت',
#                             'result': 'موفق',
#                             'data': {
#                                 '0': {
#                                     'ticket': 'آیدی تیکت',
#                                     'content': 'محتوای پیام',
#                                     'attachments': {
#                                         '0': 'file_url',
#                                         '1': 'file_url',
#                                         '2': 'file_url',
#                                         '3': '...',
#                                     },
#                                     'created_at': 'زمان ایجاد',
#                                     'created_by': 'ایجاد شده توسط',
#                                 },
#                                 '1': {
#                                     'ticket': 'آیدی تیکت',
#                                     'content': 'محتوای پیام',
#                                     'attachments': {
#                                         '0': 'file_url',
#                                         '1': 'file_url',
#                                         '2': 'file_url',
#                                         '3': '...',
#                                     },
#                                     'created_at': 'زمان ایجاد',
#                                     'created_by': 'ایجاد شده توسط',
#                                 },
#                                 '2': {
#                                     'ticket': 'آیدی تیکت',
#                                     'content': 'محتوای پیام',
#                                     'attachments': {
#                                         '0': 'file_url',
#                                         '1': 'file_url',
#                                         '2': 'file_url',
#                                         '3': '...',
#                                     },
#                                     'created_at': 'زمان ایجاد',
#                                     'created_by': 'ایجاد شده توسط',
#                                 },
#                                 '3': '...',
#                             }
#                         },
#                         'لیست خطا های احتمالی': {
#                             '1': 'تیکت با ایدی xxx یافت نشد یا دسترسی وجود ندارد',
#                             '2': 'content بدرستی ارسال نشده است',
#                             '3': 'ticket_id بدرستی ارسال نشده است',
#                         }
#                     },
#                     'PUT': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                     'DELETE': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                 },
#                 'ticket/api/ticket-list/': {
#                     'درخواست': 'لیست تیکت',
#                     'GET': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                     'POST': {
#                         'توضیحات': 'از طریق این متد امکان دریافت لیست تیکت فراهم شده است',
#                         'HTTP HEADER': {
#                             'Authorization': 'BatoboxToken xxx',
#                         },
#                         'سبک داده مورد پذیرش': 'ندارد',
#                         'داده های ارسالی': 'ندارد',
#                         'داده بازگشتی در صورت موفقیت': {
#                             'method': 'post',
#                             'request': 'لیست تیکت',
#                             'result': 'موفق',
#                             'data': {
#                                 '0': {
#                                     'status': 'وضعیت',
#                                     'title': 'عنوان',
#                                     'created_at': 'زمان ایجاد',
#                                     'updated_at': 'زمان بروز رسانی',
#                                     'created_by': 'ساخته شده توسط',
#                                     'updated_by': 'بروز شده توسط',
#                                 },
#                                 '1': {
#                                     'status': 'وضعیت',
#                                     'title': 'عنوان',
#                                     'created_at': 'زمان ایجاد',
#                                     'updated_at': 'زمان بروز رسانی',
#                                     'created_by': 'ساخته شده توسط',
#                                     'updated_by': 'بروز شده توسط',
#                                 },
#                                 '2': {
#                                     'status': 'وضعیت',
#                                     'title': 'عنوان',
#                                     'created_at': 'زمان ایجاد',
#                                     'updated_at': 'زمان بروز رسانی',
#                                     'created_by': 'ساخته شده توسط',
#                                     'updated_by': 'بروز شده توسط',
#                                 },
#                                 '3': '...',
#                             }
#                         },
#                         'لیست خطا های احتمالی': {
#                             '1': 'لیست تیکت یافت نشد',
#                         }
#                     },
#                     'PUT': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                     'DELETE': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                 },
#                 'ticket/api/message-list/': {
#                     'درخواست': 'لیست پیام های تیکت',
#                     'GET': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                     'POST': {
#                         'توضیحات': 'از طریق این متد امکان دریافت لیست پیام های تیکت فراهم شده است',
#                         'HTTP HEADER': {
#                             'Authorization': 'BatoboxToken xxx',
#                         },
#                         'سبک داده مورد پذیرش': 'جیسون json',
#                         'داده های ارسالی': {
#                             'ticket_id': 'آیدی تیکت',
#                         },
#                         'داده بازگشتی در صورت موفقیت': {
#                             'method': 'post',
#                             'request': 'لیست پیام های تیکت',
#                             'result': 'موفق',
#                             'data': {
#                                 '0': {
#                                     'ticket': 'آیدی تیکت',
#                                     'content': 'محتوای پیام',
#                                     'attachments': {
#                                         '0': 'file_url',
#                                         '1': 'file_url',
#                                         '2': 'file_url',
#                                         '3': '...',
#                                     },
#                                     'created_at': 'زمان ایجاد',
#                                     'created_by': 'ایجاد شده توسط',
#                                 },
#                                 '1': {
#                                     'ticket': 'آیدی تیکت',
#                                     'content': 'محتوای پیام',
#                                     'attachments': {
#                                         '0': 'file_url',
#                                         '1': 'file_url',
#                                         '2': 'file_url',
#                                         '3': '...',
#                                     },
#                                     'created_at': 'زمان ایجاد',
#                                     'created_by': 'ایجاد شده توسط',
#                                 },
#                                 '2': {
#                                     'ticket': 'آیدی تیکت',
#                                     'content': 'محتوای پیام',
#                                     'attachments': {
#                                         '0': 'file_url',
#                                         '1': 'file_url',
#                                         '2': 'file_url',
#                                         '3': '...',
#                                     },
#                                     'created_at': 'زمان ایجاد',
#                                     'created_by': 'ایجاد شده توسط',
#                                 },
#                                 '3': '...',
#                             }
#                         },
#                         'لیست خطا های احتمالی': {
#                             '1': 'ورودی صحیح نیست',
#                             '2': 'داده ورودی کامل ارسال نشده است',
#                             '3': 'تیکت با ایدی xxx یافت نشد یا دسترسی وجود ندارد',
#                         }
#                     },
#                     'PUT': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                     'DELETE': {
#                         'توضیحات': 'متد غیر مجاز',
#                     },
#                 },
#             }
#         }
#         return JsonResponse(json_response_body)
#
#     def post(self, request, *args, **kwargs):
#         return JsonResponse({'message': 'not allowed'})
#
#     def put(self, request, *args, **kwargs):
#         return JsonResponse({'message': 'not allowed'})
#
#     def delete(self, request, *args, **kwargs):
#         return JsonResponse({'message': 'not allowed'})
