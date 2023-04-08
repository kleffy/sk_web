# events/views.py
from django.views import generic
from .models import Event

class EventListView(generic.ListView):
    model = Event
    template_name = 'events/events_list.html'
    context_object_name = 'events'
    ordering = ['date']
