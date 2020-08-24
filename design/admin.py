from django.contrib import admin
from .models import Design


# Register your models here.


# class DesignAdmin(admin.ModelAdmin):

class DesignAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'designer', 'published', 'software_tool', 'design_upload_date')
    list_display_links = ('id', 'title')
    list_filter = ('designer', 'published', 'software_tool')
    search_fields = ('title', 'description', 'phone', 'software_tool', 'designer', 'عنوان', 'توضیحات', 'موبایل', 'نرم_افزارهای_مورد_استفاده', 'طراح')
    list_per_page = 25


admin.site.register(Design, DesignAdmin)

