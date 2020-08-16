from django.shortcuts import render, redirect
from .models import Hotels, HotelPhotos
from random import choice
from django.contrib.auth.decorators import login_required
from users import models

# Create your views here.
def choose_hotel():
    return choice(Hotels.objects.all())


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
        
    chosen_hotel = choose_hotel()
    context = {
        'hotel': chosen_hotel,
        'photos': chosen_hotel.hotelphotos_set.all()
    }
    return render(request, 'hotels/showhotels.html', context)

