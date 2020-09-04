from django.db import models

# from common_models import Location

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=100)
    when = models.DateTimeField()
    # location = models.ForeignKey(Location, on_delete=models.DO_NOTHING)
    # mode = models.ForeignKey(Mode, on_delete=models.DO_NOTHING)
    status = [
        ('U', 'Upcoming'),
        ('P', 'In Progress'),
        ('F', 'Finished'),

        ('C', 'Cancelled'),
        ('L', 'Postponed'),
        ('E', 'Preponed'),
    ]

# class SportMode(models.Model):

# class Mode(models.Model):
#     name = models.CharField()
#     # descriptor 
#     sport = models.ForeignKey(Sport, on_delete=models.CASCADE)

# class Sport(models.Model):
#     name = models.CharField()
#     description = models.CharField()