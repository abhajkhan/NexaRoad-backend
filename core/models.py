from django.db import models

class ServiceProvider(models.Model):
    name = models.CharField(max_length=255)
    service_type = models.CharField(max_length=50)  
    mobile_number = models.CharField(max_length=15)
    location_name = models.CharField(max_length=255, blank=True, null=True)  # Autocomplete Field
    # latitude = models.FloatField()
    # longitude = models.FloatField()

    def __str__(self):
        return f"{self.name} - {self.service_type} ({self.location_name})"
