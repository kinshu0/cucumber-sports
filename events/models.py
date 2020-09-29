from django.db import models
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.auth.models import User

result_choices = [
    ('T', 'Timed'),
    ('P', 'Points'),
    ('0', 'Unhandled')
]

class SportMode(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    
    result_handler = models.CharField(choices=result_choices, default='0', max_length=2)

    result_schema = models.JSONField()
    display_schema = models.JSONField()
    # registration_schema = models.JSONField()
    # event_schema = models.JSONField()
    # result_schema = 
    # which_form = models.CharField(max_length=100, null=False, blank=False, default='CustomResult')
    def __str__(self):
        return self.name

class Event(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    participants_public = models.BooleanField(default=True)

    name = models.CharField(max_length=100)
    event_picture = models.ImageField(upload_to='images/event_pictures', null=True, blank=True)

    description_picture_1 = models.ImageField(upload_to='images/event_pictures', null=True, blank=True)
    description_picture_2 = models.ImageField(upload_to='images/event_pictures', null=True, blank=True)
    description_picture_3 = models.ImageField(upload_to='images/event_pictures', null=True, blank=True)

    description = models.CharField(max_length=1000)
    when = models.DateTimeField()
    sport_mode = models.ForeignKey(SportMode, on_delete=models.DO_NOTHING)
    registration_fee = models.DecimalField(decimal_places=2, max_digits=6, default=0)

    class Status(models.IntegerChoices):
        OPEN = 1
        IN_PROGRESS = 0
        ENDED = -1

        CANCELLED = -3
        POSTPONED = 2
        PREPONED = -2

        CLOSED = 10

    
    location_name = models.CharField(max_length=255, blank=True)
    address_1 = models.CharField(max_length=255, blank=False)
    address_2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=False)
    state = models.CharField(max_length=255, blank=False)
    zip_code = models.CharField(max_length=18, blank=True)
    country = models.CharField(max_length=90, blank=True)

    status = models.IntegerField(choices=Status.choices, default=Status.OPEN, blank=True)

    result = models.JSONField(null=True)

    max_registrations = models.IntegerField(null=True)
    def __str__(self):
        return self.name