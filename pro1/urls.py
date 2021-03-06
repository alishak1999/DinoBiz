"""pro1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from accounts import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home,name="home"),
    path('home/get_started/',views.get_started,name="get_started"),
    path('home/get_started/login_cust',views.login_cust, name="login_cust"),
    path('home/get_started/login_seller',views.login_seller, name="login_seller"),
    path('home/get_started/cust_reg',views.cust_reg,name="cust_reg"),
    path('home/get_started/seller_reg',views.seller_reg,name="seller_reg"),
    path('customer/<str:c_pk>/',views.test2,name="customer"),
    path('seller/',views.test1,name="seller"),
    path('order_update/<str:pk>/',views.orderUpdate,name="orderUpdate"),
    path('uhome/', views.userHome, name="uHome"),
    path('uprofile/', views.userProfile, name="uProfile"),
    path('sellerpage/<str:pk>/', views.order, name="order"),
    path('usercart/', views.cart, name="cart"),
    path('updatecart/', views.updateItem, name="updatecart"),
    path('orders/', views.vieworders, name="orders"),
    path('sprofile/', views.sellerProfile, name="sProfile"),
    path('productsAdd/', views.productsAdd, name="productsAdd"),
    path('p_update/', views.productsUpdate, name="productsUpdate"),
    path('viewprod/', views.viewProducts, name="viewProducts"),

    
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
