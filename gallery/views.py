# gallery/views.py
from django.views import generic
from .models import GalleryImage

class GalleryListView(generic.ListView):
    model = GalleryImage
    template_name = 'gallery/gallery_list.html'
    context_object_name = 'images'
