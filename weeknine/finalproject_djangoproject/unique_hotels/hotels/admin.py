from django.contrib import admin
from .models import *

# Register your models here.

class PhotosInline(admin.StackedInline):
    model = HotelPhotos

class AmenitiesInline(admin.StackedInline):
    model = Amenities.hotel.through

class CategoryInline(admin.StackedInline):
    model = Categories.hotel.through

class CoordinatesInline(admin.StackedInline):
    model = Coordinates


class HotelsAdmin(admin.ModelAdmin):
    model = Hotels
    fields = ['name', 'location', 'unique_snippet', 'details', 'booking_website']
    inlines = [CoordinatesInline, PhotosInline, CategoryInline, AmenitiesInline]

admin.site.register(Hotels, HotelsAdmin)
admin.site.register(Location)
admin.site.register(Country)
admin.site.register(Categories)
admin.site.register(Amenities)