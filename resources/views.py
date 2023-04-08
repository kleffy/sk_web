# resources/views.py
from django.views import generic
from .models import Resource

class ResourceListView(generic.ListView):
    model = Resource
    template_name = 'resources/resource_list.html'
    context_object_name = 'resources'
    ordering = ['-upload_date']
