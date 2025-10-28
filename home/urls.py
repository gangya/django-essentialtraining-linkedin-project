from django.urls import path
from . import views

urlpatterns = [
    path("homepage/", views.home_page),
    path("homepagewelcome/", views.homePageWelcomeView.as_view(), name="homepagewelcomeView"),
    path("authorized/", views.Authorized.as_view(), name="authorizedView"),
    path("advantages/", views.Advantages.as_view(), name="advantageView")
]