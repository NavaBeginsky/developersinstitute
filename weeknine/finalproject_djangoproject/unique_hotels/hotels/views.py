from django.shortcuts import render, redirect
from .models import Hotels, HotelPhotos
from random import choice
from django.contrib.auth.decorators import login_required
from users import models
from .forms import CategoryForm, AmenityForm

# Create your views here.


def choose_hotel(current_user, *args):
    if current_user.is_authenticated:
        unjudged_hotels = Hotels.objects.exclude(liked_by_user=current_user).exclude(
            rejected_by_user=current_user).exclude(approved=False)
        if len(unjudged_hotels) == 0:  # if the user has judged all the hotels on the site
            return False
    else:
        unjudged_hotels = Hotels.objects.exclude(approved=False)

    for category in args[0]:
        unjudged_hotels = unjudged_hotels.filter(categories=category) 

    for amenity in args[1]:
        unjudged_hotels = unjudged_hotels.filter(amenities=amenity) 
        
    return choice(unjudged_hotels)


def show_hotels(request):
    current_user = request.user
    if request.method == 'POST':
        if current_user.is_authenticated:
            hotel = Hotels.objects.get(pk=request.POST.get('hotel_pk'))
            if 'like' in request.POST:
                current_user.liked.add(hotel)
            if 'reject' in request.POST:
                current_user.rejected.add(hotel)

        elif 'skip' not in request.POST:  # user should be able to skip through hotels even if not logged in
            return redirect('login')

    chosen_hotel = choose_hotel(current_user, request.GET.getlist('categories'), request.GET.getlist('amenities'))
    if chosen_hotel == False:
        return render(request, 'hotels/nohotels.html')

    context = {
        'hotel': chosen_hotel,
        'cat_form': CategoryForm(request.GET),
        'amen_form': AmenityForm(request.GET)
    }

    return render(request, 'hotels/showhotels.html', context)
