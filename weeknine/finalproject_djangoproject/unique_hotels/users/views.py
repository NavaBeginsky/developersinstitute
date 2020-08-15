from django.shortcuts import render, redirect
from .forms import UserSignUpForm
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.
class UserSignUp(generic.CreateView):
    template_name = 'registration/signup.html'
    model = User
    form_class = UserSignUpForm
    success_url = '/'
    failed_message = 'The signup did not go through'

    def form_valid(self, form):
        super(UserSignUp, self).form_valid(form)
        username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
        new_user = authenticate(username=username, password=password)

        if new_user == None:
            print('------------------------login after signup authentication fail')
            return self.render_to_response(self.get_context_data(form=form, failed_message=self.failed_message))

        else:
            login(self.request, new_user)
            return redirect(self.get_success_url())