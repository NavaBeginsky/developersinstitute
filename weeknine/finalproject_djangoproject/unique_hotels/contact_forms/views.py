from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .forms import AddHotelForm, HotelPhotosForm
from hotels import models
from django.contrib import messages
from django.forms.models import modelformset_factory


# Create your views here.
def addHotel(request):
    imageFormSet = modelformset_factory(
        models.HotelPhotos, 
        form=HotelPhotosForm, 
        extra=5
        )
    if request.method == 'POST':
        hotel_form = AddHotelForm(request.POST)
        photos_formset = imageFormSet(request.POST, request.FILES)
        if hotel_form.is_valid() and photos_formset.is_valid():
            country, created = models.Country.objects.get_or_create(name = hotel_form.cleaned_data['country'])
            location, created = models.Location.objects.get_or_create(city=hotel_form.cleaned_data['city'], country=country)
            hotel = hotel_form.save(commit=False)
            hotel.location = location
            hotel.approved = False
            hotel.save()

            images = photos_formset.save(commit=False)
            for image in images:
                image.hotel = hotel
                image.save()

            for category in hotel_form.cleaned_data['categories']:
                hotel.categories_set.add(category)
            
            for amenity in hotel_form.cleaned_data['amenities']:
                hotel.amenities_set.add(amenity)

            messages.success(request, 'Form submission successful')
            
    context = {
        'form': AddHotelForm,
        'photos_formset': imageFormSet(queryset=models.HotelPhotos.objects.none())
    }
    return render(request, 'contact/addhotel.html', context)

   