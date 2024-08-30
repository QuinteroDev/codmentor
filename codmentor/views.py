# views.py
from django.shortcuts import render
from django.views.generic import TemplateView, RedirectView
from django.urls import reverse_lazy

class HomeView(TemplateView):
    template_name = 'home.html'

class RedirectExerciseView(RedirectView):
    url = reverse_lazy('generate_exercise') 