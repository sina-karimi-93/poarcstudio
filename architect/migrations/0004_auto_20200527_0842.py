# Generated by Django 3.0.6 on 2020-05-27 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('architect', '0003_auto_20200527_0841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='architect',
            name='name',
            field=models.CharField(default='Please inter in Capitalize ', max_length=200),
        ),
    ]
