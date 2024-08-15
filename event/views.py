from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from .models import Event

def home(request):
    context = {}
    current_datetime = timezone.now()
    events = Event.objects.filter(datetime__gte=current_datetime)
    context['events'] = events
    return render(request, 'event/home.html', context)

def event_details(request, id):
    context = {}
    event = Event.objects.get(id=id)
    context['event'] = event
    return render(request, 'event/details.html', context)