# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.views.generic import ListView

from .models import Event, Guide
from .views import HomePageView

urlpatterns = [
    url(r'^$', HomePageView.as_view(template_name='pages/home.html'), name='home'),
    url(r'^about/$', TemplateView.as_view(template_name='pages/about.html'), name='about'),
    url(r'^eventos/$', ListView.as_view(model=Event), name='events'),
    url(r'^guias/$', ListView.as_view(model=Guide), name='guides'),
]
