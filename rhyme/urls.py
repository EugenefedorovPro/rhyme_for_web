from django.urls import path
from .views import views_title, views_rhyme, views_rhyme_results

app_name = 'rhyme'

urlpatterns = [
    path('', views_title.title, name = 'title'),
    path('rhyme/', views_rhyme.rhyme, name = 'rhyme'),
    path('rhyme/rhyme_results/', views_rhyme_results.rhyme_results, name='rhyme_results')

    ]

