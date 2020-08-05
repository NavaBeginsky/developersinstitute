from django.db import models

# Create your models here.
class Family(models.Model):
    name = models.CharField(max_length=50)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

class Animal(models.Model):
    name = models.CharField(max_length=50, null=True)
    legs = models.IntegerField()
    weight = models.IntegerField()
    height = models.FloatField()
    speed = models.IntegerField()
    family = models.ForeignKey(Family, on_delete=models.CASCADE)

    def __str__(self):
        return self.name