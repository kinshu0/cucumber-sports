from django.shortcuts import render, get_object_or_404, redirect

from .models import Event
from accounts.models import Registration, Profile

from django.contrib.auth.decorators import login_required

from .forms import EventCreation, TrackResult

result_forms = {
    'TrackResult': TrackResult,
}

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
        f = EventCreation(request.POST)
        if f.is_valid():
            f.save()
            return redirect('events')
    else:
        f = EventCreation()
    return render(request, 'events/create.html', {'form': f})

def add_result(request, event_id):
    if request.method == 'POST':
        pass
    else:
        event = get_object_or_404(Event, id=event_id)
        mode = event.sport_mode
        f = result_forms[mode.which_form]()
    return render(request, 'events/add-result.html', {'form': f})

# def event_result(request):
