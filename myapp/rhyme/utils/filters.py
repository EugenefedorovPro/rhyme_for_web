import django_filters
from rhyme.models import Rhymes

class RhymesFilter(django_filters.FilterSet):
  rhyme = django_filters.CharFilter()
  # rhyme = m
  # score = m
  # assonance
  # pattern =
  class Meta:
    model = Rhymes
    fields = ['rhyme']