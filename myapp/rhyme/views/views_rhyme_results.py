import json
import pdb
import pandas as pd
from rhyme_rus.rhyme import rhyme_with_stresses
from django.shortcuts import render
from rhyme.utils.rhyme_results.data_score_assonance import DataScoreAssonance
from rhyme.views.allowed_characters import allowed_characters

def rhyme_results(request):
    unstressed_word = request.POST["target_word"]
    # pdb.set_trace()

    # check words validity
    unstressed_word = unstressed_word.strip()
    allowed_characters.append("'")
    disallowed_characters = [_ for _ in unstressed_word if _ not in allowed_characters]
    if not unstressed_word or disallowed_characters:
        message = '''Напишите слово следуя правилам: запрещены большие буквы, 
                     среди небуквенных знаков разрешены дефис /-/ и знак ударения /'/'''
        context = {"message": message}
        return render(request, "rhyme.html", context)

    try:
        table_of_rhymes, all_stresses, stressed_word = rhyme_with_stresses(
            unstressed_word
        )
        rhymes = tuple(table_of_rhymes["rhyme"])
        scores = tuple(table_of_rhymes["score"])
        unique_scores = tuple(set(scores))
        assonances = tuple(table_of_rhymes["assonance"])
        unique_assonances = tuple(set(assonances))
        patterns = tuple(table_of_rhymes["pattern"])
        number_rhymes = len(table_of_rhymes)

        Data = DataScoreAssonance(table_of_rhymes, scores, assonances)
        data_scores_by_assonance = Data.data_scores_by_assonance
        data_assonances_by_score = Data.data_assonances_by_score
        all_score_values = Data.all_score_values
        all_assonance_values = Data.all_assonance_values

        cards = []
        for rhyme, score, assonance, pattern in zip(
            rhymes, scores, assonances, patterns
        ):
            cards.append(tuple((rhyme, score, assonance, pattern)))

        context = {
            "number_rhymes": number_rhymes,
            "stressed_word": stressed_word,
            "cards": cards,
            "unique_scores": unique_scores,
            "unique_assonances": unique_assonances,
            "data_assonances_by_score": data_assonances_by_score,
            "data_scores_by_assonance": data_scores_by_assonance,
            "all_score_values": all_score_values,
            "all_assonance_values": all_assonance_values,
        }
        return render(request, "rhyme_results.html", context)
    except:
        all_stresses = rhyme_with_stresses(unstressed_word)[1]
        context = {"unstressed_word": unstressed_word, "all_stresses": all_stresses}
        return render(request, "rhyme.html", context)
