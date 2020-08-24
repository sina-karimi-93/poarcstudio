from django.contrib import admin
from .models import Architect


# Register your models here.


class ArchitectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'software_tools', 'education')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'education', 'software_tools', 'phone', 'تحصیلات', 'مسلط_به_نرم_افزار_های', 'موبایل')
    list_filter = ('education', 'software_tools')


admin.site.register(Architect, ArchitectAdmin)




