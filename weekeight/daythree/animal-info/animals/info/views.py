from django.shortcuts import render
from .models import Family, Animal

# Create your views here.
def family_members(request, family_id):
    family_name = Family.objects.get(id=family_id)
    families_animals = Animal.objects.filter(family=family_id)
    context = {
        'animals': families_animals,
        'family_name': family_name
    }
    return render(request, 'display_animals.html', context)

def animal(request, animal_id):
    animal = Animal.objects.get(id=animal_id)
    return render(request, 'animal_info.html', {'animal': animal})

def all_animals(request):
    animals = Animal.objects.all()
    return render(request, 'display_animals.html', {'animals':animals})