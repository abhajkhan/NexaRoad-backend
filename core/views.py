import requests
from django.shortcuts import get_list_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from geopy.geocoders import Nominatim
from .models import ServiceProvider
from .serializers import ServiceProviderSerializer
from django.http import JsonResponse
from django.views import View

class NearbyServiceProvidersView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        latitude = request.GET.get('latitude')
        longitude = request.GET.get('longitude')

        if not latitude or not longitude:
            return Response({"error": "Latitude and longitude are required"}, status=400)

        # Convert coordinates to location name
        geolocator = Nominatim(user_agent="nexaroad")
        location = geolocator.reverse(f"{latitude}, {longitude}", exactly_one=True)
        print(location)

        if not location:
            return Response({"error": "Could not determine location"}, status=400)

        location_name = location.raw['address'].get('county', location.raw['address'].get('state', 'Unknown'))
        print(f"the location name is: {location_name}")

        # Filter service providers by location name
        providers = ServiceProvider.objects.filter(location_name=location_name)
        serializer = ServiceProviderSerializer(providers, many=True)
        
        return Response(serializer.data)



class LocationAutocomplete(View):
    def get(self, request):
        query = request.GET.get("q", "")
        print(f"the query is: {query}")
        if not query:
            return JsonResponse([], safe=False)

        url = f"https://nominatim.openstreetmap.org/search?q={query}&format=json&addressdetails=1"
        response = requests.get(url)
        print(f"the response is: {response}")
        locations = []

        if response.status_code == 200:
            data = response.json()
            for place in data[:5]:  # Limit results to 5
                locations.append({"id": place["display_name"], "text": place["display_name"]})

        return JsonResponse(locations, safe=False)
