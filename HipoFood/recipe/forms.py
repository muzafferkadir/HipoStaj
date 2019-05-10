from django import forms

from .models import Recipe

class RecipeForm(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = ('user', 'name', 'description','image','difficulty','ingredients',
        'votes')