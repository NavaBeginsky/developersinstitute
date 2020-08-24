from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class UserSignUpForm(UserCreationForm):
    email = forms.EmailField(required = True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2']
        
    def __init__(self, *args, **kwargs):
        super(UserSignUpForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
    
    def save(self, commit=True):
        new_user = super(UserSignUpForm, self).save(commit=False)
        new_user.email = self.cleaned_data['email']
        new_user.save()
        return new_user