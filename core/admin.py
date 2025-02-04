from django.contrib import admin
from .models import ServiceProvider

# Register your models here.

from dal import autocomplete

@admin.register(ServiceProvider)
class ServiceProviderAdmin(admin.ModelAdmin):
    search_fields = ["name", "location_name"]
    formfield_overrides = {
        ServiceProvider.location_name.field: {
            "widget": autocomplete.Select2(url="/admin/location-autocomplete/")
        }
    }
