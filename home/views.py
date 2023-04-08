# home/views.py
from django.views import generic

class HomePageView(generic.TemplateView):
    template_name = 'home/home.html'
