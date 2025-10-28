from django.shortcuts import render

# My imports
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

# The home for HttpResponse verification
def home_page(request):
    return (HttpResponse("Hello, Blessed World!"))

class homePageWelcomeView(TemplateView):
    template_name = "homepage/welcome.html"
    extra_context = {"today":datetime.today()}

"""
def home_page_welcome(request):
    return (render(request, "homepage/welcome.html", {"today":datetime.today()}))
"""

class Authorized(LoginRequiredMixin,TemplateView):
    template_name = "homepage/authorized.html"
    login_url = "../admin/"

class Advantages(LoginRequiredMixin,TemplateView):
    template_name = "homepage/advantages.html"
    login_url = "../admin/"

"""
@login_required(login_url="admin/")
def home_page_authorized(request):
    return (render(request, "homepage/authorized.html", {}))
"""