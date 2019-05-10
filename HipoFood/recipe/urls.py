from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.recipe_list, name='recipe_list'),
    path('recipe/new', views.recipe_new, name='recipe_new'),
    path('login',views.loginPage,name ='login'),
]