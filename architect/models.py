from django.db import models
from datetime import datetime


# Create your models here.


class Architect(models.Model):
    choices = (
        ('Associate', 'Associate'),
        ('Undergraduate ', 'Undergraduate '),
        ('Master', 'Master'),
        ('Doctorate ', 'Doctorate ')
    )
    choices_persian = (
        ('فوق دیپلم', 'فوق دیپلم'),
        ('لیسانس ', 'لیسانس '),
        ('فوق لیسانس', 'فوق لیسانس'),
        ('دکترا ', 'دکترا ')
    )
    name = models.CharField(max_length=200, default='Please Enter Your Name in Capitalize ')
    اسم = models.CharField(max_length=200)
    education = models.CharField(max_length=20, choices=choices, default='Undergraduate')
    تحصیلات = models.CharField(max_length=20, choices=choices_persian, default='لیسانس')
    background = models.TextField()
    سابقه = models.TextField()
    software_tools = models.TextField(default='Revit / 3DsMax / Photoshop / Lumion / Autocad')
    مسلط_به_نرم_افزار_های = models.TextField(default='Revit / 3DsMax / Photoshop / Lumion / Autocad')
    phone = models.CharField(max_length=50)
    موبایل = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='photos/atchitects/%Y/%m/%d')
    hired_date = models.DateTimeField(default=datetime.now, blank=True)
    تاریخ_استخدام = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name
