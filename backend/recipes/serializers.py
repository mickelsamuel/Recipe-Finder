from rest_framework import serializers
from .models import Recipe, Ingredient, Favorite
from django.contrib.auth.models import User

# Serializer for the Ingredient model
class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'name', 'quantity']  # Assuming these are the fields in your Ingredient model

# Serializer for the Recipe model
class RecipeSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True, read_only=True)  # Nested serializer for ingredients

    class Meta:
        model = Recipe
        fields = ['id', 'name', 'description', 'instructions', 'prep_time', 'cook_time', 'calories', 'protein', 'carbohydrates', 'fats', 'ingredients']  # Include all relevant fields

# Serializer for the Favorite model
class FavoriteSerializer(serializers.ModelSerializer):
    recipe = RecipeSerializer(read_only=True)  # Nested serializer to show recipe details in favorites
    user = serializers.PrimaryKeyRelatedField(read_only=True)  # Only show the user's ID

    class Meta:
        model = Favorite
        fields = ['id', 'user', 'recipe', 'added_on']  # Include all relevant fields

# Optionally, if you want to include user serialization (e.g., for user registration or profile endpoints)
class UserSerializer(serializers.ModelSerializer):
    favorites = FavoriteSerializer(many=True, read_only=True)  # Nested serializer to show user's favorites

    class Meta:
        model = User
        fields = ['id', 'username', 'favorites']  # Include fields you want to expose about the user

