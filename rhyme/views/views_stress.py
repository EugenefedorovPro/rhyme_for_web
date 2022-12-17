from django.shortcuts import render, redirect
from django.http import request, HttpResponse
from django.template import loader
from django.urls import reverse

from ..forms import (
    StressVariantsForm,
)
from ..utils import stressed_by_nn_variants


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
