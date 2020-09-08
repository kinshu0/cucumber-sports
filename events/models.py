from django.db import models
from django.core.serializers.json import DjangoJSONEncoder

# from common_models import Location
# Create your models here.


class SportMode(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    
    # registration_schema = models.JSONField()
    # event_schema = models.JSONField()
    # result_schema = 
    which_form = models.CharField(max_length=100, null=False, blank=False, default='CustomResult')


# class Mode(models.Model):
#     name = models.CharField()
#     # descriptor 
#     sport = models.ForeignKey(Sport, on_delete=models.CASCADE)

# class Sport(models.Model):
#     name = models.CharField()
#     description = models.CharField()

class Event(models.Model):
    name = models.CharField(max_length=100)
    when = models.DateTimeField()
    # location = models.ForeignKey(Location, on_delete=models.DO_NOTHING)
    sport_mode = models.ForeignKey(SportMode, on_delete=models.DO_NOTHING)

    class Status(models.IntegerChoices):
        UPCOMING = 1
        IN_PROGRESS = 0
        ENDED = -1

        CANCELLED = -3
        POSTPONED = 2
        PREPONED = -2

    status = models.IntegerField(choices=Status.choices, default=Status.UPCOMING, blank=True)

    result = models.JSONField(null=True)
    # result = models.JSONField(encoder=DjangoJSONEncoder, null=True)