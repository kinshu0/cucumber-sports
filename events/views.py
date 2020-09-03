from django.shortcuts import render, get_object_or_404

from .models import Event
from accounts.models import Registration, Profile

from django.contrib.auth.decorators import login_required

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