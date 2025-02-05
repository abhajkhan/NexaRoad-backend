from django.db import models

class Service(models.Model):
    name=models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class ServiceProvider(models.Model):
    name = models.CharField(max_length=255)
    service_type = models.ForeignKey(Service, on_delete=models.CASCADE)  
    mobile_number = models.CharField(max_length=15)
    location_name = models.CharField(max_length=255, blank=True, null=True)  # Autocomplete Field
    # latitude = models.FloatField()
    # longitude = models.FloatField()

    def __str__(self):
        return f"{self.name} - {self.service_type} ({self.location_name})"
