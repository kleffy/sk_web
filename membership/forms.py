from django import forms
from .models import Membership

class MembershipForm(forms.Form):
    member_type = forms.ChoiceField(choices=Membership.MEMBER_TYPE_CHOICES)
    stripe_token = forms.CharField(widget=forms.HiddenInput())
