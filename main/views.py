from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home_page.html'

class ContactView(TemplateView):
    template_name = 'contact.html'
