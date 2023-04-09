from django.db import models
from django.contrib.auth.models import User

class Membership(models.Model):
    MEMBER_TYPE_CHOICES = (
        ('regular', 'Regular'),
        ('student', 'Student'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    member_type = models.CharField(max_length=10, choices=MEMBER_TYPE_CHOICES)
    membership_fee = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    monthly_deuce = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    def __str__(self):
        return self.user.username
