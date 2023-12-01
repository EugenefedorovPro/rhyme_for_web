from django.shortcuts import render
<<<<<<< HEAD


def title(request):
    return render(request, 'title.html')
=======
from django.http import HttpResponse
from django.shortcuts import render, redirect

def title(request):
    return render(request, 'title.html')

# Create your views here.
>>>>>>> 3553f703e382e2fab61378fa69d1b3fcc4114bed
