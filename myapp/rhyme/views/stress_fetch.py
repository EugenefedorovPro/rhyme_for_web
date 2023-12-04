
import pdb
# from put_stress_rus.put_stress import put_stress
from django.http import JsonResponse

def stress(request):
    word_unstressed = request.POST.get('word_unstressed')
    # word_stressed = put_stress(word_unstressed)
    # pdb.set_trace()
    # context = {
    #         'word_stressed': word_stressed,
    #         }
    word_stressed = "stresses word in fetch"
    data = {"word_stressed": word_stressed}
    return JsonResponse(data)
