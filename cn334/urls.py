"""
URL configuration for cn334 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),  # 127.00.1:8000/admin
    path('', index, name="index"),  # 127.00.1:8000/
    path('test/', test, name="test"),  # 127.00.1:8000/test
    path('home/', home, name='home'),  # 127.00.1:8000/home
    path('category/', category,name='category'),  # 127.00.1:8000/home/category
    path('product/', product, name='product'),  # 127.00.1:8000/home/product
    path('checkout/', checkout,name='checkout'),  # 127.00.1:8000/home/checkout
    path('contact/', contact, name='Contact'),  # 127.00.1:8000/home/Contact
]
