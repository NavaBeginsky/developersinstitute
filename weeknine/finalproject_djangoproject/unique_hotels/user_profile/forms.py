from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django import forms
from .models import UserProfilePic

class UpdateUserForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class UpdatePictureForm(forms.ModelForm):
    profile_pic = forms.ImageField(error_messages = {'invalid':("Image files only")}, widget=forms.FileInput)

    class Meta:
        model = UserProfilePic
        fields = ['profile_pic']
