# Generated by Django 3.1.1 on 2020-09-26 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_profile_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='result_place',
            field=models.IntegerField(null=True),
        ),
    ]
