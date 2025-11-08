from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.LoginPageView.as_view(), name="loginpageView"),
    #path("logout/", views.LogoutView.as_view(), name="logoutpageView"),
    path("logout/", views.logoutView, name="logoutpageView"),
    #path('logout/', views.LogoutView.as_view(http_method_names = ['get', 'post', 'options']), name='logoutpageView'),
    path("logout2/", views.LogoutPageView.as_view(), name="logoutpageView2"),
    path("homepage/", views.home_page),
    path("", views.homePageWelcomeView.as_view(), name="homepagewelcomeView"),
    #path("homepagewelcome/", views.homePageWelcomeView.as_view(), name="homepagewelcomeView"),
    path("authorized/", views.Authorized.as_view(), name="authorizedView"),
    path("advantages/", views.Advantages.as_view(), name="advantageView"),
    #path("advantages/", views.Advantages.as_view(), name="advantageView"),
    #path("advantages/", views.Advantages.as_view(), name="advantageView"),
]