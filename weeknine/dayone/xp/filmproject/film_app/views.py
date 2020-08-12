from django.shortcuts import render
from django.views import generic
from .forms import AddFilmForm, AddDirectorForm
from django.urls import reverse

# Create your views here.
def homepage(request):
    return render(request, 'partials/homepage.html')

class AddFilm(generic.CreateView):
    template_name = 'film/add_film.html'
    form_class = AddFilmForm

def addDirector(request):
    if request.method == 'GET':
        return render(request, 'director/add_director.html', {'form': AddDirectorForm})

    else:
        form = AddDirectorForm(request.POST)
        if form.is_valid():
            form.save()