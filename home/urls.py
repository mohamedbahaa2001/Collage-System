from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('userprofile', views.userprofile, name='userprofile'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('qrcode', views.qrcode,name='qrcode'),
    path('quiz', views.quiz,name='quiz'),
]
