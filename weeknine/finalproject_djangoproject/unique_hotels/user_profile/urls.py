from django.urls import path
from . import views

urlpatterns = [
    path('update-profile/', views.UpdateProfile.as_view(), name='update_profile'),
    path('<str:username>/', views.UserProfile.as_view(), name='profile')  
]