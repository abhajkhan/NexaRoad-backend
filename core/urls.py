from django.urls import path
from .views import NearbyServiceProvidersView, ServiceList

urlpatterns = [
    path('service-providers/', NearbyServiceProvidersView.as_view(), name='nearby-service-providers'),
    path('services/', ServiceList.as_view(), name='service-list'),  # Endpoint for getting all services

]
