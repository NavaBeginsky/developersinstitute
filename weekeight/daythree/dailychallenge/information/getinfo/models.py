from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = PhoneNumberField()
    address = models.CharField(max_length=300)

