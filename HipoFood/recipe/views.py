from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.utils import timezone
from .models import Recipe
from .forms import RecipeForm
from django.contrib.auth.forms import *
from django.contrib.auth import *
from django.contrib.auth.decorators import *
from django.http import *

class RecipeListView(ListView):

    model = Recipe
    paginate_by = 2  # if pagination is desired
    template_name = '/'


def ListingRecipes(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipeList.html', {'recipes' : recipes})

def NewRecipe(request):
    form = RecipeForm()
    return render(request, 'new.html', {'form': form})
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
    else:
        form = RecipeForm()


def LoginPage(request):
    form = AuthenticationForm
    if(request.method=='POST'):
        username = request.method['username']
        password = request.method['password']
        giris_kontrol = AuthenticationForm(data=request.POST)
        if(giris_kontrol.is_valid()):
            kullanici = authenticate(username=username,password=password)
            login(request,kullanici)
            return HttpResponseRedirect('/')
    return render(request,'login.html',locals())
 
#def bilgi(request):
#    oku = request.user.id
#    if(not oku):
#        return HttpResponseRedirect('/')
#    return render(request,'bilgi.html',locals())

