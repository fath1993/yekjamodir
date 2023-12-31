# import json
# from django.http import JsonResponse
# from rest_framework.permissions import IsAuthenticated, AllowAny
# from rest_framework.views import APIView
# from rest_framework.authentication import SessionAuthentication
# from market.models import Keyword, Category, Shop, Product
# from jamiyat_group.custom_permission import CustomIsAuthenticated
#
# '''
# section market keyword
# '''
#
#
# class MarketKeywordSingle(APIView):
#     authentication_classes = (SessionAuthentication,)
#     permission_classes = (CustomIsAuthenticated,)
#
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.context = {}
#
#     def get(self, request, *args, **kwargs):
#         json_response_body = {
#             'request': 'جزئیات کلمه کلیدی',
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
#                     'توضیحات': 'از طریق این متد امکان بررسی جزئیات کلمه کلیدی فراهم شده است',
#                     'سبک داده مورد پذیرش': 'json جیسون',
#                     'داده های ارسالی': {
#                         'Keyword_id': 'آیدی کلمه کلیدی'
#                     },
#                     'خطا های احتمالی': {
#                         'فرمت ورودی صحیح نمی باشد': 'جیسون ارسالی شامل مقادیر از پیش مشخص شده نیست',
#                         'ناموفق. کلمه کلیدی با آیدی ارائه شده وجود ندارد': 'کلمه کلیدی با آیدی ارائه شده وجود ندارد',
#                     }
#                 },
#                 'PUT': {
#                     'توضیحات': 'از طریق این متد امکان ویرایش کلمه کلیدی فراهم شده است',
#                     'سبک داده مورد پذیرش': 'json جیسون',
#                     'داده های ارسالی': {
#                         'Keyword_id': 'آیدی کلمه کلیدی'
#                     },
#                     'خطا های احتمالی': {
#                         'فرمت ورودی صحیح نمی باشد': 'جیسون ارسالی شامل مقادیر از پیش مشخص شده نیست',
#                         'ناموفق. کلمه کلیدی با آیدی ارائه شده وجود ندارد': 'کلمه کلیدی با آیدی ارائه شده وجود ندارد',
#                     }
#                 },
#                 'DELETE': {
#                     'توضیحات': 'از طریق این متد امکان حذف کلمه کلیدی فراهم شده است',
#                     'سبک داده مورد پذیرش': 'json جیسون',
#                     'داده های ارسالی': {
#                         'Keyword_id': 'آیدی کلمه کلیدی'
#                     },
#                     'خطا های احتمالی': {
#                         'فرمت ورودی صحیح نمی باشد': 'جیسون ارسالی شامل مقادیر از پیش مشخص شده نیست',
#                         'ناموفق. کلمه کلیدی با آیدی ارائه شده وجود ندارد': 'کلمه کلیدی با آیدی ارائه شده وجود ندارد',
#                     }
#                 },
#             }
#         }
#         return JsonResponse(json_response_body)
#
#     def post(self, request, *args, **kwargs):
#         front_input = json.loads(request.body)
#         try:
#             Keyword_id = front_input['Keyword_id']
#             try:
#                 keyword = Keyword.objects.get(id=Keyword_id)
#                 json_response_body = {
#                     'method': 'post',
#                     'request': 'نمایش کلمه کلیدی',
#                     'result': 'موفق',
#                     'Keyword_id': Keyword_id,
#                     'Keyword type': keyword.Keyword_type,
#                     'name_fa': keyword.name_fa,
#                     'name_en': keyword.name_en,
#                 }
#             except:
#                 json_response_body = {
#                     'method': 'post',
#                     'request': 'نمایش کلمه کلیدی',
#                     'result': 'ناموفق. کلمه کلیدی با آیدی ارائه شده وجود ندارد',
#                     'Keyword_id': Keyword_id,
#                 }
#
#             return JsonResponse(json_response_body)
#         except:
#             json_response_body = {
#                 'method': 'post',
#                 'request': 'نمایش کلمه کلیدی',
#                 'result': 'ناموفق',
#                 'message': 'فرمت ورودی صحیح نمی باشد'
#             }
#             return JsonResponse(json_response_body)
#
#     def put(self, request, *args, **kwargs):
#         front_input = json.loads(request.body)
#         try:
#             Keyword_id = front_input['Keyword_id']
#             try:
#                 keyword = Keyword.objects.get(id=Keyword_id)
#                 try:
#                     Keyword_type = front_input['Keyword_type']
#                     keyword.Keyword_type = Keyword_type
#                     keyword.save()
#                 except:
#                     pass
#                 try:
#                     name_fa = front_input['name_fa']
#                     keyword.name_fa = name_fa
#                     keyword.save()
#                 except:
#                     pass
#                 try:
#                     name_en = front_input['name_en']
#                     keyword.name_en = name_en
#                     keyword.save()
#                 except:
#                     pass
#                 json_response_body = {
#                     'method': 'post',
#                     'request': 'ویرایش کلمه کلیدی',
#                     'result': 'کلمه کلیدی با موفقیت ویرایش شد',
#                     'Keyword id': Keyword_id,
#                     'Keyword type': keyword.Keyword_type,
#                     'name fa': keyword.name_fa,
#                     'name en': keyword.name_en,
#                 }
#                 return JsonResponse(json_response_body)
#             except:
#                 json_response_body = {
#                     'method': 'post',
#                     'request': 'ویرایش کلمه کلیدی',
#                     'result': 'ناموفق. کلمه کلیدی وجود ندارد',
#                     'Keyword_id': Keyword_id,
#                 }
#                 return JsonResponse(json_response_body)
#
#         except:
#             json_response_body = {
#                 'method': 'put',
#                 'request': 'ویرایش کلمه کلیدی',
#                 'result': 'ناموفق',
#                 'message': 'فرمت ورودی صحیح نمی باشد'
#             }
#             return JsonResponse(json_response_body)
#
#     def delete(self, request, *args, **kwargs):
#         front_input = json.loads(request.body)
#         try:
#             Keyword_id = front_input['Keyword_id']
#             try:
#                 keyword = Keyword.objects.get(id=Keyword_id)
#                 keyword.delete()
#                 json_response_body = {
#                     'method': 'post',
#                     'request': 'حذف کلمه کلیدی',
#                     'result': 'کلمه کلیدی با موفقیت حذف شد',
#                     'Keyword id': Keyword_id,
#                     'Keyword type': keyword.Keyword_type,
#                     'name fa': keyword.name_fa,
#                     'name en': keyword.name_en,
#                 }
#                 return JsonResponse(json_response_body)
#             except:
#                 json_response_body = {
#                     'method': 'post',
#                     'request': 'ویرایش کلمه کلیدی',
#                     'result': 'ناموفق. کلمه کلیدی وجود ندارد',
#                     'Keyword_id': Keyword_id,
#                 }
#                 return JsonResponse(json_response_body)
#
#         except:
#             json_response_body = {
#                 'method': 'put',
#                 'request': 'ویرایش کلمه کلیدی',
#                 'result': 'ناموفق',
#                 'message': 'فرمت ورودی صحیح نمی باشد'
#             }
#             return JsonResponse(json_response_body)
#
#     def head(self, request, *args, **kwargs):
#         json_response_body = {
#             'method': 'head',
#             'request': 'ویرایش کلمه کلیدی',
#             'result': 'ناموفق',
#             'message': 'متد مورد استفاده غیر مجاز می باشد'
#         }
#         return JsonResponse(json_response_body)
#
#     def options(self, request, *args, **kwargs):
#         json_response_body = {
#             'method': 'option',
#             'request': 'ویرایش کلمه کلیدی',
#             'result': 'ناموفق',
#             'message': 'متد مورد استفاده غیر مجاز می باشد'
#         }
#         return JsonResponse(json_response_body)
#
#     def patch(self, request, *args, **kwargs):
#         json_response_body = {
#             'method': 'patch',
#             'request': 'ویرایش کلمه کلیدی',
#             'result': 'ناموفق',
#             'message': 'متد مورد استفاده غیر مجاز می باشد'
#         }
#         return JsonResponse(json_response_body)
#
#
# class MarketKeywordList(APIView):
#     authentication_classes = (SessionAuthentication,)
#     permission_classes = (CustomIsAuthenticated,)
#
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.context = {}
#
#     def get(self, request, *args, **kwargs):
#         json_response_body = {
#             'request': 'لیست کلمات کلیدی',
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
#                     'توضیحات': 'از طریق این متد امکان دریافت لیست کلمات کلیدی فراهم شده است',
#                     'سبک داده مورد پذیرش': 'json جیسون',
#                     'داده های ارسالی': 'ندارد',
#                     'خطا های احتمالی': {
#                         'نامشخص': 'خطای سیستم',
#                     }
#                 },
#             }
#         }
#         return JsonResponse(json_response_body)
#
#     def post(self, request, *args, **kwargs):
#         json_response_body = {
#             'method': 'post',
#             'request': 'نمایش کلمات کلیدی',
#             'result': 'موفق',
#         }
#
#         try:
#             keywords = Keyword.objects.filter()
#             keyword_dict = {}
#             i = 0
#             for keyword in keywords:
#                 keyword_dict[i] = {
#                     'id': keyword.id,
#                     'Keyword type': keyword.Keyword_type,
#                     'name_fa': keyword.name_fa,
#                     'name_en': keyword.name_en,
#                 }
#                 i += 1
#             json_response_body['keywords'] = keyword_dict
#             return JsonResponse(json_response_body)
#         except Exception as e:
#             json_response_body['err'] = {
#                 'err message': str(e),
#             }
#             return JsonResponse(json_response_body)
#
#     def put(self, request, *args, **kwargs):
#         json_response_body = {
#             'method': 'put',
#             'request': 'افزودن کلمه کلیدی',
#             'result': 'ناموفق',
#             'message': 'متد مورد استفاده غیر مجاز می باشد'
#         }
#         self.context['json_response_body'] = json_response_body
#         return JsonResponse(self.context)
#
#     def delete(self, request, *args, **kwargs):
#         json_response_body = {
#             'method': 'delete',
#             'request': 'افزودن کلمه کلیدی',
#             'result': 'ناموفق',
#             'message': 'متد مورد استفاده غیر مجاز می باشد'
#         }
#         self.context['json_response_body'] = json_response_body
#         return JsonResponse(self.context)
#
#     def head(self, request, *args, **kwargs):
#         json_response_body = {
#             'method': 'head',
#             'request': 'افزودن کلمه کلیدی',
#             'result': 'ناموفق',
#             'message': 'متد مورد استفاده غیر مجاز می باشد'
#         }
#         self.context['json_response_body'] = json_response_body
#         return JsonResponse(self.context)
#
#     def options(self, request, *args, **kwargs):
#         json_response_body = {
#             'method': 'option',
#             'request': 'افزودن کلمه کلیدی',
#             'result': 'ناموفق',
#             'message': 'متد مورد استفاده غیر مجاز می باشد'
#         }
#         self.context['json_response_body'] = json_response_body
#         return JsonResponse(self.context)
#
#     def patch(self, request, *args, **kwargs):
#         json_response_body = {
#             'method': 'patch',
#             'request': 'افزودن کلمه کلیدی',
#             'result': 'ناموفق',
#             'message': 'متد مورد استفاده غیر مجاز می باشد'
#         }
#         self.context['json_response_body'] = json_response_body
#         return JsonResponse(self.context)
#
#
# class MarketKeywordNew(APIView):
#     authentication_classes = (SessionAuthentication,)
#     permission_classes = (CustomIsAuthenticated,)
#
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.context = {}
#
#     def get(self, request, *args, **kwargs):
#         json_response_body = {
#             'request': 'ایجاد کلمه کلیدی',
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
#                     'توضیحات': 'از طریق این متد امکان ساخت کلمه کلیدی فراهم شده است',
#                     'سبک داده مورد پذیرش': 'json جیسون',
#                     'داده های ارسالی': {
#                         'Keyword_type': 'محصول یا مارکت',
#                         'name_fa': 'نام دلخواه به فارسی',
#                         'name_en': 'نام دلخواه به انگلیسی'
#                     },
#                     'خطا های احتمالی': {
#                        'فرمت ورودی صحیح نمی باشد': 'مقادیر از پیش تعریف شده صحیح ارسال نشده است',
#                     }
#                 },
#             }
#         }
#         return JsonResponse(json_response_body)
#
#     def post(self, request, *args, **kwargs):
#         front_input = json.loads(request.body)
#         try:
#             Keyword_type = front_input['Keyword_type']
#             name_fa = front_input['name_fa']
#             name_en = front_input['name_en']
#             new_keyword = Keyword(
#                 Keyword_type=Keyword_type,
#                 name_fa=name_fa,
#                 name_en=name_en,
#                 created_by=request.user,
#             )
#             new_keyword.save()
#             json_response_body = {
#                 'method': 'post',
#                 'request': 'افزودن کلمه کلیدی',
#                 'result': 'کلمه کلیدی با موفقیت افزوده شد',
#                 'new keyword id': new_keyword.id,
#             }
#             return JsonResponse(json_response_body)
#         except:
#             json_response_body = {
#                 'method': 'post',
#                 'request': 'افزودن کلمه کلیدی',
#                 'result': 'ناموفق',
#                 'message': 'فرمت ورودی صحیح نمی باشد'
#             }
#             return JsonResponse(json_response_body)
#
#     def put(self, request, *args, **kwargs):
#         json_response_body = {
#             'method': 'put',
#             'request': 'ویرایش کلمه کلیدی',
#             'result': 'ناموفق',
#             'message': 'متد مورد استفاده غیر مجاز می باشد'
#         }
#         return JsonResponse(json_response_body)
#
#     def delete(self, request, *args, **kwargs):
#         json_response_body = {
#             'method': 'delete',
#             'request': 'حذف کلمه کلیدی',
#             'result': 'ناموفق',
#             'message': 'متد مورد استفاده غیر مجاز می باشد'
#         }
#         return JsonResponse(json_response_body)
#
#     def head(self, request, *args, **kwargs):
#         json_response_body = {
#             'method': 'head',
#             'request': 'افزودن کلمه کلیدی',
#             'result': 'ناموفق',
#             'message': 'متد مورد استفاده غیر مجاز می باشد'
#         }
#         self.context['json_response_body'] = json_response_body
#         return JsonResponse(self.context)
#
#     def options(self, request, *args, **kwargs):
#         json_response_body = {
#             'method': 'option',
#             'request': 'افزودن کلمه کلیدی',
#             'result': 'ناموفق',
#             'message': 'متد مورد استفاده غیر مجاز می باشد'
#         }
#         self.context['json_response_body'] = json_response_body
#         return JsonResponse(self.context)
#
#     def patch(self, request, *args, **kwargs):
#         json_response_body = {
#             'method': 'patch',
#             'request': 'افزودن کلمه کلیدی',
#             'result': 'ناموفق',
#             'message': 'متد مورد استفاده غیر مجاز می باشد'
#         }
#         self.context['json_response_body'] = json_response_body
#         return JsonResponse(self.context)
#
#
# '''
# section market keyword
# '''
#
#
# '''
# section market category
# '''
#
#
# class MarketCategorySingle(APIView):
#     authentication_classes = (SessionAuthentication,)
#     permission_classes = (CustomIsAuthenticated,)
#
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.context = {}
#
#     def get(self, request, *args, **kwargs):
#         json_response_body = {
#             'request': 'جزئیات دسته',
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
#                     'توضیحات': 'از طریق این متد امکان بررسی جزئیات دسته فراهم شده است',
#                     'سبک داده مورد پذیرش': 'json جیسون',
#                     'داده های ارسالی': {
#                         'category_id': 'آیدی دسته',
#                     },
#                     'خطا های احتمالی': {
#                         'فرمت ورودی صحیح نمی باشد': 'مقادیر از پیش تعریف شده صحیح ارسال نشده است',
#                         'ناموفق. دسته با آیدی ارائه شده وجود ندارد': 'ناموفق. دسته با آیدی ارائه شده وجود ندارد'
#                     }
#                 },
#                 'PUT': {
#                     'توضیحات': 'از طریق این متد امکان ویرایش دسته فراهم شده است',
#                     'سبک داده مورد پذیرش': 'json جیسون',
#                     'داده های ارسالی': {
#                         'category_id': 'آیدی دسته',
#                     },
#                     'خطا های احتمالی': {
#                         'فرمت ورودی صحیح نمی باشد': 'مقادیر از پیش تعریف شده صحیح ارسال نشده است',
#                         'ناموفق. دسته با آیدی ارائه شده وجود ندارد': 'ناموفق. دسته با آیدی ارائه شده وجود ندارد'
#                     }
#                 },
#                 'DELETE': {
#                     'توضیحات': 'از طریق این متد امکان حذف دسته فراهم شده است',
#                     'سبک داده مورد پذیرش': 'json جیسون',
#                     'داده های ارسالی': {
#                         'category_id': 'آیدی دسته',
#                     },
#                     'خطا های احتمالی': {
#                         'فرمت ورودی صحیح نمی باشد': 'مقادیر از پیش تعریف شده صحیح ارسال نشده است',
#                         'ناموفق. دسته با آیدی ارائه شده وجود ندارد': 'ناموفق. دسته با آیدی ارائه شده وجود ندارد'
#                     }
#                 },
#             }
#         }
#         return JsonResponse(json_response_body)
#
#     def post(self, request, *args, **kwargs):
#         front_input = json.loads(request.body)
#         try:
#             category_id = front_input['category_id']
#             try:
#                 category = Category.objects.get(id=category_id)
#                 json_response_body = {
#                     'method': 'post',
#                     'request': 'مشخصات دسته',
#                     'result': 'موفق',
#                     'category id': category_id,
#                     'category type': category.category_type,
#                     'keyword': {
#                         'Keyword id': category.keyword.id,
#                         'Keyword type': category.keyword.Keyword_type,
#                         'name fa': category.keyword.name_fa,
#                         'name en': category.keyword.name_en,
#                     },
#                     'priority': category.priority
#                 }
#             except:
#                 json_response_body = {
#                     'method': 'post',
#                     'request': 'مشخصات دسته',
#                     'result': 'ناموفق. دسته با آیدی ارائه شده وجود ندارد',
#                     'category id': category_id,
#                 }
#
#             return JsonResponse(json_response_body)
#         except:
#             json_response_body = {
#                 'method': 'post',
#                 'request': 'مشخصات دسته',
#                 'result': 'ناموفق',
#                 'message': 'فرمت ورودی صحیح نمی باشد'
#             }
#             return JsonResponse(json_response_body)
#
#     def put(self, request, *args, **kwargs):
#         front_input = json.loads(request.body)
#         try:
#             category_id = front_input['category_id']
#             try:
#                 category = Category.objects.get(id=category_id)
#                 try:
#                     category_type = front_input['category_type']
#                     category.category_type = category_type
#                     category.save()
#                 except:
#                     pass
#                 try:
#                     keyword_id = front_input['keyword_id']
#                     try:
#                         keyword = Keyword.objects.get(id=keyword_id)
#                         category.keyword = keyword
#                         category.save()
#                     except:
#                         json_response_body = {
#                             'method': 'post',
#                             'request': 'ویرایش کلمه کلیدی دسته',
#                             'result': 'ناموفق. کلمه کلیدی وجود ندارد',
#                             'keyword id': keyword_id,
#                         }
#                         return JsonResponse(json_response_body)
#                 except:
#                     pass
#                 try:
#                     priority = front_input['priority']
#                     category.priority = priority
#                     category.save()
#                 except:
#                     pass
#                 json_response_body = {
#                     'method': 'post',
#                     'request': 'ویرایش دسته',
#                     'result': 'موفق. دسته با موفقیت ویرایش شد',
#                     'keyword id': category_id,
#                 }
#                 return JsonResponse(json_response_body)
#             except:
#                 json_response_body = {
#                     'method': 'post',
#                     'request': 'ویرایش دسته',
#                     'result': 'ناموفق. دسته وجود ندارد',
#                     'category id': category_id,
#                 }
#
#                 return JsonResponse(json_response_body)
#         except:
#             json_response_body = {
#                 'method': 'post',
#                 'request': 'مشخصات دسته',
#                 'result': 'ناموفق',
#                 'message': 'فرمت ورودی صحیح نمی باشد'
#             }
#             return JsonResponse(json_response_body)
#
#     def delete(self, request, *args, **kwargs):
#         front_input = json.loads(request.body)
#         try:
#             category_id = front_input['category_id']
#             try:
#                 category = Category.objects.get(id=category_id)
#                 category.delete()
#                 json_response_body = {
#                     'method': 'post',
#                     'request': 'حذف دسته',
#                     'result': 'موفق. دسته با موفقیت حذف شد',
#                     'keyword id': category_id,
#                 }
#                 return JsonResponse(json_response_body)
#             except:
#                 json_response_body = {
#                     'method': 'post',
#                     'request': 'حذف دسته',
#                     'result': 'ناموفق. دسته وجود ندارد',
#                     'category id': category_id,
#                 }
#
#                 return JsonResponse(json_response_body)
#         except:
#             json_response_body = {
#                 'method': 'post',
#                 'request': 'حذف دسته',
#                 'result': 'ناموفق',
#                 'message': 'فرمت ورودی صحیح نمی باشد'
#             }
#             return JsonResponse(json_response_body)
#
#     def head(self, request, *args, **kwargs):
#         json_response_body = {
#             'method': 'head',
#             'request': 'ویرایش دسته',
#             'result': 'ناموفق',
#             'message': 'متد مورد استفاده غیر مجاز می باشد'
#         }
#         self.context['json_response_body'] = json_response_body
#         return JsonResponse(self.context)
#
#     def options(self, request, *args, **kwargs):
#         json_response_body = {
#             'method': 'option',
#             'request': 'ویرایش دسته',
#             'result': 'ناموفق',
#             'message': 'متد مورد استفاده غیر مجاز می باشد'
#         }
#         self.context['json_response_body'] = json_response_body
#         return JsonResponse(self.context)
#
#     def patch(self, request, *args, **kwargs):
#         json_response_body = {
#             'method': 'patch',
#             'request': 'ویرایش دسته',
#             'result': 'ناموفق',
#             'message': 'متد مورد استفاده غیر مجاز می باشد'
#         }
#         self.context['json_response_body'] = json_response_body
#         return JsonResponse(self.context)
#
#
# class MarketCategoryList(APIView):
#     authentication_classes = (SessionAuthentication,)
#     permission_classes = (CustomIsAuthenticated,)
#
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.context = {}
#
#     def get(self, request, *args, **kwargs):
#         json_response_body = {
#             'request': 'لیست دسته ها',
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
#                     'توضیحات': 'از طریق این متد امکان بررسی لیست دسته ها فراهم شده است',
#                     'سبک داده مورد پذیرش': 'json جیسون',
#                     'داده های ارسالی': 'ندارد',
#                     'خطا های احتمالی': {
#                         'نامشخص': 'خطای سیستم',
#                     }
#                 },
#             }
#         }
#         return JsonResponse(json_response_body)
#
#     def post(self, request, *args, **kwargs):
#         json_response_body = {
#             'method': 'post',
#             'request': 'لیست دسته ها',
#             'result': 'موفق',
#         }
#
#         try:
#             categories = Category.objects.filter()
#             category_dict = {}
#             i = 0
#             for category in categories:
#                 category_dict[i] = {
#                     'id': category.id,
#                     'category type': category.category_type,
#                     'keyword': {
#                         'keyword id': category.keyword.id,
#                         'Keyword_type': category.keyword.Keyword_type,
#                         'name_fa': category.keyword.name_fa,
#                         'name_en': category.keyword.name_en,
#                     }
#                 }
#                 i += 1
#             json_response_body['categories'] = category_dict
#             return JsonResponse(json_response_body)
#         except Exception as e:
#             json_response_body['err'] = {
#                 'err message': str(e),
#             }
#             return JsonResponse(json_response_body)
#
#     def put(self, request, *args, **kwargs):
#         json_response_body = {
#             'method': 'put',
#             'request': 'لیست دسته ها',
#             'result': 'ناموفق',
#             'message': 'متد مورد استفاده غیر مجاز می باشد'
#         }
#         self.context['json_response_body'] = json_response_body
#         return JsonResponse(self.context)
#
#     def delete(self, request, *args, **kwargs):
#         json_response_body = {
#             'method': 'delete',
#             'request': 'لیست دسته ها',
#             'result': 'ناموفق',
#             'message': 'متد مورد استفاده غیر مجاز می باشد'
#         }
#         self.context['json_response_body'] = json_response_body
#         return JsonResponse(self.context)
#
#     def head(self, request, *args, **kwargs):
#         json_response_body = {
#             'method': 'head',
#             'request': 'لیست دسته ها',
#             'result': 'ناموفق',
#             'message': 'متد مورد استفاده غیر مجاز می باشد'
#         }
#         self.context['json_response_body'] = json_response_body
#         return JsonResponse(self.context)
#
#     def options(self, request, *args, **kwargs):
#         json_response_body = {
#             'method': 'option',
#             'request': 'لیست دسته ها',
#             'result': 'ناموفق',
#             'message': 'متد مورد استفاده غیر مجاز می باشد'
#         }
#         self.context['json_response_body'] = json_response_body
#         return JsonResponse(self.context)
#
#     def patch(self, request, *args, **kwargs):
#         json_response_body = {
#             'method': 'patch',
#             'request': 'لیست دسته ها',
#             'result': 'ناموفق',
#             'message': 'متد مورد استفاده غیر مجاز می باشد'
#         }
#         self.context['json_response_body'] = json_response_body
#         return JsonResponse(self.context)
#
#
# class MarketCategoryNew(APIView):
#     authentication_classes = (SessionAuthentication,)
#     permission_classes = (CustomIsAuthenticated,)
#
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.context = {}
#
#     def get(self, request, *args, **kwargs):
#         json_response_body = {
#             'request': 'ساخت دسته',
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
#                     'توضیحات': 'از طریق این متد امکان ساخت دسته فراهم شده است',
#                     'سبک داده مورد پذیرش': 'json جیسون',
#                     'داده های ارسالی': {
#                         'category_type': 'محصول یا مارکت',
#                         'keyword_id': 1
#                     },
#                     'خطا های احتمالی': {
#                         'فرمت ورودی صحیح نمی باشد': 'داده های ارسالی کامل نیست',
#                         'ناموفق.  دسته از قبل وجود دارد': 'دسته از قبل وجود دارد'
#                     }
#                 },
#             }
#         }
#         return JsonResponse(json_response_body)
#
#     def post(self, request, *args, **kwargs):
#         front_input = json.loads(request.body)
#         try:
#             category_type = front_input['category_type']
#             keyword_id = front_input['keyword_id']
#             try:
#                 keyword = Keyword.objects.get(id=keyword_id)
#             except:
#                 json_response_body = {
#                     'method': 'post',
#                     'request': 'افزودن دسته',
#                     'result': 'ناموفق.  کلمه کلیدی وجود ندارد',
#                     'Keyword id': keyword_id,
#                 }
#                 return JsonResponse(json_response_body)
#             priority = front_input['priority']
#             try:
#                 new_category = Category(
#                     category_type=category_type,
#                     keyword=keyword,
#                     priority=priority,
#                     created_by=request.user,
#                 )
#                 new_category.save()
#             except:
#                 category = Category.objects.get(keyword=keyword)
#                 json_response_body = {
#                     'method': 'post',
#                     'request': 'افزودن دسته',
#                     'result': 'ناموفق.  دسته از قبل وجود دارد',
#                     'category': {
#                         'category id': category.id,
#                         'category created by': request.user.username,
#                         'category type': category.category_type,
#                         'category keyword': {
#                             'Keyword id': category.keyword.id,
#                             'Keyword type': category.keyword.Keyword_type,
#                             'name fa': category.keyword.name_fa,
#                             'name en': category.keyword.name_en,
#                         },
#                         'catgory  priority': category.priority,
#                     }
#                 }
#                 return JsonResponse(json_response_body)
#
#             json_response_body = {
#                 'method': 'post',
#                 'request': 'افزودن دسته',
#                 'result': 'دسته با موفقیت افزوده شد',
#                 'new category id': new_category.id,
#             }
#             return JsonResponse(json_response_body)
#         except Exception as e:
#             print(str(e))
#             json_response_body = {
#                 'method': 'post',
#                 'request': 'افزودن دسته',
#                 'result': 'ناموفق',
#                 'message': 'فرمت ورودی صحیح نمی باشد'
#             }
#             return JsonResponse(json_response_body)
#
#     def put(self, request, *args, **kwargs):
#         json_response_body = {
#             'method': 'put',
#             'request': 'ویرایش دسته',
#             'result': 'ناموفق',
#             'message': 'متد مورد استفاده غیر مجاز می باشد'
#         }
#         return JsonResponse(json_response_body)
#
#     def delete(self, request, *args, **kwargs):
#         json_response_body = {
#             'method': 'delete',
#             'request': 'حذف دسته',
#             'result': 'ناموفق',
#             'message': 'متد مورد استفاده غیر مجاز می باشد'
#         }
#         return JsonResponse(json_response_body)
#
#     def head(self, request, *args, **kwargs):
#         json_response_body = {
#             'method': 'head',
#             'request': 'ویرایش دسته',
#             'result': 'ناموفق',
#             'message': 'متد مورد استفاده غیر مجاز می باشد'
#         }
#         return JsonResponse(json_response_body)
#
#     def options(self, request, *args, **kwargs):
#         json_response_body = {
#             'method': 'options',
#             'request': 'ویرایش دسته',
#             'result': 'ناموفق',
#             'message': 'متد مورد استفاده غیر مجاز می باشد'
#         }
#         return JsonResponse(json_response_body)
#
#     def patch(self, request, *args, **kwargs):
#         json_response_body = {
#             'method': 'patch',
#             'request': 'ویرایش دسته',
#             'result': 'ناموفق',
#             'message': 'متد مورد استفاده غیر مجاز می باشد'
#         }
#         return JsonResponse(json_response_body)
#
#
# '''
# section market category
# '''
#
#
# '''
# section market shop
# '''
#
#
# class MarketShopSingle(APIView):
#     authentication_classes = (SessionAuthentication,)
#     permission_classes = (CustomIsAuthenticated,)
#
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.context = {}
#
#     def get(self, request, *args, **kwargs):
#         json_response_body = {
#             'request': 'جزئیات فروشگاه',
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
#                     'توضیحات': 'از طریق این متد امکان دریافت جزئیات فروشگاه فراهم شده است',
#                     'سبک داده مورد پذیرش': 'json جیسون',
#                     'داده های ارسالی': {
#                         'shop_id': 'آیدی فروشگاه',
#                     },
#                     'خطا های احتمالی': {
#                         'فرمت ورودی صحیح نمی باشد': 'داده های ارسالی کامل نیست',
#                         'ناموفق. فروشگاه با آیدی ارائه شده وجود ندارد': 'فروشگاه با آیدی ارائه شده وجود ندارد'
#                     }
#                 },
#                 'PUT': {
#                     'توضیحات': 'از طریق این متد امکان ویرایش فروشگاه فراهم شده است',
#                     'سبک داده مورد پذیرش': 'json جیسون',
#                     'داده های ارسالی': {
#                         'shop_id': 'آیدی فروشگاه',
#                     },
#                     'خطا های احتمالی': {
#                         'فرمت ورودی صحیح نمی باشد': 'داده های ارسالی کامل نیست',
#                         'ناموفق. فروشگاه با آیدی ارائه شده وجود ندارد': 'فروشگاه با آیدی ارائه شده وجود ندارد'
#                     }
#                 },
#                 'DELETE': {
#                     'توضیحات': 'از طریق این متد امکان حذف فروشگاه فراهم شده است',
#                     'سبک داده مورد پذیرش': 'json جیسون',
#                     'داده های ارسالی': {
#                         'shop_id': 'آیدی فروشگاه',
#                     },
#                     'خطا های احتمالی': {
#                         'فرمت ورودی صحیح نمی باشد': 'داده های ارسالی کامل نیست',
#                         'ناموفق. فروشگاه با آیدی ارائه شده وجود ندارد': 'فروشگاه با آیدی ارائه شده وجود ندارد'
#                     }
#                 },
#             }
#         }
#         return JsonResponse(json_response_body)
#
#     def post(self, request, *args, **kwargs):
#         front_input = json.loads(request.body)
#         try:
#             shop_id = front_input['shop_id']
#             try:
#                 shop = Shop.objects.get(id=shop_id)
#
#                 shop_keywords = shop.shop_keyword.all()
#                 shop_categories = shop.shop_category.all()
#                 i = 0
#                 shop_keyword_dict = {}
#                 for shop_keyword in shop_keywords:
#                     shop_keyword_dict[i] = {
#                         'Keyword id': shop_keyword.id,
#                         'Keyword type': shop_keyword.Keyword_type,
#                         'Keyword name en': shop_keyword.name_en,
#                         'Keyword name fa': shop_keyword.name_fa,
#                     }
#
#                 i = 0
#                 shop_category_dict = {}
#                 for shop_category in shop_categories:
#                     shop_category_dict[i] = {
#                         "category id": shop_category.id,
#                         "category type": shop_category.category_type,
#                         "category priority": shop_category.priority,
#                         "category keyword": {
#                             'Keyword id': shop_category.keyword.id,
#                             'Keyword type': shop_category.keyword.Keyword_type,
#                             'Keyword name en': shop_category.keyword.name_en,
#                             'Keyword name fa': shop_category.keyword.name_fa,
#                         }
#                     }
#                 json_response_body = {
#                     'method': 'post',
#                     'request': 'مشخصات فروشگاه',
#                     'result': 'موفق',
#                     'user': shop.user.username,
#                     'name': shop.name,
#                     'is online shop': shop.is_online_shop,
#                     'website link': shop.website_link,
#                     'address': shop.address,
#                     'phone': shop.phone,
#                     'shop keywords': shop_keyword_dict,
#                     'shop categories': shop_category_dict,
#                 }
#             except Exception as e:
#                 print(str(e))
#                 json_response_body = {
#                     'method': 'post',
#                     'request': 'مشخصات فروشگاه',
#                     'result': 'ناموفق. فروشگاه با آیدی ارائه شده وجود ندارد',
#                     'shop id': shop_id,
#                 }
#
#             return JsonResponse(json_response_body)
#         except:
#             json_response_body = {
#                 'method': 'post',
#                 'request': 'مشخصات فروشگاه',
#                 'result': 'ناموفق',
#                 'message': 'فرمت ورودی صحیح نمی باشد'
#             }
#             return JsonResponse(json_response_body)
#
#     def put(self, request, *args, **kwargs):
#         front_input = json.loads(request.body)
#         try:
#             shop_id = front_input['shop_id']
#             try:
#                 shop = Shop.objects.get(id=shop_id)
#                 try:
#                     name = front_input['name']
#                     shop.name = name
#                     shop.save()
#                 except:
#                     pass
#                 try:
#                     is_online_shop = front_input['is_online_shop']
#                     shop.is_online_shop = is_online_shop
#                     shop.save()
#                 except:
#                     pass
#                 try:
#                     website_link = front_input['website_link']
#                     shop.website_link = website_link
#                     shop.save()
#                 except:
#                     pass
#                 try:
#                     address = front_input['address']
#                     shop.address = address
#                     shop.save()
#                 except:
#                     pass
#                 try:
#                     phone = front_input['phone']
#                     shop.phone = phone
#                     shop.save()
#                 except:
#                     pass
#                 try:
#                     shop_keywords_id = front_input['shop_keywords_id']
#                     for keyword_id in shop_keywords_id:
#                         try:
#                             keyword = Keyword.objects.get(id=keyword_id)
#                             shop.shop_keyword.add(keyword)
#                             shop.save()
#                         except:
#                             json_response_body = {
#                                 'method': 'post',
#                                 'request': 'ویرایش فروشگاه',
#                                 'result': 'نا موفق. آی دی کلمه کلیدی وجود ندارد',
#                                 'shop id': shop_id,
#                                 'keyword id': keyword_id,
#                             }
#                             return JsonResponse(json_response_body)
#                 except:
#                     pass
#                 try:
#                     shop_categories_id = front_input['shop_categories_id']
#                     for category_id in shop_categories_id:
#                         try:
#                             category = Category.objects.get(id=category_id)
#                             shop.shop_category.add(category)
#                             shop.save()
#                         except:
#                             json_response_body = {
#                                 'method': 'post',
#                                 'request': 'ویرایش فروشگاه',
#                                 'result': 'نا موفق. آی دی دسته وجود ندارد',
#                                 'shop id': shop_id,
#                                 'category id': category_id,
#                             }
#                             return JsonResponse(json_response_body)
#                 except:
#                     pass
#
#                 json_response_body = {
#                     'method': 'post',
#                     'request': 'ویرایش دسته',
#                     'result': 'موفق. دسته با موفقیت ویرایش شد',
#                     'shop id': shop_id,
#                 }
#                 return JsonResponse(json_response_body)
#             except:
#                 json_response_body = {
#                     'method': 'post',
#                     'request': 'ویرایش فروشگاه',
#                     'result': 'ناموفق. فروشگاه وجود ندارد',
#                     'shop id': shop_id,
#                 }
#
#                 return JsonResponse(json_response_body)
#         except Exception as e:
#             print(str(e))
#             json_response_body = {
#                 'method': 'post',
#                 'request': 'ویرایش فروشگاه',
#                 'result': 'ناموفق',
#                 'message': 'فرمت ورودی صحیح نمی باشد'
#             }
#             return JsonResponse(json_response_body)
#
#     def delete(self, request, *args, **kwargs):
#         front_input = json.loads(request.body)
#         try:
#             shop_id = front_input['shop_id']
#             try:
#                 shop = Shop.objects.get(id=shop_id)
#                 shop.delete()
#                 json_response_body = {
#                     'method': 'post',
#                     'request': 'حذف فروشگاه',
#                     'result': 'موفق. فروشگاه با موفقیت حذف شد',
#                     'shop id': shop_id,
#                 }
#                 return JsonResponse(json_response_body)
#             except:
#                 json_response_body = {
#                     'method': 'post',
#                     'request': 'حذف فروشگاه',
#                     'result': 'ناموفق. فروشگاه وجود ندارد',
#                     'shop id': shop_id,
#                 }
#
#                 return JsonResponse(json_response_body)
#         except:
#             json_response_body = {
#                 'method': 'post',
#                 'request': 'حذف فروشگاه',
#                 'result': 'ناموفق',
#                 'message': 'فرمت ورودی صحیح نمی باشد'
#             }
#             return JsonResponse(json_response_body)
#
#     def head(self, request, *args, **kwargs):
#         json_response_body = {
#             'method': 'head',
#             'request': 'ویرایش فروشگاه',
#             'result': 'ناموفق',
#             'message': 'متد مورد استفاده غیر مجاز می باشد'
#         }
#         self.context['json_response_body'] = json_response_body
#         return JsonResponse(self.context)
#
#     def options(self, request, *args, **kwargs):
#         json_response_body = {
#             'method': 'option',
#             'request': 'ویرایش فروشگاه',
#             'result': 'ناموفق',
#             'message': 'متد مورد استفاده غیر مجاز می باشد'
#         }
#         self.context['json_response_body'] = json_response_body
#         return JsonResponse(self.context)
#
#     def patch(self, request, *args, **kwargs):
#         json_response_body = {
#             'method': 'patch',
#             'request': 'ویرایش فروشگاه',
#             'result': 'ناموفق',
#             'message': 'متد مورد استفاده غیر مجاز می باشد'
#         }
#         self.context['json_response_body'] = json_response_body
#         return JsonResponse(self.context)
#
#
# class MarketShopList(APIView):
#     authentication_classes = (SessionAuthentication,)
#     permission_classes = (CustomIsAuthenticated,)
#
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.context = {}
#
#     def get(self, request, *args, **kwargs):
#         json_response_body = {
#             'request': 'لیست فروشگاه ها',
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
#                     'توضیحات': 'از طریق این متد امکان دریافت لیست فروشگاه ها فراهم شده است',
#                     'سبک داده مورد پذیرش': 'json جیسون',
#                     'داده های ارسالی': 'ندارد',
#                     'خطا های احتمالی': {
#                         'فرمت ورودی صحیح نمی باشد': 'داده های ارسالی کامل نیست',
#                         'نامشخص': 'خطای سیستم'
#                     }
#                 },
#             }
#         }
#         return JsonResponse(json_response_body)
#
#     def post(self, request, *args, **kwargs):
#         front_input = json.loads(request.body)
#         json_response_body = {
#             'method': 'post',
#             'request': 'لیست فروشگاه ها',
#             'result': 'موفق',
#         }
#
#         try:
#             shops = Shop.objects.filter(created_by=request.user)
#             shop_dict = {}
#             i = 0
#             for shop in shops:
#                 shop_dict[i] = {
#                     'user': shop.created_by.username,
#                     'name': shop.name,
#                     'is_online_shop': shop.is_online_shop,
#                     'website_link': shop.website_link,
#                     'address': shop.address,
#                     'phone': shop.phone,
#                 }
#                 keywords = shop.shop_keyword.all()
#                 categories = shop.shop_category.all()
#                 keyword_dict = {}
#                 j = 0
#                 for keyword in keywords:
#                     keyword_dict[j] = {
#                         'keyword id': keyword.id,
#                         'keyword type': keyword.Keyword_type,
#                         'keyword name fa': keyword.name_fa,
#                         'keyword name en': keyword.name_fa,
#                     }
#                 category_dict = {}
#                 k = 0
#                 for category in categories:
#                     category_dict[k] = {
#                         'category id': category.id,
#                         'category type': category.category_type,
#                         'category keyword': {
#                             'keyword id': category.keyword.id,
#                             'keyword type': category.keyword.Keyword_type,
#                             'keyword name fa': category.keyword.name_fa,
#                             'keyword name en': category.keyword.name_fa,
#                         },
#                         'category priority': category.priority,
#                     }
#                 shop_dict[i]['shop keywords'] = keyword_dict
#                 shop_dict[i]['shop categories'] = category_dict
#             json_response_body['markets'] = shop_dict
#             return JsonResponse(json_response_body)
#         except Exception as e:
#             print(str(e))
#             json_response_body = {
#                 'method': 'post',
#                 'request': 'لیست فروشگاه ها',
#                 'result': 'ناموفق',
#                 'message': str(e)
#             }
#             return JsonResponse(json_response_body)
#
#     def put(self, request, *args, **kwargs):
#         json_response_body = {
#             'method': 'put',
#             'request': 'لیست فروشگاه ها',
#             'result': 'ناموفق',
#             'message': 'متد مورد استفاده غیر مجاز می باشد'
#         }
#         self.context['json_response_body'] = json_response_body
#         return JsonResponse(self.context)
#
#     def delete(self, request, *args, **kwargs):
#         json_response_body = {
#             'method': 'delete',
#             'request': 'لیست فروشگاه ها',
#             'result': 'ناموفق',
#             'message': 'متد مورد استفاده غیر مجاز می باشد'
#         }
#         self.context['json_response_body'] = json_response_body
#         return JsonResponse(self.context)
#
#     def head(self, request, *args, **kwargs):
#         json_response_body = {
#             'method': 'head',
#             'request': 'لیست فروشگاه ها',
#             'result': 'ناموفق',
#             'message': 'متد مورد استفاده غیر مجاز می باشد'
#         }
#         self.context['json_response_body'] = json_response_body
#         return JsonResponse(self.context)
#
#     def options(self, request, *args, **kwargs):
#         json_response_body = {
#             'method': 'option',
#             'request': 'لیست فروشگاه ها',
#             'result': 'ناموفق',
#             'message': 'متد مورد استفاده غیر مجاز می باشد'
#         }
#         self.context['json_response_body'] = json_response_body
#         return JsonResponse(self.context)
#
#     def patch(self, request, *args, **kwargs):
#         json_response_body = {
#             'method': 'patch',
#             'request': 'لیست فروشگاه ها',
#             'result': 'ناموفق',
#             'message': 'متد مورد استفاده غیر مجاز می باشد'
#         }
#         self.context['json_response_body'] = json_response_body
#         return JsonResponse(self.context)
#
#
# class MarketShopNew(APIView):
#     authentication_classes = (SessionAuthentication,)
#     permission_classes = (CustomIsAuthenticated,)
#
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.context = {}
#
#     def get(self, request, *args, **kwargs):
#         json_response_body = {
#             'request': 'ایجاد فروشگاه',
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
#                     'توضیحات': 'از طریق این متد امکان ایجاد فروشگاه فراهم شده است',
#                     'سبک داده مورد پذیرش': 'json جیسون',
#                     'داده های ارسالی': {
#                         'shop_name': 'نام دلخواه',
#                         'is_online_shop': 'true or false',
#                         'shop_website_link': 'آدرس وبسایت',
#                         'shop_address': 'آدرس فروشگاه',
#                         'shop_phone': 'شماره تلفن فروشگاه',
#                         'shop_keywords_id': {
#                             0: '1',
#                             1: '2',
#                             2: '...'
#                         },
#                         'shop_categories_id': {
#                             0: '1',
#                             1: '2',
#                             2: '...'
#                         },
#                     },
#                     'خطا های احتمالی': {
#                         'فرمت ورودی صحیح نمی باشد': 'داده های ارسالی کامل نیست یا بدرستی ارسال نشده است',
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
#             shop_name = front_input['shop_name']
#             is_online_shop = front_input['is_online_shop']
#             shop_website_link = front_input['shop_website_link']
#             shop_address = front_input['shop_address']
#             shop_phone = front_input['shop_phone']
#             shop_keywords_id = front_input['shop_keyword']
#             shop_categories_id = front_input['shop_keyword']
#             new_shop = Shop(
#                 name=shop_name,
#                 is_online_shop=is_online_shop,
#                 website_link=shop_website_link,
#                 address=shop_address,
#                 phone=shop_phone,
#                 created_by=request.user,
#             )
#             new_shop.save()
#
#             for keyword_id in shop_keywords_id:
#                 keyword = Keyword.objects.get(id=keyword_id)
#                 new_shop.shop_keyword.add(keyword)
#                 new_shop.save()
#             for category_id in shop_categories_id:
#                 category = Category.objects.get(id=category_id)
#                 new_shop.shop_category.add(category)
#                 new_shop.save()
#
#             json_response_body = {
#                 'method': 'post',
#                 'request': 'افزودن فروشگاه',
#                 'result': 'فروشگاه با موفقیت افزوده شد',
#                 'new shop id': new_shop.id,
#             }
#             return JsonResponse(json_response_body)
#         except Exception as e:
#             json_response_body = {
#                 'method': 'post',
#                 'request': 'افزودن فروشگاه',
#                 'result': 'ناموفق',
#                 'message': 'فرمت ورودی صحیح نمی باشد'
#             }
#             return JsonResponse(json_response_body)
#
#     def put(self, request, *args, **kwargs):
#         json_response_body = {
#             'method': 'put',
#             'request': 'ویرایش دسته',
#             'result': 'ناموفق',
#             'message': 'متد مورد استفاده غیر مجاز می باشد'
#         }
#         return JsonResponse(json_response_body)
#
#     def delete(self, request, *args, **kwargs):
#         json_response_body = {
#             'method': 'delete',
#             'request': 'حذف دسته',
#             'result': 'ناموفق',
#             'message': 'متد مورد استفاده غیر مجاز می باشد'
#         }
#         return JsonResponse(json_response_body)
#
#     def head(self, request, *args, **kwargs):
#         json_response_body = {
#             'method': 'head',
#             'request': 'ویرایش دسته',
#             'result': 'ناموفق',
#             'message': 'متد مورد استفاده غیر مجاز می باشد'
#         }
#         return JsonResponse(json_response_body)
#
#     def options(self, request, *args, **kwargs):
#         json_response_body = {
#             'method': 'options',
#             'request': 'ویرایش دسته',
#             'result': 'ناموفق',
#             'message': 'متد مورد استفاده غیر مجاز می باشد'
#         }
#         return JsonResponse(json_response_body)
#
#     def patch(self, request, *args, **kwargs):
#         json_response_body = {
#             'method': 'patch',
#             'request': 'ویرایش دسته',
#             'result': 'ناموفق',
#             'message': 'متد مورد استفاده غیر مجاز می باشد'
#         }
#         return JsonResponse(json_response_body)
#
#
# '''
# section market shop
# '''
#
# '''
# section market Product
# '''
#
#
# class MarketProductSingle(APIView):
#     authentication_classes = (SessionAuthentication,)
#     permission_classes = (CustomIsAuthenticated,)
#
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.context = {}
#
#     def get(self, request, *args, **kwargs):
#         json_response_body = {
#             'request': 'مشخصات محصول',
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
#                     'توضیحات': 'از طریق این متد امکان دریافت مشخصات محصول فراهم شده است',
#                     'سبک داده مورد پذیرش': 'json جیسون',
#                     'داده های ارسالی': {
#                         'product_id': 'آیدی محصول',
#                     },
#                     'خطا های احتمالی': {
#                         'فرمت ورودی صحیح نمی باشد': 'داده های ارسالی کامل نیست یا بدرستی ارسال نشده است',
#                         'ناموفق. محصول با آیدی ارائه شده وجود ندارد': 'ناموفق. محصول با آیدی ارائه شده وجود ندارد'
#                     }
#                 },
#                 'PUT': {
#                     'توضیحات': 'از طریق این متد امکان ویرایش محصول فراهم شده است',
#                     'سبک داده مورد پذیرش': 'json جیسون',
#                     'داده های ارسالی': {
#                         'product_id': 'آیدی محصول',
#                     },
#                     'خطا های احتمالی': {
#                         'فرمت ورودی صحیح نمی باشد': 'داده های ارسالی کامل نیست یا بدرستی ارسال نشده است',
#                         'ناموفق. محصول با آیدی ارائه شده وجود ندارد': 'ناموفق. محصول با آیدی ارائه شده وجود ندارد'
#                     }
#                 },
#                 'DELETE': {
#                     'توضیحات': 'از طریق این متد امکان حذف محصول فراهم شده است',
#                     'سبک داده مورد پذیرش': 'json جیسون',
#                     'داده های ارسالی': {
#                         'product_id': 'آیدی محصول',
#                     },
#                     'خطا های احتمالی': {
#                         'فرمت ورودی صحیح نمی باشد': 'داده های ارسالی کامل نیست یا بدرستی ارسال نشده است',
#                         'ناموفق. محصول با آیدی ارائه شده وجود ندارد': 'ناموفق. محصول با آیدی ارائه شده وجود ندارد'
#                     }
#                 },
#             }
#         }
#         return JsonResponse(json_response_body)
#
#     def post(self, request, *args, **kwargs):
#         front_input = json.loads(request.body)
#         try:
#             product_id = front_input['product_id']
#             try:
#                 product = Product.objects.get(created_by=request.user, id=product_id)
#                 product_keywords = product.product_keywords.all()
#                 product_keywords_json = {}
#                 i = 0
#                 for keyword in product_keywords:
#                     product_keywords_json[i] = keyword.id
#                     i += 1
#                 product_categories = product.product_categories.all()
#                 product_categories_json = {}
#                 i = 0
#                 for category in product_categories:
#                     product_categories_json[i] = category.id
#                     i += 1
#                 json_response_body = {
#                     'shop id': product.shop.id,
#                     'name': product.name,
#                     'price': product.price,
#                     'is online product': product.is_online_product,
#                     'product link': product.product_link,
#                     'product keywords id': product_keywords_json,
#                     'product categories id': product_categories_json,
#                     'created by id': request.user.id,
#                 }
#
#             except Exception as e:
#                 print(str(e))
#                 json_response_body = {
#                     'method': 'post',
#                     'request': 'مشخصات محصول',
#                     'result': 'ناموفق. محصول با آیدی ارائه شده وجود ندارد',
#                     'product id': product_id,
#                 }
#
#             return JsonResponse(json_response_body)
#         except Exception as e:
#             print(str(e))
#             json_response_body = {
#                 'method': 'post',
#                 'request': 'مشخصات محصول',
#                 'result': 'ناموفق',
#                 'message': 'فرمت ورودی صحیح نمی باشد'
#             }
#             return JsonResponse(json_response_body)
#
#     def put(self, request, *args, **kwargs):
#         front_input = json.loads(request.body)
#         try:
#             product_id = front_input['product_id']
#             try:
#                 product = Product.objects.get(created_by=request.user, id=product_id)
#                 try:
#                     product_shop_id = front_input['product_shop_id']
#                     try:
#                         shop = Shop.objects.get(id=product_shop_id, created_by=request.user)
#                         product.shop = shop
#                         product.save()
#                     except:
#                         json_response_body = {
#                             'method': 'post',
#                             'request': 'ویرایش محصول',
#                             'result': 'نا موفق. فروشگاهی با آیدی مورد نظر وجود ندارد',
#                             'shop id': product_shop_id,
#                         }
#                         return JsonResponse(json_response_body)
#                 except:
#                     pass
#                 try:
#                     product_name = front_input['product_name']
#                     product.name = product_name
#                     product.save()
#                 except:
#                     pass
#                 try:
#                     product_price = front_input['product_price']
#                     product.price = product_price
#                     product.save()
#                 except:
#                     pass
#                 try:
#                     product_is_online_product = front_input['product_is_online_product']
#                     product.is_online_product = product_is_online_product
#                     product.save()
#                 except:
#                     pass
#                 try:
#                     product_link = front_input['product_link']
#                     product.product_link = product_link
#                     product.save()
#                 except:
#                     pass
#                 try:
#                     product_keywords_id = front_input['product_keywords_id']
#                     product.product_keywords.all().delete()
#                     for keyword_id in product_keywords_id:
#                         keyword = Keyword.objects.get(id=keyword_id, created_by=request.user)
#                         product.product_keywords.add(keyword)
#                         product.save()
#                 except:
#                     pass
#                 try:
#                     product_categories_id = front_input['product_categories_id']
#                     product.product_categories.all().delete()
#                     for category_id in product_categories_id:
#                         category = Category.objects.get(id=category_id, created_by=request.user)
#                         product.product_categories.add(category)
#                         product.save()
#                 except:
#                     pass
#
#                 json_response_body = {
#                     'method': 'post',
#                     'request': 'ویرایش محصول',
#                     'result': 'موفق. تغییرات انجام شد',
#                     'product id': product_id,
#                 }
#                 return JsonResponse(json_response_body)
#             except:
#                 json_response_body = {
#                     'method': 'post',
#                     'request': 'ویرایش محصول',
#                     'result': 'نا موفق. محصول با آیدی پیدا نشد',
#                     'product id': product_id,
#                 }
#                 return JsonResponse(json_response_body)
#
#         except Exception as e:
#             print(str(e))
#             json_response_body = {
#                 'method': 'post',
#                 'request': 'ویرایش فروشگاه',
#                 'result': 'ناموفق',
#                 'message': 'فرمت ورودی صحیح نمی باشد'
#             }
#             return JsonResponse(json_response_body)
#
#     def delete(self, request, *args, **kwargs):
#         front_input = json.loads(request.body)
#         try:
#             product_id = front_input['product_id']
#             try:
#                 product = Product.objects.get(created_by=request.user, id=product_id)
#                 product.delete()
#                 json_response_body = {
#                     'method': 'delete',
#                     'request': 'حذف محصول',
#                     'result': 'موفق. محصول با موفقیت حذف شد',
#                     'product id': product_id,
#                 }
#                 return JsonResponse(json_response_body)
#             except:
#                 json_response_body = {
#                     'method': 'delete',
#                     'request': 'حذف محصول',
#                     'result': 'ناموفق. محصول وجود ندارد',
#                     'product id': product_id,
#                 }
#
#                 return JsonResponse(json_response_body)
#         except:
#             json_response_body = {
#                 'method': 'delete',
#                 'request': 'حذف محصول',
#                 'result': 'ناموفق',
#                 'message': 'فرمت ورودی صحیح نمی باشد'
#             }
#             return JsonResponse(json_response_body)
#
#     def head(self, request, *args, **kwargs):
#         json_response_body = {
#             'method': 'head',
#             'request': 'ویرایش محصول',
#             'result': 'ناموفق',
#             'message': 'متد مورد استفاده غیر مجاز می باشد'
#         }
#         self.context['json_response_body'] = json_response_body
#         return JsonResponse(self.context)
#
#     def options(self, request, *args, **kwargs):
#         json_response_body = {
#             'method': 'option',
#             'request': 'ویرایش محصول',
#             'result': 'ناموفق',
#             'message': 'متد مورد استفاده غیر مجاز می باشد'
#         }
#         self.context['json_response_body'] = json_response_body
#         return JsonResponse(self.context)
#
#     def patch(self, request, *args, **kwargs):
#         json_response_body = {
#             'method': 'patch',
#             'request': 'ویرایش محصول',
#             'result': 'ناموفق',
#             'message': 'متد مورد استفاده غیر مجاز می باشد'
#         }
#         self.context['json_response_body'] = json_response_body
#         return JsonResponse(self.context)
#
#
# class MarketProductList(APIView):
#     authentication_classes = (SessionAuthentication,)
#     permission_classes = (CustomIsAuthenticated,)
#
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.context = {}
#
#     def get(self, request, *args, **kwargs):
#         json_response_body = {
#             'request': 'لیست محصولات',
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
#                     'توضیحات': 'از طریق این متد امکان دریافت لیست محصولات فراهم شده است',
#                     'سبک داده مورد پذیرش': 'json جیسون',
#                     'داده های ارسالی': 'ندارد',
#                     'خطا های احتمالی': {
#                         'فرمت ورودی صحیح نمی باشد': 'داده های ارسالی کامل نیست یا بدرستی ارسال نشده است',
#                         'نامشخص': 'خطای سیستم'
#                     }
#                 },
#             }
#         }
#         return JsonResponse(json_response_body)
#
#     def post(self, request, *args, **kwargs):
#         front_input = json.loads(request.body)
#         json_response_body = {
#             'method': 'post',
#             'request': 'لیست محصولات',
#             'result': 'موفق',
#         }
#         try:
#             products = Product.objects.filter(created_by=request.user)
#             product_dict = {}
#             j = 0
#             for product in products:
#                 product_keywords = product.product_keywords.all()
#                 product_keywords_json = {}
#                 i = 0
#                 for keyword in product_keywords:
#                     product_keywords_json[i] = keyword.id
#                     i += 1
#                 product_categories = product.product_categories.all()
#                 product_categories_json = {}
#                 i = 0
#                 for category in product_categories:
#                     product_categories_json[i] = category.id
#                     i += 1
#                 product_dict[j] = {
#                     'shop id': product.shop.id,
#                     'name': product.name,
#                     'price': product.price,
#                     'is online product': product.is_online_product,
#                     'product link': product.product_link,
#                     'product keywords id': product_keywords_json,
#                     'product categories id': product_categories_json,
#                     'created by': request.user.username,
#                 }
#                 j += 1
#             json_response_body['products'] = product_dict
#             return JsonResponse(json_response_body)
#         except Exception as e:
#             json_response_body = {
#                 'method': 'post',
#                 'request': 'لیست محصولات',
#                 'result': 'ناموفق',
#                 'message': str(e)
#             }
#             return JsonResponse(json_response_body)
#
#     def put(self, request, *args, **kwargs):
#         json_response_body = {
#             'method': 'put',
#             'request': 'لیست محصولات',
#             'result': 'ناموفق',
#             'message': 'متد مورد استفاده غیر مجاز می باشد'
#         }
#         self.context['json_response_body'] = json_response_body
#         return JsonResponse(self.context)
#
#     def delete(self, request, *args, **kwargs):
#         json_response_body = {
#             'method': 'delete',
#             'request': 'لیست محصولات',
#             'result': 'ناموفق',
#             'message': 'متد مورد استفاده غیر مجاز می باشد'
#         }
#         self.context['json_response_body'] = json_response_body
#         return JsonResponse(self.context)
#
#     def head(self, request, *args, **kwargs):
#         json_response_body = {
#             'method': 'head',
#             'request': 'لیست محصولات',
#             'result': 'ناموفق',
#             'message': 'متد مورد استفاده غیر مجاز می باشد'
#         }
#         self.context['json_response_body'] = json_response_body
#         return JsonResponse(self.context)
#
#     def options(self, request, *args, **kwargs):
#         json_response_body = {
#             'method': 'option',
#             'request': 'لیست محصولات',
#             'result': 'ناموفق',
#             'message': 'متد مورد استفاده غیر مجاز می باشد'
#         }
#         self.context['json_response_body'] = json_response_body
#         return JsonResponse(self.context)
#
#     def patch(self, request, *args, **kwargs):
#         json_response_body = {
#             'method': 'patch',
#             'request': 'لیست محصولات',
#             'result': 'ناموفق',
#             'message': 'متد مورد استفاده غیر مجاز می باشد'
#         }
#         self.context['json_response_body'] = json_response_body
#         return JsonResponse(self.context)
#
#
# class MarketProductNew(APIView):
#     authentication_classes = (SessionAuthentication,)
#     permission_classes = (CustomIsAuthenticated,)
#
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.context = {}
#
#     def get(self, request, *args, **kwargs):
#         json_response_body = {
#             'request': 'افزودن محصول',
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
#                     'توضیحات': 'از طریق این متد امکان افزودن محصول جدید فراهم شده است',
#                     'سبک داده مورد پذیرش': 'json جیسون',
#                     'داده های ارسالی': {
#                         'product_shop_id': 'آیدی فروشگاه مرتبط با محصول',
#                         'product_name': 'نام محصول',
#                         'product_price': 'قیمت محصول',
#                         'product_is_online_product': 'true or false',
#                         'product_link': 'لینک محصول',
#                         'product_keywords_id': {
#                             0: 1,
#                             1: 2,
#                             2: '...'
#                         },
#                         'product_categories_id': {
#                             0: 1,
#                             1: 2,
#                             2: '...'
#                         },
#                     },
#                     'خطا های احتمالی': {
#                         'فرمت ورودی صحیح نمی باشد': 'داده های ارسالی کامل نیست',
#                         'ناموفق. فروشگاه با آیدی ارائه شده وجود ندارد': 'فروشگاه با آیدی ارائه شده وجود ندارد'
#                     }
#                 },
#             }
#         }
#         return JsonResponse(json_response_body)
#
#     def post(self, request, *args, **kwargs):
#         front_input = json.loads(request.body)
#         try:
#             product_shop_id = front_input['product_shop_id']
#             product_name = front_input['product_name']
#             product_price = front_input['product_price']
#             product_is_online_product = front_input['product_is_online_product']
#             product_link = front_input['product_link']
#             product_keywords_id = front_input['product_keywords_id']
#             product_categories_id = front_input['product_categories_id']
#             try:
#                 shop = Shop.objects.get(id=product_shop_id, created_by=request.user)
#             except:
#                 json_response_body = {
#                     'method': 'post',
#                     'request': 'افزودن محصول',
#                     'result': 'نا موفق. فروشگاهی با آیدی مورد نظر وجود ندارد',
#                     'shop id': product_shop_id,
#                 }
#                 return JsonResponse(json_response_body)
#             new_product = Product(
#                 shop=shop,
#                 name=product_name,
#                 price=product_price,
#                 is_online_product=product_is_online_product,
#                 product_link=product_link,
#                 created_by=request.user,
#             )
#             new_product.save()
#             keywords_dict = {}
#             i = 0
#             for keyword_id in product_keywords_id:
#                 keyword = Keyword.objects.get(id=keyword_id, created_by=request.user)
#                 new_product.product_keywords.add(keyword)
#                 new_product.save()
#                 keywords_dict[i] = keyword.id
#                 i += 1
#             categories_dict = {}
#             i = 0
#             for category_id in product_categories_id:
#                 category = Category.objects.get(id=category_id, created_by=request.user)
#                 new_product.product_categories.add(category)
#                 new_product.save()
#                 categories_dict[i] = category.id
#                 i += 1
#             json_response_body = {
#                 'method': 'post',
#                 'request': 'افزودن محصول',
#                 'result': 'موفق. محصول افزوده شد',
#                 'product id': new_product.id,
#                 'shop id': new_product.shop.id,
#                 'name': new_product.name,
#                 'price': new_product.price,
#                 'is online product': new_product.is_online_product,
#                 'product link': new_product.product_link,
#                 'product keywords id': keywords_dict,
#                 'product categories id': categories_dict,
#                 'created by id': request.user.username,
#             }
#             return JsonResponse(json_response_body)
#         except Exception as e:
#             print(str(e))
#             json_response_body = {
#                 'method': 'post',
#                 'request': 'افزودن محصول',
#                 'result': 'ناموفق',
#                 'message': 'فرمت ورودی صحیح نمی باشد'
#             }
#             return JsonResponse(json_response_body)
#
#     def put(self, request, *args, **kwargs):
#         json_response_body = {
#             'method': 'put',
#             'request': 'ویرایش محصول',
#             'result': 'ناموفق',
#             'message': 'متد مورد استفاده غیر مجاز می باشد'
#         }
#         return JsonResponse(json_response_body)
#
#     def delete(self, request, *args, **kwargs):
#         json_response_body = {
#             'method': 'delete',
#             'request': 'حذف محصول',
#             'result': 'ناموفق',
#             'message': 'متد مورد استفاده غیر مجاز می باشد'
#         }
#         return JsonResponse(json_response_body)
#
#     def head(self, request, *args, **kwargs):
#         json_response_body = {
#             'method': 'head',
#             'request': 'ویرایش محصول',
#             'result': 'ناموفق',
#             'message': 'متد مورد استفاده غیر مجاز می باشد'
#         }
#         return JsonResponse(json_response_body)
#
#     def options(self, request, *args, **kwargs):
#         json_response_body = {
#             'method': 'options',
#             'request': 'ویرایش محصول',
#             'result': 'ناموفق',
#             'message': 'متد مورد استفاده غیر مجاز می باشد'
#         }
#         return JsonResponse(json_response_body)
#
#     def patch(self, request, *args, **kwargs):
#         json_response_body = {
#             'method': 'patch',
#             'request': 'ویرایش محصول',
#             'result': 'ناموفق',
#             'message': 'متد مورد استفاده غیر مجاز می باشد'
#         }
#         return JsonResponse(json_response_body)
#
#
# '''
# section market Product
# '''
#
#
# def token_8_first_letter(request):
#     header_token = request.META['HTTP_AUTHORIZATION']
#     header_token = str(header_token)
#     header_token = header_token.replace('Token ', '')
#     header_token = header_token[:8]
#     return str(header_token)
