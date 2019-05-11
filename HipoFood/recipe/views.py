from django.shortcuts import render,redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.utils import timezone
from .models import Recipe
from .forms import RecipeForm,NewUserForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.core.paginator import Paginator
from django.db.models import Q

def ListingRecipes(request):
    recipes = Recipe.objects.all()
    query = request.GET.get('q')
    if query:
        recipes = recipes.filter(Q(name__icontains = query)|
                                Q(description__icontains = query))

    pagination = Paginator(recipes,4)
    page = request.GET.get('page')
    RecipeList = pagination.get_page(page)
    return render(request, 'recipeList.html', {'recipes' : RecipeList})

def NewRecipe(request):
    form = RecipeForm()
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('/')
        else:

            print("asdasdad")   
    else:
        form = RecipeForm()
    return render(request, 'new.html', {'form': form})

def NewUser(request):
    form = NewUserForm()
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('/')
    else:
        form = NewUserForm()
    return render(request,'register.html',{'form':form})

def LoginPage(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "login.html",
                    context={"form":form})

def LogoutPage(request):
    logout(request)
    return redirect('/')
