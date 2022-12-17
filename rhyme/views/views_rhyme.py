from django.shortcuts import render, redirect
from django.http import request, HttpResponse
from django.template import loader
from django.urls import reverse

from ..forms import (
    DepthTimeForm,
    InputWordWithoutStress,
)
from django.http import HttpResponseRedirect


def rhyme(request):
    if request.method == "POST":
        word_without_stress = InputWordWithoutStress(request.POST)
        depth_time = DepthTimeForm(request.POST)
        if word_without_stress.is_valid and depth_time.is_valid:
            return HttpResponseRedirect("rhyme/results/")
    else:
        depth_time = DepthTimeForm()
        input_word_without_stress = InputWordWithoutStress()
        return render(
            request,
            "rhyme.html",
            {
                "depth_time": depth_time,
                "input_word_without_stress": input_word_without_stress,
            },
        )
