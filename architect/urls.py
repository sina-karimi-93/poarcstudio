from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='designers'),
    path('فارسی/', views.index_persian, name='designers_persian'),
]
