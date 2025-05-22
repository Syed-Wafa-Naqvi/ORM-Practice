from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Category, Product, Brand, Tag, Customer, Order
from django.forms.models import model_to_dict
# Create your views here.
def index(request):
    return HttpResponse(f"Hello, world. You're at the ORM index.for admin page go to {request.build_absolute_uri('/admin/')}")

def categories(request):
    categories = Category.objects.all()
    return JsonResponse(list(categories.values()), safe=False)

def category_id(request, category_id):
    categories = Category.objects.filter(id=category_id).values()
    return JsonResponse(list(categories), safe=False)

# def check(request):
#     category = Product.objects.get(name='Cotton Shirts').category
    return JsonResponse(model_to_dict(category), safe=True)
def check(request):
    products = Product.objects.filter(category__name='Product 1')
    return JsonResponse(list(products), safe=False)

def get_product(request):
    products = Product.objects.all().values()
    return JsonResponse(list(products),safe=False)

def product_detail(request, product_id):
    product = Product.objects.filter(id=product_id).values()
    return JsonResponse(list(product), safe=False)

def specific_product(request):
    products = Product.objects.filter(category__name="Category 1").values()
    return JsonResponse(list(products), safe=False)

def least_one(request):
    orders = Customer.objects.filter(orders=1).values()
    return JsonResponse(list(orders), safe=False)

def retrive_product(request):
    retriving = Product.objects.filter(price__gte=10000).values()
    return JsonResponse(list(retriving),safe=False)

def orderBy_email(request):
    order_Placed = Order.objects.filter(customer__name='Wafa').values()
    return JsonResponse(list(order_Placed),safe=False)

def outOfStock(request):
    stock = Product.objects.filter(stock=0).values()
    return JsonResponse(list(stock),safe=False)

def productName(request):
    brand = Product.objects.filter(category__name='Category 1').values()
    return JsonResponse(list(brand),safe=False)

def single_coloumn(request):
    name_Coloumn = Product.objects.all().values_list('name',flat=True)
    return JsonResponse(list(name_Coloumn),safe=False)

def tagged_with(request):
    tagged = Product.objects.filter(tags__name='Tag 50').values()
    return JsonResponse(list(tagged),safe=False)

def tag_used(request):
    products = Tag.objects.filter(products__name='Product 3').values()
    return JsonResponse(list(products),safe=False)

def product_tags(request):
    product = Product.objects.get(name="iPhone 14")
    tags = product.tags.all().values_list('name', flat=True)
    return JsonResponse(list(tags), safe=False)

