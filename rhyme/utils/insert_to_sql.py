from ..models import Rhyme

# insert rhyming data to sqlite


def assign_values_to_rhyme_model(
    stressed_word, depth_time_for_rhyming, current_row, rhyme
):
    # assigning data fields for db
    pattern = current_row[1]
    part_speech = current_row[2]
    score = current_row[3]

    # writing new data to db
    rhyme_output = Rhyme()
    rhyme_output.word_without_stress = stressed_word.replace("'", "")
    rhyme_output.word_with_stress = stressed_word
    rhyme_output.depth_time = depth_time_for_rhyming
    rhyme_output.rhyme = rhyme
    rhyme_output.pattern = pattern
    rhyme_output.part_speech = part_speech
    rhyme_output.score = score

    rhyme_output.save()


def insert_rhyme_output_to_sql(table_of_rhymes, stressed_word, depth_time_for_rhyming):
    # check is stressed word is available in db
    if Rhyme.objects.filter(word_with_stress=stressed_word).exists() == False:

        for i in range(0, len(table_of_rhymes)):
            current_row = table_of_rhymes.iloc[i]
            rhyme = current_row[0]

            assign_values_to_rhyme_model(
                stressed_word, depth_time_for_rhyming, current_row, rhyme
            )

    else:

        for i in range(0, len(table_of_rhymes)):
            current_row = table_of_rhymes.iloc[i]
            rhyme = current_row[0]

            # check if the rhyme of the stressed word is available in db
            if Rhyme.objects.filter(rhyme=rhyme).exists() == False:

                assign_values_to_rhyme_model(
                    stressed_word, depth_time_for_rhyming, current_row, rhyme
                )
