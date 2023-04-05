from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect

def title(request):
    return render(request, 'title.html')

# Create your views here.
