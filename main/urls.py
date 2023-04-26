from django.urls import path

from . import views

app_name = "main"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    #path("/produto/<int:pk>", views.DetailView.as_view(), name="detail"),
]