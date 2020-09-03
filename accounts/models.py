from django.db import models

# Create your models here.
from django.contrib.auth.models import User

from events.models import Event

class Profile(models.Model):        
    # required to associate Author model with User model (Important)
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)

    # additional fields
    activation_key = models.CharField(max_length=255, default=1)
    email_validated = models.BooleanField(default=False)

    first_name = models.CharField(max_length=50, default='')
    last_name = models.CharField(max_length=50, default='')
    # first_name = models.CharField(max_length=50)
    # last_name = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username

class Registration(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)
    event = models.ForeignKey(Event, on_delete=models.DO_NOTHING)

    created_when = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)