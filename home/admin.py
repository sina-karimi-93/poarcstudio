from django.contrib import admin
from .models import Home


# Register your models here.


class HomeAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone', 'office_phone')


admin.site.register(Home, HomeAdmin)



