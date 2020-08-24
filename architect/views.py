from django.shortcuts import render, get_object_or_404
from .models import Architect


# Create your views here.

def index(request):
    queryset = Architect.objects.order_by('-hired_date')
    context = {
        'designers': queryset
    }
    return render(request, 'architects/designers.html', context)


def index_persian(request):
    queryset = Architect.objects.order_by('-تاریخ_استخدام')
    context = {
        'persian_designer': queryset
    }
    return render(request, 'architects/designers_persian.html', context)
