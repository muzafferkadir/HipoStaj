from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.ListingRecipes, name='Recipes'),
    path('recipe/new', views.NewRecipe, name='New'),
    path('login',views.LoginPage,name ='Login'),
]