# from django.forms import ModelForm, DateTimeInput, Form
import django.forms as forms

import django.forms as forms

from . import models

from django.utils.timezone import now
from django.core.exceptions import ValidationError

from tempus_dominus.widgets import DateTimePicker

# from django_jsonforms.forms import JSONSchemaField

class EventCreation(forms.ModelForm):
    class Meta:
        model = models.Event
        fields = ['name', 'when', 'sport_mode']
        widgets = {
            'when': DateTimePicker()
        }
        
    def clean_when(self):
        data = self.cleaned_data['when']
        if not data > now():
            raise ValidationError("The date or time entered is not valid")
        return data

# class AddResult(forms.Form):

#     def __init__(self, data=None, files=None, auto_id='id_%s', prefix=None, initial=None, error_class=ErrorList, label_suffix=None, empty_permitted=False, field_order=None, use_required_attribute=None, renderer=None, result_schema=None):
#         super().__init__(data=data, files=files, auto_id=auto_id, prefix=prefix, initial=initial, error_class=error_class, label_suffix=label_suffix, empty_permitted=empty_permitted, field_order=field_order, use_required_attribute=use_required_attribute, renderer=renderer)
#         self.fields['result_form'] = JSONSchemaField(schema = result_schema, options = {'theme': 'bootstrap4'})

class TrackResult(forms.Form):
    
    time = forms.DurationField(required=False)
    participated = forms.BooleanField(required=True)

class TennisResult(forms.Form):
    pass

class CustomResult(forms.Form):
    pass