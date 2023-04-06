from pathlib import Path
from django.shortcuts import render
from rhyme.utils.rhyme import rhyme
print("))))))))))))))))))))))))", Path(__name__))

def rhyme_results(request):
   print("__________________", request.POST)
   unstressed_word = request.POST["rhyme_word"]
   print("________________", request.POST["rhyme_word"])
   table_of_rhymes, all_stresses, stressed_word = rhyme(unstressed_word)
   table_of_rhymes = table_of_rhymes.to_html()
   context = {"table_of_rhymes": table_of_rhymes, "stressed_word": stressed_word}
   return render(request, "rhyme_results.html", context)
