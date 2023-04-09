import stripe
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import MembershipForm
from .models import Membership

stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required
def membership_payment(request):
    if request.method == 'POST':
        form = MembershipForm(request.POST)
        if form.is_valid():
            member_type = form.cleaned_data['member_type']
            token = form.cleaned_data['stripe_token']

            if member_type == 'regular':
                membership_fee = 2000
                monthly_deuce = 1000
            else: # student
                membership_fee = 1000
                monthly_deuce = 500

            try:
                charge = stripe.Charge.create(
                    amount=membership_fee,
                    currency='gbp',
                    description='Membership Fee',
                    source=token,
                )

                membership = Membership(
                    user=request.user,
                    member_type=member_type,
                    membership_fee=membership_fee / 100,
                    monthly_deuce=monthly_deuce / 100,
                )
                membership.save()

                return redirect('membership_success')

            except stripe.error.CardError as e:
                error = "Your card was declined."

    else:
        form = MembershipForm()

    return render(request, 'membership/membership_payment.html', {'form': form})

def membership_success(request):
    return render(request, 'membership/membership_success.html')
