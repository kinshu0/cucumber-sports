from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404

from .models import Event
from accounts.models import Registration, Profile

from django.contrib.auth.decorators import login_required

from .forms import EventCreation
# from django.db.models.expressions import RawSQL

# from django.core.serializers import serialize
# from django.core.serializers.json import DjangoJSONEncoder

from django_jsonforms.forms import JSONSchemaForm
from .helper import result_functions

# Create your views here.
def index_view(request):
    upcoming_events = Event.objects.order_by('when')

    return render(request, 'events/events.html', {
        'upcoming_events': upcoming_events,
    })

def specific_event(request, event_id):
    sp_event = get_object_or_404(Event, id=event_id)
    
    return render(request, 'events/specific.html', {
        'event': sp_event,
    })

@login_required
def event_register(request, event_id):
    registration = Registration(
        profile = Profile.objects.get(user=request.user),
        event = Event.objects.get(id=event_id)
    )
    registration.save()
    return render(request, 'events/successful.html')

def create_event(request):
    if request.method == 'POST':
        f = EventCreation(request.POST, request.FILES)
        if f.is_valid():
            f.save()
            return redirect('events')
    else:
        f = EventCreation()
    return render(request, 'events/create.html', {'form': f})

def edit_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    if request.method == 'POST':
        f = EventCreation(request.POST, request.FILES, instance=event)
        if f.is_valid():
            f.save()
            return redirect('events')
    else:
        f = EventCreation(initial=vars(event))

    return render(request, 'events/edit_event.html', {'form': f, 'event': event})


# def TrackResultEval(f, request, event):
#     profile = get_object_or_404(Profile, user=request.user)
#     all_registrations = Registration.objects.filter(event=event)
#     registration = all_registrations.get(profile=profile)

#     b = f.cleaned_data.items()

#     registration.result = {
#         k: serialize('json', v, cls=DjangoJSONEncoder) for (k, v) in f.cleaned_data.items()
#     }

#     # registration.result = {
#     #         'Time': f.cleaned_data['result_time'],
#     # }

#     registration.save()
#     z = 1

#     for x in all_registrations.order_by(RawSQL("result->>%s", ("Time",))):
#         x.result['Position'] = z
#         x.save()
#         z += 1



# result_forms = {
#     'TrackResult': (TrackResult, TrackResultEval),
# }

@login_required
def add_result(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    mode = event.sport_mode

    result_schema = mode.result_schema
    ResultForm = JSONSchemaForm(schema=result_schema, options={
        "iconlib": "fontawesome5",
        "no_additional_properties ": True,
        "disable_collapse": True,
        "disable_edit_json": True,
        "disable_properties": True,
        "theme": "bootstrap4",
    }, ajax=False)

    if request.method == 'POST':
        profile = get_object_or_404(Profile, user=request.user)
        form_data = request.POST['json']
        
        registration_result = result_functions[mode.result_handler](form_data, event, profile)
        
        return redirect('events')
    pass

    # else:
    #     f = r()
    # return render(request, 'events/add_result.html', {'result_schema': result_schema})
    f = ResultForm
    return render(request, 'events/add_result.html', {'form': f})

def event_result(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    registrations = get_list_or_404(Registration, event=event)

    final = []
    for i in registrations:
        i.result['name'] = f'{i.profile.first_name} {i.profile.last_name}'
        final.append(i.result)

    display_schema = event.sport_mode.display_schema

    return render(request, 'events/results.html', {'event_name': event.name,'results': final, 'display_schema': display_schema})