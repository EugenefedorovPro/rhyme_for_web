from django.shortcuts import render, redirect
from django.http import request, HttpResponse
from django.template import loader
from django.urls import reverse

from .models import Rhyme

from .forms import (
    InputWordToStressForm,
    StressVariantsForm,
    DepthTimeForm,
    InputWordWithoutStress,
)
from django.http import HttpResponseRedirect
from rhyme_rus.rhyme import rhyme_to_table, stress_word_by_wiki, stress_word_by_nn
from .utils import stressed_by_nn_variants
