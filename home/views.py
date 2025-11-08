from django.shortcuts import render, redirect

# My imports
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import logout
from django.http import HttpResponseRedirect

# Create your views here.

class LoginPageView(LoginView):
    template_name = "userpage/login.html"

def logoutView(request):
    if request.method == 'POST':
        HttpResponse(request, "Awesome! You have been logged out successfully!")
        return LogoutView.as_view(next_page='/login/')(request)
    else:
        return render(request, '/login/')

class LogoutPageView(LogoutView):    
    template_name = "userpage/logout.html"
    #next_page = "/login/"
    #success_url = "/login/"

"""    def get(self, request):
        logout(request)
        return (render(request, "home/templates/userpage/logout.html", {}))
"""    """ 
    /workspaces/django-esst-2894047-copy/home/templates/userpage/logout.html
    home/templates/userpage/logout.html

    def get(self, request):
        logout(request)
        return (render(request, "login/", {})) #HttpResponseRedirect(redirect_to="userpage/login.html")
    """    
    #template_name = "userpage/logout.html"
    #success_url = "userpage/login.html"

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
    login_url = "/login/"

class Advantages(LoginRequiredMixin,TemplateView):
    template_name = "homepage/advantages.html"
    login_url = "/login/"

"""
@login_required(login_url="admin/")
def home_page_authorized(request):
    return (render(request, "homepage/authorized.html", {}))
"""