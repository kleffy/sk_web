"""
URL configuration for sk_web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# project/urls.py
from django.contrib import admin
from django.urls import path, include
from home.views import HomePageView
from about.views import AboutPageView
from events.views import EventListView
from gallery.views import GalleryListView
from resources.views import ResourceListView
from contact.views import ContactView, ContactSuccessView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('news/', include('news.urls')),
    path('about/', AboutPageView.as_view(), name='about'),
    path('events/', EventListView.as_view(), name='events'),
    path('gallery/', GalleryListView.as_view(), name='gallery'),
    path('resources/', ResourceListView.as_view(), name='resources'),
    path('membership/', include('membership.urls')),
    path('contact/', ContactView.as_view(), name='contact'),
    path('contact/success/', ContactSuccessView.as_view(), name='contact_success'),
    path('accounts/', include('accounts.urls')),
    path('', HomePageView.as_view(), name='home'),
]
