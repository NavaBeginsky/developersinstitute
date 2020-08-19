from django.db import models
from django.contrib.auth.models import User
from annoying.fields import AutoOneToOneField

# Create your models here.
class UserProfilePic(models.Model):
    user = AutoOneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='media', default='avatar.png')

    def __str__(self):
        return str(self.user)