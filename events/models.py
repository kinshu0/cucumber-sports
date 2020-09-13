from django.db import models
from django.core.serializers.json import DjangoJSONEncoder




class SportMode(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    
    # registration_schema = models.JSONField()
    # event_schema = models.JSONField()
    # result_schema = 
    which_form = models.CharField(max_length=100, null=False, blank=False, default='CustomResult')


class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    when = models.DateTimeField()
    sport_mode = models.ForeignKey(SportMode, on_delete=models.DO_NOTHING)

    class Status(models.IntegerChoices):
        UPCOMING = 1
        IN_PROGRESS = 0
        ENDED = -1

        CANCELLED = -3
        POSTPONED = 2
        PREPONED = -2

    
    location_name = models.CharField(max_length=255, blank=True)
    address_1 = models.CharField(max_length=255, blank=False)
    address_2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=False)
    state = models.CharField(max_length=255, blank=False)
    zip_code = models.CharField(max_length=18, blank=True)
    country = models.CharField(max_length=90, blank=True)

    status = models.IntegerField(choices=Status.choices, default=Status.UPCOMING, blank=True)

    result = models.JSONField(encoder=DjangoJSONEncoder, null=True)