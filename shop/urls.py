from django.urls import path

from .views import register_view,login_view,get_product_view,all_product,basket_view,add_product


app_name = 'shop'


urlpatterns = [
    path('register/',register_view,name='register_page'),
    path('login/',login_view,name='login_page'),
    path('products/',all_product,name='all_product'),
    path('get_product/',get_product_view,name='product_page'),
    path('basket/',basket_view,name='basket_oage'),
    path('product_add/',add_product,name='add_view' )
]
