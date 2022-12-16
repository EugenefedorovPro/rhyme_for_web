from django.urls import path, re_path
from . import views

urlpatterns = [
    path("", views.title, name="title"),
    path("rhyme/", views.rhyme, name="rhyme"),
    re_path(
        r"^rhyme/stress/(?P<word_stressed_by_nn>.*)/(?P<unstressed_word>.*)/(?P<tuple_of_omographs>.*)/$",
        views.stress,
        name="stress",
    ),
    path("transcribe", views.transcribe, name="transcribe"),
    re_path(r"^rhyme/stress/.*/results", views.results, name="results"),
    path("rhyme/results", views.results, name="results"),
]
