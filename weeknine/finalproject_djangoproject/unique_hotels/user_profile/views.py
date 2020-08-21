from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.contrib.auth.models import User 
from hotels.models import Hotels

# Create your views here.
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

