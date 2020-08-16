from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Location(models.Model):
    city = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('city', 'country')

    def __str__(self):
        return self.city + ', ' + self.country.name

class Hotels(models.Model):
    name = models.CharField(max_length=100)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    details = models.CharField(max_length=1000)
    liked_by_user = models.ManyToManyField(User, related_name='liked')
    rejected_by_user = models.ManyToManyField(User, related_name='rejected')

    def __str__(self):
        return self.name
   
class HotelPhotos(models.Model):
    image = models.ImageField()
    hotel = models.ForeignKey(Hotels, on_delete=models.CASCADE)    

    def __str__(self):
        return self.hotel.name

class Categories(models.Model):
    name = models.CharField(max_length=100)
    hotel = models.ManyToManyField(Hotels)
    
    def __str__(self):
        return self.name

class Amenities(models.Model):
    name = models.CharField(max_length=100)
    hotel = models.ManyToManyField(Hotels)

    def __str__(self):
        return self.name
