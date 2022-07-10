
from django.urls import path

from .views import LoginView, user_logout
urlpatterns = [
    path("login/", LoginView.as_view(), name="sign_in"),
    path("logout/", user_logout, name="logout")
]