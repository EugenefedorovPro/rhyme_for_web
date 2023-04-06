from rhyme_rus.rhyme import rhyme, rhyme_with_stresses

def rhyme(unstressed_word):
    table, all_stresses, stressed_word = rhyme_with_stresses(unstressed_word)
    return table, all_stresses, stressed_word
