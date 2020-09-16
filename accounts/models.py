from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.core.serializers.json import DjangoJSONEncoder

from events.models import Event

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.DO_NOTHING)

    activation_key = models.CharField(max_length=255, default=1)
    email_validated = models.BooleanField(default=False)

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    bio = models.CharField(max_length=150, blank=True)

    '''
    User Location Data, only gonna ask user to feed city and state
    '''
    location_name = models.CharField(max_length=255, blank=True)
    address_1 = models.CharField(max_length=255, blank=True)
    address_2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    state = models.CharField(max_length=255, blank=True)
    zip_code = models.CharField(max_length=18, blank=True)
    country = models.CharField(max_length=90, blank=True)

    def __str__(self):
        return self.user.username

class Registration(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)
    event = models.ForeignKey(Event, on_delete=models.DO_NOTHING)

    created_when = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    '''
    Result could be time or any number through which to order results,
    For instance: 1, 2, 3 for place which would be ascending
    or time: 4:23, 4:30, 4:33 where the ascending order would still create the same position
    '''

    '''
    Schema of this field depends on schema defined in the row pointed by the foreign key stored in the Event's
    sport_mode field
    '''
    result = models.JSONField(null=True)
    # result = models.JSONField(encoder=DjangoJSONEncoder, null=True)
