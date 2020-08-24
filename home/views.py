from django.shortcuts import render, redirect
from .models import Home
from django.core.mail import send_mail
from .forms import HomeForm, HomePersianForm
from django.contrib import messages


# Create your views here.


def index(request):
    queryset = Home.objects.all()
    # Form
    form = HomeForm(request.POST or None)
    sent = False
    if request.method == 'POST':
        if form.is_valid():
            form_name = form.cleaned_data.get('fullname')
            form_email = form.cleaned_data.get('email')
            form_message = form.cleaned_data.get('message')
            # Preparing send_mail requirements
            subject = f"{form_name} sent you a message from Poarc Studio's home page"
            message = f"his/her email is : {form_email}\n{form_message}"
            send_mail(subject, message, 'sinakmi70@gmail.com', ['sinakmi70@gmail.com'], )
            sent = True
            messages.success(request, 'Your Message has been successfully sent')
            form = HomeForm()

    context = {
        'home': queryset,
        'form': form,
        'sent': sent
    }
    return render(request, 'home/home.html', context)


def index_persian(request):
    queryset = Home.objects.all()
    form = HomePersianForm(request.POST or None)
    sent = False
    if request.method == 'POST':
        if form.is_valid():
            form_name = form.cleaned_data.get('fullname')
            form_email = form.cleaned_data.get('email')
            form_message = form.cleaned_data.get('message')
            # Preparing send_mail requirements
            subject = f"{form_name} sent you a message from Poarc Studio's home page"
            message = f"his/her email is : {form_email}\n{form_message}"
            send_mail(subject, message, 'sinakmi70@gmail.com', ['sinakmi70@gmail.com'], )
            sent = True
            messages.success(request, 'Your Message has been successfully sent')
            form = HomePersianForm()
    context = {
        'persian_home': queryset,
        'form': form,
        'sent': sent
    }
    return render(request, 'home/home_persian.html', context)


def registration(request):
    sent = False
    if request.method == 'POST':
        yourname = request.POST.get('yourname')
        email = request.POST.get('email')
        location = request.POST.get('location')
        phone = request.POST.get('phone')
        # Getting Checkbox Valu
        if request.POST.get('3dsmax') == '3dsMax':
            dsmax = '3dsMax'
        else:
            dsmax = ''

        if request.POST.get('revit') == 'Revit':
            revit = 'Revit'
        else:
            revit = ''

        if request.POST.get('lumion') == 'Lumion':
            lumion = 'Lumion'
        else:
            lumion = ''

        if request.POST.get('photoshop') == 'Photoshop':
            photoshop = 'Photoshop'
        else:
            photoshop = ''

        if request.POST.get('autocad') == 'Autocad':
            autocad = 'Autocad'
        else:
            autocad = ''
        description = request.POST.get('description')
        subject = f'{yourname} submit a project from "Project Registration"'
        message = f"Customer Name : {yourname}\n\n" \
                  f"Customer E-mail : {email}\n\n" \
                  f"Customer Phone : {phone}\n\n" \
                  f"Customer Location: {location}\n\n" \
                  f"Required Tools : {dsmax} {revit} {photoshop} {lumion} {autocad}\n\n" \
                  f"Customer Description : {description}"
        send_mail(subject, message, 'sinakmi70@gmail.com', ['sinakmi70@gmail.com'])
        messages.success(request, 'Your project has been successfully registered')
        sent = True

    context = {
        'sent': sent
    }
    return render(request, 'home/registration.html', context)


def registration_persian(request):
    sent = False
    if request.method == 'POST':
        yourname = request.POST.get('yourname')
        email = request.POST.get('email')
        location = request.POST.get('location')
        phone = request.POST.get('phone')
        # Getting Checkbox Valu
        if request.POST.get('3dsmax') == '3dsMax':
            dsmax = '3dsMax'
        else:
            dsmax = ''

        if request.POST.get('revit') == 'Revit':
            revit = 'Revit'
        else:
            revit = ''

        if request.POST.get('lumion') == 'Lumion':
            lumion = 'Lumion'
        else:
            lumion = ''

        if request.POST.get('photoshop') == 'Photoshop':
            photoshop = 'Photoshop'
        else:
            photoshop = ''

        if request.POST.get('autocad') == 'Autocad':
            autocad = 'Autocad'
        else:
            autocad = ''
        description = request.POST.get('description')
        subject = f'{yourname} یک پروژه از قسمت ثبت پروژه ارسال کرده است .'
        message = f"Customer Name : {yourname}\n\n" \
                  f"Customer E-mail : {email}\n\n" \
                  f"Customer Phone : {phone}\n\n" \
                  f"Customer Location: {location}\n\n" \
                  f"Required Tools : {dsmax} {revit} {photoshop} {lumion} {autocad}\n\n" \
                  f"Customer Description : {description}"
        send_mail(subject, message, 'sinakmi70@gmail.com', ['sinakmi70@gmail.com'])
        messages.success(request, 'پروژه شما با موفقیت ارسال شد')
        sent = True

    context = {
        'sent': sent
    }
    return render(request, 'home/registration_persian.html', context)
