# Generated by Django 2.2.6 on 2019-11-10 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0003_auto_20191109_2141'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
    ]