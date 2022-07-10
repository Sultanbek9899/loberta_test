from django.urls import path
from backend.apps.service import views
urlpatterns = [
    path('', views.IndexView.as_view(), name="index")
]