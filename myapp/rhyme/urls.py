from django.urls import path
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
from .views import (
    views_title,
    views_rhyme,
    views_rhyme_results,
    views_stress,
    views_transcribe,
)
from django.views.generic import RedirectView

app_name = "rhyme"

urlpatterns = [
    path("", views_title.title, name="title"),
    path("rhyme", views_rhyme.rhyme, name="rhyme"),
    path("stress", views_stress.stress, name="stress"),
    path("transcribe", views_transcribe.transcribe, name="transcribe"),
    # path('rhyme/', views_rhyme.rhyme, name = 'rhyme'),
    path(
        "rhyme/rhyme_results/", views_rhyme_results.rhyme_results, name="rhyme_results"
    ),
    path("favicon.ico", RedirectView.as_view(url="/static/favicon.ico")),
]
=======
=======
>>>>>>> 3553f703e382e2fab61378fa69d1b3fcc4114bed
=======
>>>>>>> 3553f703e382e2fab61378fa69d1b3fcc4114bed
from .views import views_title, views_rhyme, views_rhyme_results, views_stress, views_transcribe

app_name = 'rhyme'

urlpatterns = [
    path('', views_title.title, name = 'title'),
    path('rhyme', views_rhyme.rhyme, name = 'rhyme'),
    path('stress', views_stress.stress, name = 'stress'),
    path('transcribe', views_transcribe.transcribe, name = 'transcribe'),
    # path('rhyme/', views_rhyme.rhyme, name = 'rhyme'),
    path('rhyme/rhyme_results/', views_rhyme_results.rhyme_results, name='rhyme_results')
    ]

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 3553f703e382e2fab61378fa69d1b3fcc4114bed
=======
>>>>>>> 3553f703e382e2fab61378fa69d1b3fcc4114bed
=======
>>>>>>> 3553f703e382e2fab61378fa69d1b3fcc4114bed
