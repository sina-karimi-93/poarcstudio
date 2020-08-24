from django.shortcuts import render, get_object_or_404, redirect
from .models import Design
from django.views.generic import DetailView, ListView
from django.core.mail import send_mail
from django.contrib import messages
from django.core.paginator import EmptyPage, Paginator, PageNotAnInteger


# Create your views here.


def index(request):
    queryset = Design.objects.order_by('-design_upload_date').filter(published=True)
    paginator = Paginator(queryset, 4)
    page = request.GET.get('page')
    paged_designs = paginator.get_page(page)
    context = {
        'designs': paged_designs
    }
    return render(request, 'designs/designs.html', context)


def index_persian(request):
    queryset = Design.objects.order_by('-design_upload_date').filter(published=True)
    paginator = Paginator(queryset, 4)
    page = request.GET.get('page')
    paged_designs = paginator.get_page(page)
    context = {
        'designs': paged_designs
    }
    return render(request, 'designs/designs_persian.html', context)


def design(request, design_id):
    queryset = get_object_or_404(Design, pk=design_id)
    sent = False
    if request.method == 'POST':
        form_name = request.POST.get('name')
        form_email = request.POST.get('email')
        form_message = request.POST.get('message')
        subject = f'{form_name} sent you a message from Poarc Studio Site about {queryset.title} Design'
        message = f'his/her email is : {form_email}\n\n{form_message}'
        send_mail(subject, message, 'sinakmi70@gmail.com', ['sinakmi70@gmail.com'], )
        sent = True
        messages.success(request, 'Your Message has been successfully sent')
    context = {
        'design': queryset,
        'sent': sent
    }
    return render(request, 'designs/design.html', context)


def design_persian(request, design_id):
    queryset = get_object_or_404(Design, pk=design_id)
    sent = False
    if request.method == 'POST':
        form_name = request.POST.get('name')
        form_email = request.POST.get('email')
        form_message = request.POST.get('message')
        subject = f'{form_name} برای شما یک پیغام از قسمت فارسی سایت Poarc Studio درباره {queryset.عنوان} فرستاده.'
        message = f'his/her email is : {form_email}\n\n{form_message}'
        send_mail(subject, message, 'sinakmi70@gmail.com', ['sinakmi70@gmail.com'], )
        sent = True
        messages.success(request, 'نظر شما با موفقیت ارسال شد')
    context = {
        'design': queryset,
        'sent': sent
    }
    return render(request, 'designs/design_persian.html', context)
