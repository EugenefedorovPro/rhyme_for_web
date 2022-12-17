from django.shortcuts import render, redirect
from django.http import request, HttpResponse
from django.template import loader
from django.urls import reverse


def transcribe(request):
    word_as_ipa = "Here goes word in IPA notation"
    return render(request, "transcribe.html", {"word_as_ipa": word_as_ipa})
