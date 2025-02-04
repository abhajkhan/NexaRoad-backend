from django.core.management.base import BaseCommand
from geopy.geocoders import Nominatim
from core.models import Location
import time

class Command(BaseCommand):
    help = "Fetch and store locations from Nominatim API for Kerala"

    def handle(self, *args, **kwargs):
        geolocator = Nominatim(user_agent="nexaroad")
        state = "Kerala"

        # Fetch multiple locations within Kerala
        locations = geolocator.geocode(state, exactly_one=False)

        if locations:
            for loc in locations:
                try:
                    Location.objects.get_or_create(name=loc.address)
                    self.stdout.write(self.style.SUCCESS(f"Added location: {loc.address}"))
                    # # Extract only relevant part of the address
                    # address = loc.address.split(",")[0]
                    
                    # # Save to database if not already present
                    # obj, created = Location.objects.get_or_create(name=address)
                    
                    # if created:
                    #     self.stdout.write(self.style.SUCCESS(f"Added location: {address}"))
                    # else:
                    #     self.stdout.write(self.style.WARNING(f"Location already exists: {address}"))

                    # Add delay to avoid API rate limits
                    time.sleep(1)
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"Error adding location: {e}"))
        else:
            self.stdout.write(self.style.ERROR("No locations found from Nominatim"))
