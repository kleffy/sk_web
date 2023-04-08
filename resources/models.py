# resources/models.py
from django.db import models

class Resource(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    file = models.FileField(upload_to='resources/')
    upload_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
