# Generated by Django 3.0.6 on 2020-05-27 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('architect', '0004_auto_20200527_0842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='architect',
            name='name',
            field=models.CharField(default='Please Enter Your Name in Capitalize ', max_length=200),
        ),
    ]