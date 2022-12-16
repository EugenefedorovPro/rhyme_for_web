from django.shortcuts import render, redirect
from django.http import request, HttpResponse
from django.template import loader
from django.urls import reverse

from .forms import (
    InputWordToStressForm,
    StressVariantsForm,
    DepthTimeForm,
    InputWordWithoutStress,
)
from django.http import HttpResponseRedirect
from rhyme_rus.rhyme import rhyme_to_table, stress_word_by_wiki, stress_word_by_nn
from .utils import stressed_by_nn_variants


def title(request):
    return render(request, "title.html")


def rhyme(request):
    if request.method == "POST":
        word_without_stress = InputWordWithoutStress(request.POST)
        depth_time = DepthTimeForm(request.POST)
        if word_without_stress.is_valid and depth_time.is_valid:
            return HttpResponseRedirect("rhyme/results/")
    else:
        depth_time = DepthTimeForm()
        input_word_without_stress = InputWordWithoutStress()
        return render(
            request,
            "rhyme.html",
            {
                "depth_time": depth_time,
                "input_word_without_stress": input_word_without_stress,
            },
        )


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

    table_of_rhymes = rhyme_to_table(
        stressed_word,
        max_length_pat_of_ipa=max_length_pat_of_ipa,
        list_score_numbers=list_score_numbers,
        max_number_hard_sounds_in_one_pat=max_number_hard_sounds_in_one_pat,
    )
    table_of_rhymes = "\n".join(table_of_rhymes["rhymes"])
    return render(
        request,
        "results.html",
        {"stressed_word": stressed_word, "table_of_rhymes": table_of_rhymes},
    )


def stress(request, word_stressed_by_nn, unstressed_word, tuple_of_omographs):
    if tuple_of_omographs and word_stressed_by_nn == 0:
        tuple_of_stressed_words = tuple([(word, word) for word in tuple_of_omographs])
        index_of_word_stressed_by_nn_in_tuple_of_stressed_word = 0
    else:
        tuple_of_stressed_words = stressed_by_nn_variants.make_tuple_of_stress_variants(
            unstressed_word
        )
        index_of_word_stressed_by_nn_in_tuple_of_stressed_word = [
            item[0]
            for item in tuple_of_stressed_words
            if item[1] == word_stressed_by_nn
        ]

    select = StressVariantsForm(
        tuple_of_stressed_words,
        initial={"select": index_of_word_stressed_by_nn_in_tuple_of_stressed_word},
    )
    return render(
        request,
        "stress.html",
        {
            "unstressed_word": unstressed_word,
            "word_stressed_by_nn": word_stressed_by_nn,
            "select": select,
        },
    )


def transcribe(request):
    word_as_ipa = "Here goes word in IPA notation"
    return render(request, "transcribe.html", {"word_as_ipa": word_as_ipa})
