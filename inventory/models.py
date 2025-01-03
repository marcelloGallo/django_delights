from django.db import models
# Create your models here.

class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)
    quantity = models.FloatField(default=0)
    unit = models.CharField(max_length=20)  # e.g., kg, liters, pieces
    price_per_unit = models.FloatField(default=0)
    
    def get_absolute_url(self):
        return "/ingredients"
    
    def __str__(self):
        return f"{self.name} ({self.quantity} {self.unit})"
    
class MenuItem(models.Model):
    name = models.CharField(max_length=100, unique=True)
    price = models.FloatField(default=0.00)
    
    def get_absolute_url(self):
        return "/menu"
    
    def available(self):
        return all(
            requirement.ingredient.quantity >= requirement.quantity
            for requirement in self.reciperequirement_set.all()
        )

    def __str__(self):
        return f"{self.name} (${self.price})"
    
class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0)

    class Meta:
        unique_together = ['menu_item', 'ingredient']
    
    def get_absolute_url(self):
        return "/menu"
    
    def __str__(self):
        return f"{self.menu_item.name} requires {self.quantity} {self.ingredient.unit} of {self.ingredient.name}"
    
class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.menu_item.name} purchased at {self.timestamp}"

    def get_absolute_url(self):
        return "/purchases"
    