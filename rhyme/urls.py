from django.urls import path, re_path
from .views import (
    views_results,
    views_rhyme,
    views_stress,
    views_title,
    views_transcribe,
)

urlpatterns = [
    path("", views_title.title, name="title"),
    path("rhyme/", views_rhyme.rhyme, name="rhyme"),
    re_path(
        r"^rhyme/stress/(?P<word_stressed_by_nn>.*)/(?P<unstressed_word>.*)/(?P<tuple_of_omographs>.*)/$",
        views_stress.stress,
        name="stress",
    ),
    path("transcribe", views_transcribe.transcribe, name="transcribe"),
    re_path(r"^rhyme/stress/.*/results", views_results.results, name="results"),
    path("rhyme/results", views_results.results, name="results"),
]
