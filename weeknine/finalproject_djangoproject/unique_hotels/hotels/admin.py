from django.contrib import admin
from .models import Hotels, HotelPhotos, Location, Country

# Register your models here.

class PhotosInline(admin.StackedInline):
    model = HotelPhotos

class HotelsAdmin(admin.ModelAdmin):
    model = Hotels
    inlines = [PhotosInline]

admin.site.register(Hotels, HotelsAdmin)
admin.site.register(Location)
admin.site.register(Country)