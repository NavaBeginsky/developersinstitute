from django.db import models
import datetime

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=100)

class Category(models.Model):
    name = models.CharField(max_length=100)

class Director(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

class Film(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField(default=datetime.date.today)
    created_in_country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, related_name='created')
    available_in_countries = models.ManyToManyField(Country, related_name='available')
    category = models.ManyToManyField(Category)
    director = models.ManyToManyField(Director)