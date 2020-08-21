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
        extra=3
        )
    if request.method == 'POST':
        hotel_form = AddHotelForm(request.POST)
        photos_formset = imageFormSet(request.POST, request.FILES)
        if hotel_form.is_valid() and photos_formset.is_valid():
            country, created = models.Country.objects.get_or_create(name = hotel_form.cleaned_data['country'])
            location = models.Location.objects.get_or_create(city=hotel_form.cleaned_data['city'], country=country)
            hotel = hotel_form.save(commit=False)
            hotel.location = location
            hotel.approved = False
            hotel.save()
            
            for form in photos_formset.cleaned_data:
                models.HotelPhotos(image=form['image'], hotel=hotel).save()
            
            for category in hotel_form.cleaned_data['categories']:
                cat = models.Categories.objects.get(name=category)
                models.Categories.hotel.add(cat)
            
            for amenity in hotel_form.cleaned_data['amenities']:
                amenity = models.Categories.objects.get(name=amenity)
                models.Amenities.hotel.add(cat)
            
            messages.success(request, 'Form submission successful')
            
    context = {
        'form': AddHotelForm,
        'photos_formset': imageFormSet(queryset=models.HotelPhotos.objects.none())
    }
    return render(request, 'contact/addhotel.html', context)

   