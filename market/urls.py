# from django.urls import path
# from django.views.decorators.csrf import csrf_exempt
#
# from market.views import MarketKeywordSingle, MarketKeywordNew, MarketKeywordList, \
#     MarketCategorySingle, MarketCategoryList, MarketCategoryNew, MarketShopSingle, MarketShopList, MarketShopNew, \
#     MarketProductSingle, MarketProductList, MarketProductNew
#
# app_name = 'market'
#
# urlpatterns = [
#
#     # keyword
#     path('market-keyword-single/', csrf_exempt(MarketKeywordSingle.as_view()), name='market-keyword-single'),
#     path('market-keyword-list/', csrf_exempt(MarketKeywordList.as_view()), name='market-keyword-list'),
#     path('market-keyword-new/', csrf_exempt(MarketKeywordNew.as_view()), name='market-keyword-new'),
#
#     # category
#     path('market-category-single/', csrf_exempt(MarketCategorySingle.as_view()), name='market-category-single'),
#     path('market-category-list/', csrf_exempt(MarketCategoryList.as_view()), name='market-category-list'),
#     path('market-category-new/', csrf_exempt(MarketCategoryNew.as_view()), name='market-category-new'),
#
#     # shop
#     path('market-shop-single/', csrf_exempt(MarketShopSingle.as_view()), name='market-shop-single'),
#     path('market-shop-list/', csrf_exempt(MarketShopList.as_view()), name='market-shop-list'),
#     path('market-shop-new/', csrf_exempt(MarketShopNew.as_view()), name='market-shop-new'),
#
#     # shop
#     path('market-product-single/', csrf_exempt(MarketProductSingle.as_view()), name='market-product-single'),
#     path('market-product-list/', csrf_exempt(MarketProductList.as_view()), name='market-product-list'),
#     path('market-product-new/', csrf_exempt(MarketProductNew.as_view()), name='market-product-new'),
# ]
