from rhyme_rus.rhyme import rhyme_with_stresses
from django.shortcuts import render
from rhyme.utils.populate_db import populate_db


def rhyme_results(request):
   unstressed_word = request.POST["target_word"]
   try:
      table_of_rhymes, all_stresses, stressed_word = rhyme_with_stresses(unstressed_word)
      new_word = populate_db(unstressed_word, all_stresses, stressed_word, table_of_rhymes)
      number_rhymes = len(table_of_rhymes)
      table_of_rhymes.reset_index(inplace = True)
      new_names = {'index': 'id', 'rhyme': 'Рифма', 'score': 'Штраф', 'assonance': 'Сонанс', 'pattern': 'ттерн'}
      table_of_rhymes.rename(columns = new_names, inplace = True)
      table_of_rhymes = table_of_rhymes.to_html(index = False)
      context = {"table_of_rhymes": table_of_rhymes, "stressed_word": stressed_word, "number_rhymes": number_rhymes}
      return render(request, "rhyme_results.html", context)
   except:
      all_stresses = rhyme_with_stresses(unstressed_word)[1]
      context = {'unstressed_word': unstressed_word, 'all_stresses': all_stresses}
      return render(request, 'rhyme.html', context)