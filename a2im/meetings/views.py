from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from .models import Company, Meeting, Event
from .forms import EventForm

# Create your views here.
def index(request):
	context = {
		'events': Event.objects.all()
	}
	return render(request, 'meetings/index.html', context)

def event_detail(request, pk):
	event_from_request = get_object_or_404(Event, id=pk)
	if request.method == "POST":
		if 'generate-meetings' in request.POST:
			event_from_request.generate_meetings()
			return redirect('event_detail', pk=event_from_request.pk)
		elif 'delete-meetings' in request.POST:
			event_from_request.delete_meetings()
			return redirect('event_detail', pk=event_from_request.pk)

	meetings = event_from_request.determine_meetings()

	context = {
		'meetings': meetings,
		'should_meet': meetings['should_meet'],
		'should_not_meet': meetings['should_not_meet'],
		'maybe_should_meet': meetings['undecided'],
		'event': event_from_request
	}

	return render(request, 'meetings/event_detail.html', context)

def event_new(request):
	if request.method == "POST":
		form = EventForm(request.POST)

		if form.is_valid():
			event = form.save(commit=False)
			event.save()
			return redirect('event_detail', pk=event.pk)
	else:
		form = EventForm()

	return render(request, 'meetings/event_edit.html', {'form': form})
		
	