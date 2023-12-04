import pdb
from django.shortcuts import render

def stress(request):
    return render(request, 'stress.html')

