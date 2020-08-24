from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('فارسی/', views.index_persian, name='persian_home'),
    path('registration/', views.registration, name='registration'),
    path('registration/فارسی', views.registration_persian, name='registration_persian'),

]
