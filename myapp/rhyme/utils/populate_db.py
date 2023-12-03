from rhyme.models import Word, Rhymes

def populate_db(unstressed_word, all_stresses, stressed_word, table):
    new_word, created = Word.objects.get_or_create(unstressed_word = unstressed_word,
                                          all_stresses = all_stresses,
                                          stressed_word = stressed_word
                                          )
    new_word.save()
    for rhyme, score, assonance, pattern in zip(table['rhyme'], table['score'], table['assonance'], table['pattern']):
        new_word.rhymes.create(rhyme = rhyme,
                               score = score,
                               assonance = assonance,
                               pattern = list(pattern)
                               )
    return new_word

