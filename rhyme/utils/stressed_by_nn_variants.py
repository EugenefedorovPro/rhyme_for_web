def make_tuple_of_stress_variants(word_without_stress):
    vowels = ["а", "у", "о", "ы", "э", "я", "ю", "ё", "и", "е"]
    tuple_of_stress_variants = []
    # count = 0
    for i, letter in enumerate(word_without_stress):
        if letter in vowels:
            # count += 1
            letter += "'"
            stressed_word = (
                word_without_stress[:i] + letter + word_without_stress[i:][1:]
            )
            tuple_of_stress_variants.append((stressed_word, stressed_word))
    return tuple(tuple_of_stress_variants)
