from django.urls import path
from .views import SignUpView
from .views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("edit/",edit_profile,name="edit_profile"),
]