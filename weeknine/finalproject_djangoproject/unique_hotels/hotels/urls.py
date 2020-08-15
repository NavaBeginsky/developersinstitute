from django.urls import path, include
from . import views

urlpatterns = [
    path('action/<str:action>', views.user_choice, name = 'user_choice'),
    path('', views.show_hotels, name = 'show_hotels'),
]