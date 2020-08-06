from django.shortcuts import render
from phonenumber_field.formfields import PhoneNumberField

# Create your views here.
def search_form(request):
    my_phone_field = ClientForm.phone()
    return render(request, 'search_form.html', {'phone_field': my_phone_field})

def display_results(request, search_type, search_input):
    pass

