from django.http import HttpResponse
from django.shortcuts import render
def rhyme(request):
    return render(request, 'rhyme.html')