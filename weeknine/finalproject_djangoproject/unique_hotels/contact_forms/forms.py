from django import forms
from hotels import models

class AddHotelForm(forms.ModelForm):
    class Meta:
        model = models.Hotels
        fields = ['name', 'unique_snippet', 'details', 'booking_website']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        possible_categories = models.Categories.objects.all() 
        self.fields['categories'] = forms.ModelMultipleChoiceField(
            widget=forms.CheckboxSelectMultiple,
            queryset=possible_categories,
            required=False)
        possible_amenities = models.Amenities.objects.all()
        self.fields['amenities'] = forms.ModelMultipleChoiceField(
            widget=forms.CheckboxSelectMultiple,
            queryset=possible_amenities,
            required=False)
        self.fields['city'] = forms.CharField(max_length=100)
        self.fields['country'] = forms.CharField(max_length=50)
        

class HotelPhotosForm(forms.ModelForm):
    class Meta:
        model = models.HotelPhotos
        fields = ['image']
