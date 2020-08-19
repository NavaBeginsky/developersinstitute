from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.contrib.auth.models import User 

# Create your views here.
class UserProfile(ListView):
    template_name = 'user_profile/profile.html'
    
    def get_queryset(self):
        self.user = get_object_or_404(User, username=self.kwargs['username'])
        liked = self.user.liked.all()
        # for hotel in liked:
        #     hotel['photos'] = hotel.hotelphotos_set.all()
        return liked

    # def get_context_data(self):
    #     super.
