# from django.forms import ModelForm, DateTimeInput, Form
import django.forms as forms

import django.forms as forms

from . import models

from django.utils.timezone import now
from django.core.exceptions import ValidationError
from .models import SportMode

# from django_jsonforms.forms import JSONSchemaField

class EventCreation(forms.ModelForm):

    class Meta:
        model = models.Event

        sport_mode = forms.ModelChoiceField(SportMode.objects)
        # sponsored_prize = forms.DecimalField(help_text='Enter value here if outside source is providing portion of prize money')

        fields = [
            'name', 'event_picture', 'description_picture_1', 'description_picture_2', 'description_picture_3',
            'description', 'when', 'max_registrations', 'registration_fee', 'sponsored_prize', 'sport_mode', 'location_name', 'address_1',
            'address_2', 'city', 'state', 'zip_code'
        ]
        widgets = {
            'description': forms.Textarea(),
            'when': forms.DateTimeInput(attrs={
                'type': 'datetime-local',
                
            })
        }
        help_texts = {
            'sponsored_prize': 'Enter value here if outside source is providing portion of prize money'
        }
        
    def clean_when(self):
        data = self.cleaned_data['when']
        if not data > now():
            raise ValidationError("The date or time entered is not valid")
        return data

'''
Event Completion Form -> Trigger Payment
'''
class Event_Completion(forms.ModelForm):

    class Meta:
        model = models.Event
        
        fields = [
            'status'
        ]
        widgets = {
        }