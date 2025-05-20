from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Category, Product, Brand, Tag, Customer, Order

# Create your views here.
def index(request):
    return HttpResponse(f"Hello, world. You're at the ORM index.for admin page go to {request.build_absolute_uri('/admin/')}")

def categories(request):
    categories = Category.objects.all()
    return JsonResponse(list(categories.values()), safe=False)


