from django.shortcuts import render, redirect
from .models import Hotels, HotelPhotos
from random import choice
from django.contrib.auth.decorators import login_required
from users import models

# Create your views here.


def choose_hotel():
    return choice(Hotels.objects.all())


def show_hotels(request):
    chosen_hotel = choose_hotel()
    current_user = request.user
    # if the current user is logged in, store the hotel they are currently being shown so we can categorize it later for them.
    if current_user.is_authenticated:
        models.UserLastViewedHotel.objects.create(
            user=current_user, last_viewed=chosen_hotel)
    context = {
        'hotel': chosen_hotel,
        'photos': chosen_hotel.hotelphotos_set.all()
    }
    return render(request, 'showhotels.html', context)


@login_required
def user_choice(request, action):
    current_user = request.user
    current_hotel = models.UserLastViewedHotel.objects.get(
        user=current_user).last_viewed
    if action == 'like':
        models.UserLikedHotels.objects.create(
            user=current_user, hotel=current_hotel)
    elif action == 'reject':
        models.UserRejectedHotels.objects.create(
            user=current_user, hotel=current_hotel)

    return redirect('show_hotels')
