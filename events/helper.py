from django.shortcuts import get_object_or_404
from accounts.models import Registration

from django.core.serializers.json import DjangoJSONEncoder
# from django.core.serializers import serialize

import json
from datetime import timedelta

from django.db.models.expressions import RawSQL

def timed_event(form_data, event, profile):
    try:
        converted_form_data = json.loads(form_data)
        # time_duration = timedelta(hours=converted_form_data['time']['hours'], minutes=converted_form_data['time']['minutes'], seconds=converted_form_data['time']['seconds'])
        if not converted_form_data['disqualified']:
            time_duration = f"{converted_form_data['time']['hours'] * 60 + converted_form_data['time']['minutes']}:{converted_form_data['time']['seconds']}"
        else:
            time_duration = f"DQ {converted_form_data['time']['hours'] * 60 + converted_form_data['time']['minutes']}:{converted_form_data['time']['seconds']}"
        converted_form_data['time'] = time_duration
        # final = json.dumps(converted_form_data, cls=DjangoJSONEncoder)
        # all_registrations = Registration.objects.filter(event=event).order_by(RawSQL("result->>%s", ("time",)))
        registration = get_object_or_404(Registration, event=event, profile=profile)
        # registration.result = final
        registration.result = converted_form_data
        registration.save()
        all_registrations = Registration.objects.filter(event=event).order_by(RawSQL("result->>%s", ("time",)))
        x = 1
        for i in all_registrations:
            i.result['#'] = x
            x += 1
            i.save()
    except:
        raise Exception("Error Saving or getting Registration object lol")

def points_event():
    pass

def unknown():
    pass


result_functions = {
    'T': timed_event,
    'P': points_event,
    '0': unknown
}