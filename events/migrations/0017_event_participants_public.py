# Generated by Django 3.1.1 on 2020-09-29 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0016_auto_20200928_1846'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='participants_public',
            field=models.BooleanField(default=True),
        ),
    ]