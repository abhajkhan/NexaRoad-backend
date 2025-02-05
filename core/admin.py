from django.contrib import admin
from .models import ServiceProvider, Service
from dal import autocomplete
from dal import autocomplete


# Register your models here.
admin.site.register(Service)

@admin.register(ServiceProvider)
class ServiceProviderAdmin(admin.ModelAdmin):
    list_display = ['name', 'location_name']
    search_fields = ['name', 'location_name']

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['location_name'].widget = autocomplete.Select2(
            url='location-autocomplete',
            attrs={
                'data-placeholder': 'Search for a location...',
                'data-minimum-input-length': 2,  # Minimum characters to trigger search
            },
        )
        return form
    
