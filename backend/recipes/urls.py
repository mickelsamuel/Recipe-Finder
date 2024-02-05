from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RecipeSearchAPIView, FavoriteViewSet

# Create a router for any viewsets
router = DefaultRouter()
router.register(r'favorites', FavoriteViewSet, basename='favorite')

# Define URL patterns
urlpatterns = [
    path('search/', RecipeSearchAPIView.as_view(), name='recipe-search'),  # Endpoint for searching recipes
    path('', include(router.urls)),  # Include routes created by the router for favorites
]
