# from django.contrib import admin
#
# from market.models import Keyword, Category, Product, Shop
#
#
# @admin.register(Keyword)
# class KeywordAdmin(admin.ModelAdmin):
#     list_display = (
#         'name_fa',
#         'name_en',
#         'Keyword_type',
#     )
#     readonly_fields = (
#         'slug_name_fa',
#         'slug_name_en',
#         'created_by',
#     )
#     fields = (
#         'name_fa',
#         'slug_name_fa',
#         'name_en',
#         'slug_name_en',
#         'Keyword_type',
#         'created_by',
#     )
#
#     def save_model(self, request, instance, form, change):
#         user = request.user
#         instance = form.save(commit=False)
#         if not change:
#             instance.created_by = user
#         instance.save()
#         form.save_m2m()
#         return instance
#
#
# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = (
#         'priority',
#         'keyword',
#         'category_type',
#     )
#     readonly_fields = (
#         'created_by',
#     )
#     fields = (
#         'priority',
#         'keyword',
#         'category_type',
#         'created_by',
#     )
#
#     def save_model(self, request, instance, form, change):
#         user = request.user
#         instance = form.save(commit=False)
#         if not change:
#             instance.created_by = user
#         instance.save()
#         form.save_m2m()
#         return instance
#
#
# @admin.register(Shop)
# class ShopAdmin(admin.ModelAdmin):
#     list_display = (
#         'name',
#         'is_online_shop',
#         'website_link',
#     )
#     readonly_fields = (
#         'created_by',
#     )
#     fields = (
#         'name',
#         'is_online_shop',
#         'website_link',
#         'address',
#         'phone',
#         'shop_keyword',
#         'shop_category',
#         'created_by',
#     )
#
#     def save_model(self, request, instance, form, change):
#         user = request.user
#         instance = form.save(commit=False)
#         if not change:
#             instance.created_by = user
#         instance.save()
#         form.save_m2m()
#         return instance
#
#
# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = (
#         'shop',
#         'name',
#         'price',
#     )
#     readonly_fields = (
#         'created_by',
#     )
#     fields = (
#         'shop',
#         'name',
#         'price',
#         'is_online_product',
#         'product_link',
#         'product_keywords',
#         'product_categories',
#         'created_by',
#     )
#
#     def save_model(self, request, instance, form, change):
#         user = request.user
#         instance = form.save(commit=False)
#         if not change:
#             instance.created_by = user
#         instance.save()
#         form.save_m2m()
#         return instance
