from django.shortcuts import render
from django.http import HttpResponse
from core.models import Sermon, Event, Live


def index(request):
    sermons = Sermon.objects.all()[:4] 
    lives = Live.objects.all()[:1] 
    events = Event.objects.all()[:4]

    context ={
        'lives':lives,
        'sermons':sermons,
        'events':events,
    }

    return render(request, 'core/index.html', context)

def about(request):
    return render(request, 'core/about.html')

def sermon(request):
    sermons = Sermon.objects.all()

    context ={
        'sermons':sermons,
    }

    return render(request, 'core/sermons.html', context)

def event(request):
    events = Event.objects.all()

    context ={
        'events':events,
    }

    return render(request, 'core/events.html', context)

def contact(request):
    return render(request, 'core/contact.html')