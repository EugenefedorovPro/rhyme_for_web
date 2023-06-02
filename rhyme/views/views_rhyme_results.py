from rhyme_rus.rhyme import rhyme_with_stresses
from django.shortcuts import render
from rhyme.utils.populate_db import populate_db


def rhyme_results(request):
   unstressed_word = request.POST["target_word"]
   try:
      table_of_rhymes, all_stresses, stressed_word = rhyme_with_stresses(unstressed_word)
      # new_word = populate_db(unstressed_word, all_stresses, stressed_word, table_of_rhymes)
      rhymes = tuple(table_of_rhymes['rhyme'])
      scores = tuple(table_of_rhymes['score'])
      assonances = tuple(table_of_rhymes['assonance'])
      patterns = tuple(table_of_rhymes['pattern'])
      number_rhymes = len(table_of_rhymes)
      cards = []
      for rhyme, score, assonance, pattern in zip(rhymes, scores, assonances, patterns):
         cards.append(tuple((rhyme, score, assonance, pattern)))

      context = {
         'number_rhymes': number_rhymes,
         'stressed_word': stressed_word,
         'cards': cards,
         }
      return render(request, "rhyme_results.html", context)
   except:
      all_stresses = rhyme_with_stresses(unstressed_word)[1]
      context = {'unstressed_word': unstressed_word, 'all_stresses': all_stresses}
      return render(request, 'rhyme.html', context)


# number_rhymes = len(table_of_rhymes)
# new_word = populate_db(unstressed_word, all_stresses, stressed_word, table_of_rhymes)
#
# table_of_rhymes.reset_index(inplace = True)
# new_names = {'index': 'id', 'rhyme': 'Рифма', 'score': 'Штраф', 'assonance': 'Сонанс', 'pattern': 'Паттерн'}
# table_of_rhymes.rename(columns = new_names, inplace = True)
# table_of_rhymes = table_of_rhymes.to_html(index = False)
#
# context = {"table_of_rhymes": table_of_rhymes, "stressed_word": stressed_word, "number_rhymes": number_rhymes}
