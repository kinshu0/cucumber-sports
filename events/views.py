from django.shortcuts import render, get_object_or_404

from .models import Event

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