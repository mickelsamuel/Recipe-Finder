from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    instructions = models.TextField()
    prep_time = models.IntegerField(help_text="Preparation time in minutes")
    cook_time = models.IntegerField(help_text="Cooking time in minutes")
    # Nutritional information
    calories = models.FloatField(help_text="Calories per serving")
    protein = models.FloatField(help_text="Protein content in grams per serving", null=True, blank=True)
    carbohydrates = models.FloatField(help_text="Carbohydrates in grams per serving", null=True, blank=True)
    fats = models.FloatField(help_text="Fats in grams per serving", null=True, blank=True)

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.CharField(max_length=255)
    recipe = models.ForeignKey(Recipe, related_name='ingredients', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.quantity} of {self.name}"

from django.contrib.auth.models import User

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    added_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'recipe')  # Each user can only have one instance of each recipe as a favorite

    def __str__(self):
        return f"{self.user}'s favorite: {self.recipe.name}"
