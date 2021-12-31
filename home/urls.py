from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    # path('about', views.about, name='about'),
    path('material', views.material, name='material'),
    path('contact', views.contact, name='contact'),
    path('userprofile', views.userprofile, name='userprofile'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('qrcode', views.qrcode,name='qrcode'),
]
