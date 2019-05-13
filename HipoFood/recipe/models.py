from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

DIFFICULTY = (
    ('BEGINNER', _('Beginner')),
    ('EASY', _('Easy')),
    ('NORMAL', _('Normal')),
    ('HARD', _('Hard')),
    ('EXPERT', _('Expert')),
    
)

class Ingredient(models.Model):
    ingredient = models.CharField(max_length=40)

    def __str__(self):
        return self.ingredient


class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    description = models.TextField()
    image = models.ImageField(upload_to = 'recipe/',null=True,blank=True)
    difficulty = models.CharField(max_length=45, choices=DIFFICULTY)
    ingredients = models.ManyToManyField(Ingredient)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    
    def __unicode__ (self):
        return self.user.name