from django.contrib import admin
from .models import RecipeRequirement, MenuItem, Ingredient, Purchase
# Register your models here.
[admin.site.register(X) for X in [RecipeRequirement, MenuItem, Ingredient, Purchase]]