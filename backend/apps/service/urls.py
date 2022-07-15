from django.urls import path
from backend.apps.service import views
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('url/delete/<int:pk>/', views.delete_url, name="delete"),
    path('url/update/<int:pk>/', views.update_url, name="update"),
    path('url/all/update/', views.update_all_user_url, name="all_update"),
]