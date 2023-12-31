# from django.contrib.auth.models import User
# from django.db import models
#
# from utilities.slug_generator import name_to_url
#
# KEYWORD_CATEGORY_TYPE = (('محصول', 'محصول'), ('مارکت', 'مارکت'))
#
#
# class Keyword(models.Model):
#     Keyword_type = models.CharField(max_length=255, choices=KEYWORD_CATEGORY_TYPE, null=False, blank=False, verbose_name='نوع کلید واژه')
#     name_fa = models.CharField(max_length=255, null=False, blank=False, verbose_name='نام')
#     name_en = models.CharField(max_length=255, null=False, blank=False, verbose_name='name')
#     slug_name_fa = models.CharField(max_length=255, null=False, blank=False, editable=False, verbose_name='اسلاگ نام')
#     slug_name_en = models.CharField(max_length=255, null=False, blank=False, editable=False, verbose_name='name slug')
#     created_by = models.ForeignKey(User, on_delete=models.CASCADE, editable=False, null=False, verbose_name='کاربر سازنده')
#
#     def __str__(self):
#         return self.name_fa + " | " + self.name_en
#
#     class Meta:
#         verbose_name = "0 - کلمه کلیدی"
#         verbose_name_plural = "0 - کلمات کلیدی"
#
#     def save(self, *args, **kwargs):
#         self.slug_name_en = name_to_url(self.name_en)
#         self.slug_name_fa = name_to_url(self.name_fa)
#         super().save(*args, **kwargs)
#
#
# class Category(models.Model):
#     category_type = models.CharField(max_length=255, choices=KEYWORD_CATEGORY_TYPE, null=False, blank=False, verbose_name='نوع کلید واژه')
#     keyword = models.OneToOneField(Keyword, on_delete=models.CASCADE, null=False, blank=False, verbose_name='کلیدواژه')
#     priority = models.PositiveSmallIntegerField(default=1)
#     created_by = models.ForeignKey(User, on_delete=models.CASCADE, editable=False, null=False, verbose_name='کاربر سازنده')
#
#     def __str__(self):
#         return self.keyword.name_fa + " | " + self.keyword.name_en
#
#     class Meta:
#         ordering = ['priority', ]
#         verbose_name = "1 - دسته"
#         verbose_name_plural = "1 - دسته ها"
#
#
# class Shop(models.Model):
#     name = models.CharField(max_length=255, null=False, blank=False, verbose_name='نام فروشگاه')
#     is_online_shop = models.BooleanField(default=False, verbose_name='آیا آنلاین شاپ است؟')
#     website_link = models.CharField(max_length=255, null=False, blank=False, verbose_name='آدرس اصلی وب سایت')
#     address = models.TextField(null=True, blank=True, verbose_name='آدرس')
#     phone = models.CharField(max_length=255, null=False, blank=False, verbose_name='شماره تماس')
#     shop_keyword = models.ManyToManyField(Keyword, limit_choices_to={'Keyword_type': 'مارکت'}, blank=True, verbose_name='کلمات کلیدی')
#     shop_category = models.ManyToManyField(Category, limit_choices_to={'category_type': 'مارکت'}, blank=True,
#                                            verbose_name='دسته ها')
#     created_by = models.ForeignKey(User, on_delete=models.CASCADE, editable=False, null=False, verbose_name='کاربر سازنده')
#
#     def __str__(self):
#         return self.created_by.username + " | " + self.name
#
#     class Meta:
#         verbose_name = "2 - مارکت"
#         verbose_name_plural = "2 - مارکت ها"
#
#
# class Product(models.Model):
#     shop = models.ForeignKey(Shop, on_delete=models.CASCADE, null=False, blank=False, verbose_name='فروشگاه')
#     name = models.CharField(max_length=255, null=False, blank=False, verbose_name='نام محصول')
#     price = models.PositiveIntegerField(default=0, null=False, blank=False, verbose_name='قیمت - ریال')
#     is_online_product = models.BooleanField(default=False, verbose_name='آیا محصول به صورت آنلاین ارائه شده است؟')
#     product_link = models.CharField(max_length=255, null=False, blank=False, verbose_name='لینک صفحه خرید محصول')
#     product_keywords = models.ManyToManyField(Keyword, limit_choices_to={'Keyword_type': 'محصول'}, blank=True, verbose_name='کلمات کلیدی')
#     product_categories = models.ManyToManyField(Category, limit_choices_to={'category_type': 'محصول'}, blank=True,
#                                                 verbose_name='دسته ها')
#     created_by = models.ForeignKey(User, on_delete=models.CASCADE, editable=False, null=False, verbose_name='کاربر سازنده')
#
#     def __str__(self):
#         return self.name + " | " + str(self.price)
#
#     class Meta:
#         verbose_name = "3 - محصول"
#         verbose_name_plural = "3 - محصولات"
