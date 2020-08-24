from django import forms


class HomeForm(forms.Form):
    fullname = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control mb-1",
        "placeholder": "Full Name"
    }), label='')
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        "class": "form-control mb-1",
        "placeholder": "E-mail"
    }), label='')
    message = forms.CharField(widget=forms.Textarea(attrs={
        "class": "form-control mb-1",
        "placeholder": "Message"
    }), label='')


class HomePersianForm(forms.Form):
    fullname = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control mb-1",
        "placeholder": "اسم"
    }), label='')
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        "class": "form-control mb-1",
        "placeholder": "ایمیل"
    }), label='')
    message = forms.CharField(widget=forms.Textarea(attrs={
        "class": "form-control mb-1",
        "placeholder": "پیام"
    }), label='')
