from django.urls import path #path function
from . import views # . is shorthand for the current directory

# one urlpattern per line
urlpatterns = [
    path('', views.people, name='people'),
    path('<str:id_num>/', views.id, name='id_page')
]