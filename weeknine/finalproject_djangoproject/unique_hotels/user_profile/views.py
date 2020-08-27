from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, UpdateView, DeleteView
from django.contrib.auth.models import User 
from hotels.models import Hotels
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from .forms import UpdateUserForm, UpdatePictureForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import UserProfilePic
from django.contrib.auth.views import PasswordChangeView
from hotels.views import filter_hotels
from hotels.forms import CategoryForm, AmenityForm
from django.http import JsonResponse
from django.core import serializers

# Create your views here.
@method_decorator(login_required, name='dispatch')
class UpdateProfile(SuccessMessageMixin, UpdateView):
    template_name = 'user_profile/update_profile.html'
    form_class = UpdateUserForm
    success_message = 'Update Successful!'

    def get_object(self):
        return self.request.user
    
    def get_success_url(self):
        return self.request.path

@method_decorator(login_required, name='dispatch')
class UpdateProfilePhoto(SuccessMessageMixin, UpdateView):
    template_name = 'user_profile/update_photo.html'
    form_class = UpdatePictureForm
    success_message = 'Profile Photo Updated Successfully!'

    def get_initial(self):
        return {'user': self.request.user}

    def get_object(self):
        return self.request.user.userprofilepic
    
    def get_success_url(self):
        return self.request.path

    def form_valid(self, form):
        super(UpdateProfilePhoto, self).form_valid(form)
        print(form.cleaned_data)
        return redirect(self.get_success_url())

        
class UpdatePassword(SuccessMessageMixin, PasswordChangeView):
    template_name = 'user_profile/change_password.html'
    success_message = 'Password Updated Successfully!'

    def get_success_url(self):
        return self.request.path

class DeleteAccount(DeleteView):
    model = User
    template_name = 'user_profile/delete_profile.html'
    success_url = '/'

    def get_object(self):
        return self.request.user



class UserProfile(ListView):
    template_name = 'user_profile/profile.html'
    
    def get_queryset(self):
        self.user_profile = get_object_or_404(User, username=self.kwargs['username'])
        hotels = filter_hotels(self.user_profile.liked.all(), self.request.GET.getlist('categories'), self.request.GET.getlist('amenities'))
        return hotels

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)        
        context['cat_form'] = CategoryForm(self.request.GET)
        context['amen_form'] = AmenityForm(self.request.GET)
        context['self'] = True if self.request.user == self.user_profile else False
        return context

def likeUnlike(request):
    current_user = request.user
    if request.is_ajax and request.method == "POST":
        hotel = Hotels.objects.get(pk=request.POST.get('hotel_pk'))
        if hotel in Hotels.objects.filter(liked_by_user=current_user):
            hotel.liked_by_user.remove(current_user)
        else:
            hotel.liked_by_user.add(current_user)
        return JsonResponse({"success": "like/unlike successful"}, status=200)
    else:
        return JsonResponse({"error": "like/unlike did not go through"}, status=400)




# def update_loved_hotel():
#     user = get_object_or_404(User, username=self.kwargs['username'])
#     hotel = Hotels.objects.get(pk=request.POST["hotel_pk"])
#     if hotel in Hotels.objects.filter(liked_by_user=user):
#         hotel.liked_by_user.remove(user)
#     else:
#         hotel.liked_by_user.add(user)
    
#     return UserProfile.as_view()


