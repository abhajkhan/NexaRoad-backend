from django.urls import path
from .views import NearbyServiceProvidersView

urlpatterns = [
    path('service-providers/', NearbyServiceProvidersView.as_view(), name='nearby-service-providers'),
]
