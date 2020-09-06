from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Hotels, HotelPhotos, Amenities, Categories, Coordinates, Location, Country

# Register your models here.

class PhotosInline(admin.StackedInline):
    model = HotelPhotos

class AmenitiesInline(admin.StackedInline):
    model = Amenities.hotel.through

class CategoryInline(admin.StackedInline):
    model = Categories.hotel.through

class CoordinatesInline(admin.StackedInline):
    model = Coordinates


class HotelsAdmin(OSMGeoAdmin):
    model = Hotels
    fields = ['name', 'location', 'point_coordinates', 'unique_snippet', 'details', 'booking_website', 'approved']
    inlines = [CoordinatesInline, PhotosInline, CategoryInline, AmenitiesInline]

admin.site.register(Hotels, HotelsAdmin)
admin.site.register(Location)
admin.site.register(Country)
admin.site.register(Categories)
admin.site.register(Amenities)