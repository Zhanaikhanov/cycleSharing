from django.contrib import admin

# Register your models here.
from bicycle.models import Bicycle, BicycleRent

admin.site.register(Bicycle)
admin.site.register(BicycleRent)

