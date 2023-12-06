from django.urls import path
from .views import (
    views_title,
    views_rhyme,
    views_rhyme_results,
    views_stress,
    views_transcribe,
    views_stress_fetch,
    views_transcription_fetch,
    views_about,
)
from django.views.generic import RedirectView

app_name = "rhyme"

urlpatterns = [
    path("", views_title.title, name="title"),
    path("rhyme", views_rhyme.rhyme, name="rhyme"),
    path("stress", views_stress.stress, name="stress"),
    path("transcribe", views_transcribe.transcribe, name="transcribe"),
    path(
        "rhyme/rhyme_results/", views_rhyme_results.rhyme_results, name="rhyme_results"
    ),
    path("favicon.ico", RedirectView.as_view(url="/static/favicon.ico")),
    path("stress/results/", views_stress_fetch.get_stressed_word, name="get_stressed_word"),
    path(
        "transcribe/results/", views_transcription_fetch.get_transcription, name="get_transcription"
        ),
    path("about", views_about.get_about, name="about"),

]
