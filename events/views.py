from django.shortcuts import render

from .models import Event

# Create your views here.
def index_view(request):
    upcoming_events = Event.objects.filter(finished=False).order_by('when')

    return render(request, 'events/index.html', {
        'upcoming_events': upcoming_events,
    })