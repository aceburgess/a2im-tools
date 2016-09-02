from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Company, Meeting, Event

# Create your views here.
def index(request):
	context = {
		'events': Event.objects.all()
	}
	return render(request, 'meetings/index.html', context)

def event(request, event_id):
	event_from_request = get_object_or_404(Event, id=event_id)
	meetings = Meeting.objects.filter(event=event_from_request)
	context = {
		'meetings': meetings,
		'event': event_from_request
	}
	return render(request, 'meetings/index.html', context)