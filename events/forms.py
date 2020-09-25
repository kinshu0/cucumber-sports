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

        sport_mode = forms.ModelChoiceField(SportMode.objects, to_field_name='name')

        fields = [
            'name', 'event_picture', 'description_picture_1', 'description_picture_2', 'description_picture_3',
            'description', 'when', 'max_registrations', 'registration_fee', 'sport_mode', 'location_name', 'address_1',
            'address_2', 'city', 'state', 'zip_code'
        ]
        widgets = {
            'description': forms.Textarea(),
            'when': forms.DateTimeInput(attrs={
                'type': 'datetime-local',
                
            })
        }
        
    def clean_when(self):
        data = self.cleaned_data['when']
        if not data > now():
            raise ValidationError("The date or time entered is not valid")
        return data

