from django.contrib import admin
from .models import Area, Location, Measurement
# Register your models here.


class LocationInline(admin.TabularInline):
    model = Location

class MeasurementInline(admin.TabularInline):
    model = Measurement


class AreaAdmin(admin.ModelAdmin):
    inlines = [
        LocationInline,
    ]


class LocationAdmin(admin.ModelAdmin):
    inlines = [
        MeasurementInline,
    ]

admin.site.register(Area, AreaAdmin)
admin.site.register(Location, LocationAdmin)
