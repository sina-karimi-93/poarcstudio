from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='designs'),
    path('فارسی/', views.index_persian, name='designs_persian'),
    path('<int:design_id>', views.design, name='design'),
    path('فارسی/<int:design_id>', views.design_persian, name='design_persian'),
]
