# tuning depth of rhyming - time of processing parameter as an input for thyme_to_table


def setup_depth_rhyme(depth_time_for_rhyming):
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
    return max_length_pat_of_ipa, list_score_numbers, max_number_hard_sounds_in_one_pat
