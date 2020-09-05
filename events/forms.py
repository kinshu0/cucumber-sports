from django.forms import ModelForm, DateTimeInput
from . import models

from django.utils.timezone import now
from django.core.exceptions import ValidationError

from tempus_dominus.widgets import DateTimePicker

class EventCreation(ModelForm):
    class Meta:
        model = models.Event
        fields = ['name', 'when']
        widgets = {
            'when': DateTimePicker()
        }
        
    def clean_when(self):
        data = self.cleaned_data['when']
        if not data > now():
            raise ValidationError("The date or time entered is not valid")
        return data