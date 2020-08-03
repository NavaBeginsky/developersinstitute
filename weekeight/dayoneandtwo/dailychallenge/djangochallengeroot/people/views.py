from django.shortcuts import render # this line is added automatically
from django.http import HttpResponse # pass view information into the browser

people_list = [
  {
    'id': 1,
    'name': 'Bob Smith',
    'age': 35,
    'country': 'USA'
  },
  {
     'id': 2,
    'name': 'Martha Smith',
    'age': 60,
    'country': 'USA'
  },
  {
     'id': 3,
    'name': 'Fabio Alberto',
    'age': 18,
    'country': 'Italy'
  },
  {
     'id': 4,
    'name': 'Dietrich Stein',
    'age': 85,
    'country': 'Germany'
  }
]

# Create your views here.
def people(request):
    return render(request, 'people/people.html', {'people': people_list})

def id(request, id_num):
    
    for person in people_list:
        if person['id'] == (int(id_num)):
            person_info = person
            return render(request, 'people/id.html', {'person': person_info})