from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Event, Field

class HomePageView(TemplateView):

    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['events'] = Event.objects.all()[:5]
        context['fields'] = Field.objects.all()[:5]
        return context
