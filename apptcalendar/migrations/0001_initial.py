# Generated by Django 2.2.6 on 2019-12-15 09:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('appointments', '0010_auto_20191215_0100'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('Eventid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointments.Appointment')),
            ],
        ),
    ]