from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404

from .models import Event
from accounts.models import Registration, Profile

from django.contrib.auth.decorators import login_required

from .forms import EventCreation
# from django.db.models.expressions import RawSQL

# from django.core.serializers import serialize
# from django.core.serializers.json import DjangoJSONEncoder

from django_jsonforms.forms import JSONSchemaForm
from .helper import result_functions, prize_display_functions, prize_calc_functions

# Create your views here.
def index_view(request):
    upcoming_events = Event.objects.order_by('when')

    return render(request, 'events/events.html', {
        'upcoming_events': upcoming_events,
    })

def specific_event(request, event_id):
    sp_event = get_object_or_404(Event, id=event_id)
    
    prize_handler_key = sp_event.sport_mode.result_handler
    prize_function = prize_display_functions[prize_handler_key]

    prize_section, prize_section_context = prize_function(sp_event)
    
    return render(request, 'events/specific.html', {
        'event': sp_event,
        'prize_section_template': prize_section,
    })

@login_required
def event_register(request, event_id):
    event = Event.objects.get(id=event_id)
    profile = Profile.objects.get(user=request.user)

    if event.status == 10:
        return render(request, 'events/specific.html', {'event_errors': ['Sorry, event registration is full.'], 'anchor': 'register'})
            
    if Registration.objects.filter(profile=profile, event=event).exists():
        return render(request, 'events/specific.html', {'event': event, 'event_errors': ['You are already registered for this event!'], 'anchor': 'register'})

    registration = Registration(
        profile = profile,
        event = event
    )
    registration.save()

    if event.max_registrations:
        if event.max_registrations == Registration.objects.filter(event=event, profile=profile).count():
            event.status = 10

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


@login_required
def add_result(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    mode = event.sport_mode

    if request.method == 'POST':
        profile = get_object_or_404(Profile, user=request.user)
        form_data = request.POST['json']
        
        registration_result = result_functions[mode.result_handler](form_data, event, profile)
        
        return redirect('events')
        
    result_schema = mode.result_schema
    ResultForm = JSONSchemaForm(schema=result_schema, options={
        "iconlib": "fontawesome5",
        "no_additional_properties ": True,
        "disable_collapse": True,
        "disable_edit_json": True,
        "disable_properties": True,
        "theme": "bootstrap4",
    }, ajax=False)
    
    # else:
    #     f = r()
    # return render(request, 'events/add_result.html', {'result_schema': result_schema})
    f = ResultForm
    return render(request, 'events/add_result.html', {'form': f})

def organizer_add_result(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    mode = event.sport_mode

    if request.method == 'POST':
        lolol = request.POST.keys()

        for x in Registration.objects.filter(event=event):
            helper_arguments = request.POST[f'{x.id}-json'], event, x.profile
            save_result = result_functions[mode.result_handler](*helper_arguments)
        
        return redirect('events')
        
    result_schema = mode.result_schema
    
    corresponding_forms = {f'{x.profile.first_name} {x.profile.last_name}': JSONSchemaForm(prefix=x.id, schema=result_schema, options={
        "iconlib": "fontawesome5",
        "no_additional_properties ": True,
        "disable_collapse": True,
        "disable_edit_json": True,
        "disable_properties": True,
        "theme": "bootstrap4",
    }, ajax=False) for x in Registration.objects.filter(event=event)}

    ResultForm = JSONSchemaForm(schema=result_schema, options={
        "iconlib": "fontawesome5",
        "no_additional_properties ": True,
        "disable_collapse": True,
        "disable_edit_json": True,
        "disable_properties": True,
        "theme": "bootstrap4",
    }, ajax=False)

    return render(request, 'events/organizer_add_result.html', {'formScripts': ResultForm.media, 'stuff': corresponding_forms})

def event_result(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    registrations = get_list_or_404(Registration, event=event)

    final = []
    for i in registrations:
        i.result['name'] = f'{i.profile.first_name} {i.profile.last_name}'
        final.append(i.result)

    display_schema = event.sport_mode.display_schema

    return render(request, 'events/results.html', {'event_name': event.name,'results': final, 'display_schema': display_schema})

def release_payment(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    mode = event.sport_mode

    calculate_function = prize_calc_functions[mode.result_handler]

    payment = calculate_function(event, commit=False)

    if request.method == 'POST':
        calculate_function(event, commit=True)
        return redirect('events')

    return render(request, 'events/confirm_release_pay.html', {'payment': payment})