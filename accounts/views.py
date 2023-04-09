# from django.shortcuts import render, redirect
# from django.contrib.auth import login, authenticate
# from django.contrib.auth.views import LoginView
# from django.views import View
# from .forms import SignUpForm, LoginForm

# class SignUpView(View):
#     def get(self, request):
#         form = SignUpForm()
#         return render(request, 'accounts/signup.html', {'form': form})

#     def post(self, request):
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('home')
#         return render(request, 'accounts/signup.html', {'form': form})

# class LoginView(LoginView):
#     form_class = LoginForm
#     template_name = 'accounts/login.html'

#     def form_valid(self, form):
#         login(self.request, form.get_user())
#         return redirect('home')
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'
