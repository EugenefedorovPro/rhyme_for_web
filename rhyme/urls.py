from django.urls import path
from . import views

urlpatterns = [
    path("", views.title, name="title"),
    path("results", views.results, name="results"),
]
