import json
import pdb
from rhyme_rus.seeds.mysql_connect import my_sql
from put_stress_rus.put_stress import put_stress
from django.http import JsonResponse
from rhyme.views.allowed_characters import allowed_characters


def get_stressed_word(request):
    request_data = json.loads(request.body)
    unstressed_word = request_data.get("unstressed_word")

    # default message for invalid unstressed word
    message = "Напишите слово следуя правилам: запрещены большие буквы, среди небуквенных знаков разрешен только дефис /-/"
    stressed_word = "*****"
    data = {"stressed_word": stressed_word, "message": message}
    
    # check words validity
    if not unstressed_word:
        return JsonResponse(data)

    disallowed_characters = [_ for _ in unstressed_word if _ not in allowed_characters]
    if disallowed_characters:
        return JsonResponse(data)

    # get stressed word from db
    query = f"select accent from wiki_pickled where word = '{unstressed_word}'"
    stressed_word = my_sql.cur_execute(query)
    stressed_word = list(set(stressed_word))
    stressed_word= [word[0] for word in stressed_word]
    if stressed_word:
       # pdb.set_trace()
       stressed_word_str = ", ".join(stressed_word)
       word = "Слово" if len(stressed_word) == 1 else "Слова"
       taken = "взято" if len(stressed_word) == 1 else "взяты"
       message = f"{word} /{stressed_word_str}/ {taken} из en.wiktionary.org"

    # get stressed word from Neural Network
    if not stressed_word:
        stressed_word = put_stress(unstressed_word)
        message = f"Нейросеть поставила ударение в слове '{stressed_word}' с точностью 73%"

    # pdb.set_trace()
    data = {"stressed_word": stressed_word, "message": message}
    return JsonResponse(data)
