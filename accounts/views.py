from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from .models import CustomUser

class SignUpView(generic.CreateView):
    model = CustomUser
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('home')