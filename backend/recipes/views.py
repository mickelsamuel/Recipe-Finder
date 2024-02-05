from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
import requests
from django.conf import settings  # For API keys stored in settings.py

# Helper function to handle API requests with rate limit considerations
def make_external_api_request(url, params):
    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json(), None  # Successful request, return data and no error
        elif response.status_code == 429:  # Common status code for rate limits
            return None, "API rate limit exceeded. Please try again later."
        else:
            return None, f"External API error: {response.status_code}"
    except requests.exceptions.RequestException as e:
        return None, f"Request failed: {str(e)}"

# View for searching recipes using an external API
class RecipeSearchAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        query = request.query_params.get('s')  # 's' parameter for searching by name in TheMealDB
        url = "https://www.themealdb.com/api/json/v1/1/search.php"

        params = {"s": query}

        data, error = make_external_api_request(url, params)
        if error:
            return Response({"error": error}, status=status.HTTP_503_SERVICE_UNAVAILABLE)
        return Response(data, status=status.HTTP_200_OK)

# Assuming you have a model and serializer for Favorites, you can use a ViewSet as before
# from rest_framework import viewsets
# from .models import Favorite
# from .serializers import FavoriteSerializer
# class FavoriteViewSet(viewsets.ModelViewSet):
#     ...
