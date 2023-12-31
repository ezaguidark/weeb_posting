from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, TemplateView
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

# Create your views here.

class SignUpView(CreateView):
    form_class = CustomUserCreationForm  # la form class que creamos en forms.py
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class ConfirmLogoutView(TemplateView):
    template_name = 'confirmlogout.html'
