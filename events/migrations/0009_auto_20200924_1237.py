# Generated by Django 3.1.1 on 2020-09-24 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_event_event_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='description_picture_1',
            field=models.ImageField(blank=True, null=True, upload_to='images/event_pictures'),
        ),
        migrations.AddField(
            model_name='event',
            name='description_picture_2',
            field=models.ImageField(blank=True, null=True, upload_to='images/event_pictures'),
        ),
        migrations.AddField(
            model_name='event',
            name='description_picture_3',
            field=models.ImageField(blank=True, null=True, upload_to='images/event_pictures'),
        ),
    ]
