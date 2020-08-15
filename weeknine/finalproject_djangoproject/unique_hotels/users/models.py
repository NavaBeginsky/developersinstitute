from django.db import models
from django.contrib.auth.models import User
from hotels.models import Hotels

# Create your models here.
class UserLastViewedHotel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    last_viewed = models.ForeignKey(Hotels, on_delete=models.CASCADE)

class UserLikedHotels(models.Model):
    user = models.ManyToManyField(User)
    hotel = models.ManyToManyField(Hotels)

class UserRejectedHotels(models.Model):
    user = models.ManyToManyField(User)
    hotel = models.ManyToManyField(Hotels)
