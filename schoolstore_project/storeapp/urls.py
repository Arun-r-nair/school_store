from . import views
from django.urls import path

# app_name = 'storeapp'

urlpatterns = [

    path('',views.home,name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('new/', views.new, name='new'),
    path('order/', views.order, name='order'),
]