from django.shortcuts import render, redirect
from .models import Hotels, HotelPhotos
from random import choice
from django.contrib.auth.decorators import login_required
from users import models

# Create your views here.
def choose_hotel(current_user):
    if current_user.is_authenticated:
        unjudged_hotels = Hotels.objects.exclude(liked_by_user=current_user).exclude(rejected_by_user=current_user)
        if len(unjudged_hotels) == 0: #if the user has judged all the hotels on the site
            return False
    else:
        unjudged_hotels = Hotels.objects.all()
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

        else:
            return redirect('login')
        
    chosen_hotel = choose_hotel(current_user)
    if chosen_hotel == False:
        return render(request, 'hotels/nohotels.html')

    return render(request, 'hotels/showhotels.html', {'hotel': chosen_hotel})

