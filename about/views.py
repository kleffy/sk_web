# about/views.py
from django.views import generic

class AboutPageView(generic.TemplateView):
    template_name = 'about/about.html'
