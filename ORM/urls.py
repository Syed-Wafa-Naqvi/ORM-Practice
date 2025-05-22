from django.urls import path
from ORM.views import *

urlpatterns = [
    path('', index, name='index'),
    path('categories/', categories, name='categories'),
    path('categoryid/<int:category_id>/', category_id, name='category_id'),
    path('check/', check, name='check'),
    path('get/',get_product,name='get_products'),
    path('pid/''<int:product_id>/',product_detail,name='products_by_id'),
    path('product1/', specific_product ,name='get_products'),
    path('least/', least_one ,name='one_order'),
    path('retrive/', retrive_product ,name='retrive_price'),      
    path('order/', orderBy_email ,name='order_email'),      
    path('stock/', outOfStock ,name='out_of_stock'),
    path('pname/', productName ,name='product_name'),
    path('coloumn/', single_coloumn ,name='single_column_values'),
    path('tag/', tagged_with ,name='tagged_by'),
    path('tags/', tag_used ,name='tagged'),
    path('ptag/', product_tags ,name='tagged_Product'),


]