from django.urls import path
from .views import views_title, views_rhyme


urlpatterns = [
    path('', views_title.title, name = 'title'),
    path('rhyme/', views_rhyme.rhyme, name = 'rhyme')
    ]

