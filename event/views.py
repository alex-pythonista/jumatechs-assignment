from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from .models import Event

def home(request):
    context = {}
    current_datetime = timezone.now()
    events = Event.objects.filter(datetime__gte=current_datetime)
    query = request.GET.get('q')
    if query:
        events = events.filter(title__icontains=query)
        context['q'] = True
    context['events'] = events
    return render(request, 'event/home.html', context)

def event_details(request, id):
    context = {}
    event = Event.objects.get(id=id)
    if request.user.is_authenticated:
        user = request.user
        is_registered = event.attendees.filter(user=user).exists()
        if is_registered:
            context['is_registered'] = True
    context['event'] = event
    return render(request, 'event/details.html', context)

@login_required
def my_event(request):
    context = {}
    user = request.user
    events = Event.objects.filter(attendees__user=user)
    print(events)
    context['events'] = events
    return render(request, 'event/events.html', context)

@login_required
def register(request, id):
    event = Event.objects.get(id=id)
    user = request.user
    event.attendees.create(user=user)
    return redirect('my-events')

@login_required
def unregister(request, id):
    event = Event.objects.get(id=id)
    user = request.user
    event.attendees.filter(user=user).delete()
    return redirect('my-events')