from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, UpdateView
from django.contrib.auth.models import User 
from hotels.models import Hotels
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from .forms import UpdateUserForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
@method_decorator(login_required, name='dispatch')
class UpdateProfile(SuccessMessageMixin, UpdateView):
    template_name = 'user_profile/update_profile.html'
    form_class = UpdateUserForm

    def get_object(self):
        return self.request.user
    
    def get_success_url(self):
        return self.request.path

class UserProfile(ListView):
    template_name = 'user_profile/profile.html'
    
    def get_queryset(self):
        self.user = get_object_or_404(User, username=self.kwargs['username'])
        return self.user.liked.all()

# def update_loved_hotel():
#     user = get_object_or_404(User, username=self.kwargs['username'])
#     hotel = Hotels.objects.get(pk=request.POST["hotel_pk"])
#     if hotel in Hotels.objects.filter(liked_by_user=user):
#         hotel.liked_by_user.remove(user)
#     else:
#         hotel.liked_by_user.add(user)
    
#     return UserProfile.as_view()


