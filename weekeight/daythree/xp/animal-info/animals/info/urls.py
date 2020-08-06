from django.urls import path, include
from . import views

urlpatterns = [
    path('family/<int:family_id>/', views.family_members, name='family_member_info'),
    path('animal/<int:animal_id>/', views.animal, name='animal_info'),
    path('animals/', views.all_animals, name='animals_all')
]