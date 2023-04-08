# contact/views.py
from django.views import generic
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

class ContactView(generic.FormView):
    form_class = ContactForm
    template_name = 'contact/contact.html'
    success_url = reverse_lazy('contact_success')

    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']

        message = f"Message from {name} ({email})\n\n{message}"
        send_mail(subject, message, email, [settings.EMAIL_HOST_USER])
        return super().form_valid(form)

class ContactSuccessView(generic.TemplateView):
    template_name = 'contact/contact_success.html'
