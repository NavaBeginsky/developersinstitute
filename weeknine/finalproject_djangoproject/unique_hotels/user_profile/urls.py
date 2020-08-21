from django.urls import path
from . import views

urlpatterns = [
    path('user/<str:username>', views.UserProfile.as_view(), name='profile'),
  
]