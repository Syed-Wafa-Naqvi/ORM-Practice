from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Brand)
admin.site.register(Tag)
admin.site.register(Customer)
admin.site.register(Order)