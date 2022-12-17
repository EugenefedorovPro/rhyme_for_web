from ..models import Rhyme

# insert rhyming data to sqlite
def insert_rhyme_output_to_sql(
    table_of_rhymes_initial, stressed_word, depth_time_for_rhyming
):
    for i in range(0, len(table_of_rhymes_initial)):
        current_row = table_of_rhymes_initial.iloc[i]
        rhyme = current_row[0]
        pattern = current_row[1]
        part_speech = current_row[2]
        score = current_row[3]

        rhyme_output = Rhyme()
        rhyme_output.word_without_stress = stressed_word.replace("'", "")
        rhyme_output.word_with_stress = stressed_word
        rhyme_output.depth_time = depth_time_for_rhyming
        rhyme_output.rhyme = rhyme
        rhyme_output.pattern = pattern
        rhyme_output.part_speech = part_speech
        rhyme_output.score = score

        rhyme_output.save()
