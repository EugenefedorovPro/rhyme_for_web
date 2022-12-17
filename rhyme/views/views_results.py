from django.shortcuts import render, redirect
from django.http import request, HttpResponse
from django.template import loader
from django.urls import reverse

from ..models import Rhyme
from ..utils import insert_to_sql

from django.http import HttpResponseRedirect
from rhyme_rus.rhyme import rhyme_to_table, stress_word_by_wiki, stress_word_by_nn


def results(request):
    depth_time_transient = request.POST.get("scale", False)
    if depth_time_transient:
        global depth_time_for_rhyming
        depth_time_for_rhyming = int(depth_time_transient)

    # after user selected stress variants made by nn
    if "select" in request.POST.keys():
        stressed_word = request.POST["select"]
    # if word is in wiki and does not requiere accentuating by nn
    else:
        unstressed_word = request.POST.get("user_input_to_rhyme", False)
        try:
            stressed_word = stress_word_by_wiki(unstressed_word)
            if len(stressed_word) == 1:
                stressed_word = stressed_word[0]
            else:
                tuple_of_omographs = stressed_word
                word_stressed_by_nn = 0
                return redirect(
                    "stress",
                    word_stressed_by_nn=word_stressed_by_nn,
                    unstressed_word=unstressed_word,
                    tuple_of_omographs=tuple_of_omographs,
                )
        except KeyError:
            word_stressed_by_nn = stress_word_by_nn(unstressed_word)
            tuple_of_omographs = 0
            return redirect(
                "stress",
                word_stressed_by_nn=word_stressed_by_nn,
                unstressed_word=unstressed_word,
                tuple_of_omographs=tuple_of_omographs,
            )

    # tuning depth of rhyming - time of processing parameter as an input for thyme_to_table
    if depth_time_for_rhyming == 2:
        max_length_pat_of_ipa = 6
        list_score_numbers = range(0, 45, 5)
        max_number_hard_sounds_in_one_pat = 1
    if depth_time_for_rhyming == 1:
        max_length_pat_of_ipa = 5
        list_score_numbers = range(0, 30, 5)
        max_number_hard_sounds_in_one_pat = 1
    if depth_time_for_rhyming == 3:
        max_length_pat_of_ipa = 6
        list_score_numbers = range(0, 50, 5)
        max_number_hard_sounds_in_one_pat = 1
    if depth_time_for_rhyming == 4:
        max_length_pat_of_ipa = 7
        list_score_numbers = range(0, 100, 5)
        max_number_hard_sounds_in_one_pat = 1
    if depth_time_for_rhyming == 5:
        max_length_pat_of_ipa = 7
        list_score_numbers = range(0, 100, 5)
        max_number_hard_sounds_in_one_pat = 2

    table_of_rhymes_initial = rhyme_to_table(
        stressed_word,
        max_length_pat_of_ipa=max_length_pat_of_ipa,
        list_score_numbers=list_score_numbers,
        max_number_hard_sounds_in_one_pat=max_number_hard_sounds_in_one_pat,
    )
    table_of_rhymes = "\n".join(table_of_rhymes_initial["rhymes"])

    # insert rhyme data to db
    insert_to_sql.insert_rhyme_output_to_sql(
        table_of_rhymes_initial, stressed_word, depth_time_for_rhyming
    )

    return render(
        request,
        "results.html",
        {"stressed_word": stressed_word, "table_of_rhymes": table_of_rhymes},
    )
