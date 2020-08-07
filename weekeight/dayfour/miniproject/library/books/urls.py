from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.virtualLibrary, name='library'),
    path('<str:booktitle>/', views.myBook, name='mybook')
]