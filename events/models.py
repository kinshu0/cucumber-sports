from django.db import models

# from common_models import Location

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=100)
    when = models.DateTimeField()
    # location = models.ForeignKey(Location, on_delete=models.DO_NOTHING)
    # mode = models.ForeignKey(Mode, on_delete=models.DO_NOTHING)

    class Status(models.IntegerChoices):
        UPCOMING = 1
        IN_PROGRESS = 0
        ENDED = -1

        CANCELLED = -3
        POSTPONED = 2
        PREPONED = -2

    status = models.IntegerField(choices=Status.choices, default=Status.UPCOMING, blank=True)

# class SportMode(models.Model):

# class Mode(models.Model):
#     name = models.CharField()
#     # descriptor 
#     sport = models.ForeignKey(Sport, on_delete=models.CASCADE)

# class Sport(models.Model):
#     name = models.CharField()
#     description = models.CharField()