import pdb
# from put_stress_rus.put_stress import put_stress
from django.shortcuts import render

def stress(request):
    # word_unstressed = request.GET.get('word_unstressed')
    # word_stressed = put_stress(word_unstressed)
    # pdb.set_trace()
    # context = {
    #         'word_stressed': word_stressed,
    #         }
    return render(request, 'stress.html')

