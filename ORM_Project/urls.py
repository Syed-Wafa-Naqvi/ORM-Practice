from django.contrib import admin
from django.urls import path,include
from ORM import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ORM.urls')),
]
