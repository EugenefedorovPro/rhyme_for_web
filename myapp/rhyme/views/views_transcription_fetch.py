import json
import pdb
from word2ipa_rus.word2ipa import word2ipa
from django.http import JsonResponse
from rhyme.views.allowed_characters import allowed_characters


def get_transcription(request):
    # pdb.set_trace()
    request_data = json.loads(request.body)
    word_with_accent = request_data.get("input_word")

    # default message for invalid word
    message = "Напишите слово следуя правилам: запрещены большие буквы, среди небуквенных знаков разрешены дефис /-/ и ударение /'/"
    transcription = "*****"
    data = {"transcription": transcription, "message": message}
    
    # check words validity
    if not word_with_accent:
        return JsonResponse(data)

    if "'" not in  word_with_accent:
        message = "В слове обязательно должен стоять знак ударения /'/"
        transcription = "*****"
        data = {"transcription": transcription, "message": message}
        return JsonResponse(data)

    # remove initial and final blank spaces
    word_with_accent = word_with_accent.strip()

    allowed_characters.append("'")
    disallowed_characters = [_ for _ in word_with_accent if _ not in allowed_characters]
    if disallowed_characters:
        return JsonResponse(data)

    # get transcription from NN
    transcription = word2ipa(word_with_accent)
    message = f"Нейросеть поставила ударение в слове /{transcription}/ с точностью 99,96%"

    data = {"transcription": transcription, "message": message}
    # pdb.set_trace()

    return JsonResponse(data)
