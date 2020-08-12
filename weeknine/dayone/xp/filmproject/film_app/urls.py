from django.urls import path, include
from . import views

urlpatterns = [
    path('homepage/', views.homepage, name='homepage'),
    path('addfilm/', views.AddFilm.as_view(), name='addFilm'),
    path('adddirector/', views.AddDirector.as_view(), name='addDirector')
]