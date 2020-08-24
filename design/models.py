from django.db import models
from datetime import datetime
from architect.models import Architect


# Create your models here.

class Design(models.Model):
    designer = models.ForeignKey(Architect, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    عنوان = models.CharField(max_length=200)
    design_upload_date = models.DateTimeField()
    تاریخ_آپلود_طرح = models.DateTimeField()
    design_date = models.DateTimeField(default=datetime.now)
    تاریخ_طراحی = models.DateTimeField(default=datetime.now)
    software_tool = models.CharField(
        max_length=200,
        default='Revit / 3DsMax / Lumion / Photoshop / Autocad'
    )
    نرم_افزارهای_مورد_استفاده = models.CharField(
        max_length=200,
        default='Revit / 3DsMax / Lumion / Photoshop / Autocad'
    )
    description = models.TextField(default='please add at least 10 words')
    توضیحات = models.TextField(default='لطفا حداقل ده کلمه وارد کنید')
    photo_main = models.ImageField(upload_to='photos/designes/%Y/%m/%d')
    photo_1 = models.ImageField(upload_to='photos/designes/%Y/%m/%d', blank=True)
    photo_2 = models.ImageField(upload_to='photos/designes/%Y/%m/%d', blank=True)
    photo_3 = models.ImageField(upload_to='photos/designes/%Y/%m/%d', blank=True)
    photo_4 = models.ImageField(upload_to='photos/designes/%Y/%m/%d', blank=True)
    photo_5 = models.ImageField(upload_to='photos/designes/%Y/%m/%d', blank=True)
    photo_6 = models.ImageField(upload_to='photos/designes/%Y/%m/%d', blank=True)
    photo_7 = models.ImageField(upload_to='photos/designes/%Y/%m/%d', blank=True)
    photo_8 = models.ImageField(upload_to='photos/designes/%Y/%m/%d', blank=True)
    photo_9 = models.ImageField(upload_to='photos/designes/%Y/%m/%d', blank=True)
    photo_10 = models.ImageField(upload_to='photos/designes/%Y/%m/%d', blank=True)
    photo_11 = models.ImageField(upload_to='photos/designes/%Y/%m/%d', blank=True)
    photo_12 = models.ImageField(upload_to='photos/designes/%Y/%m/%d', blank=True)
    published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

