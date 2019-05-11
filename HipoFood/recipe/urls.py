from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.ListingRecipes, name='Recipes'),
    path('new', views.NewRecipe, name='New'),
    path('login',views.LoginPage,name ='Login'),
    path('logout',views.LogoutPage,name='Logout'),
    path('register',views.NewUser,name='Register'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)