from django.shortcuts import render,redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.utils import timezone
from .models import Recipe
from .forms import RecipeForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import AuthenticationForm

class RecipeListView(ListView):

    model = Recipe
    paginate_by = 2  # if pagination is desired
    template_name = '/'


def ListingRecipes(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipeList.html', {'recipes' : recipes})

def NewRecipe(request):
    form = RecipeForm()
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            #post.user = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('recipeList.html')
        else:

            print("asdasdad")   
    else:
        form = RecipeForm()
    return render(request, 'new.html', {'form': form})



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
    #username = request.POST.get('username')
    #password = request.POST.get('password')
    #user = authenticate(request,username=username,password=password)
    #if user is not None:
    #    login(request,user)
    #    return render(request,'login.html',locals())
    #else:
    #    print("HATALI GİRİŞ")
    #    return render(request,'login.html',locals())

