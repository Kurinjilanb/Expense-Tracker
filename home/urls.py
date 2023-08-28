from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('register/',views.register,name='register'),
    path('handleSignup/',views.handleSignup,name='handleSignup'),
    path('handlelogin/',views.handlelogin,name='handlelogin'),
    path('handleLogout/',views.handleLogout,name='handleLogout'),
    path('addmoney/',views.addmoney,name='addmoney'),
    path('addmoney_submission/',views.addmoney_submission,name='addmoney_submission'),
    path('tables/',views.tables,name='tables'),
    path('expense_edit/<int:id>',views.expense_edit,name='expense_edit'),
    path('<int:id>/addmoney_update/', views.addmoney_update, name="addmoney_update") ,
    path('expense_delete/<int:id>',views.expense_delete,name='expense_delete'),
    path('profile/',views.profile,name = 'profile'),
    path('weekly/',views.weekly, name = 'weekly'),
    path('<int:id>/profile_edit/',views.profile_edit,name="profile_edit"),
    path('<int:id>/profile_update/',views.profile_update,name="profile_update"),   
]