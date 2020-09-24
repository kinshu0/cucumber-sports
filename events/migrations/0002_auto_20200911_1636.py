# Generated by Django 3.1 on 2020-09-11 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200911_1636'),
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='event_location',
        ),
        migrations.AddField(
            model_name='event',
            name='address_1',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='event',
            name='address_2',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='event',
            name='city',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='event',
            name='country',
            field=models.CharField(blank=True, max_length=90),
        ),
        migrations.AddField(
            model_name='event',
            name='location_name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='event',
            name='state',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='event',
            name='zip_code',
            field=models.CharField(blank=True, max_length=18),
        ),
        migrations.DeleteModel(
            name='Location',
        ),
    ]