from django.shortcuts import render

def transcribe(request):
    return render(request, 'transcribe.html')
