from ..models import Rhyme
import pandas as pd


def fetch_names_fields():
    all_field_objects = Rhyme._meta.fields
    names_fields = [item.name for item in all_field_objects]
    return names_fields


def fetch_rhyme_from_db(stressed_word, depth_time_for_rhyming):
    if (
        Rhyme.objects.filter(word_with_stress=stressed_word).exists() == True
        and max(
            Rhyme.objects.filter(word_with_stress=stressed_word).values_list(
                "depth_time"
            )
        )[0]
        >= depth_time_for_rhyming
    ):
        rhymes_from_db = Rhyme.objects.filter(word_with_stress=stressed_word)
        pd_rhymes_from_db = pd.DataFrame(
            rhymes_from_db.values("rhyme", "pattern", "part_speech", "score")
        )
        pd_rhymes_from_db = pd_rhymes_from_db.rename(
            columns={
                "rhyme": "Рифма",
                "pattern": "Паттерн для создания рифм",
                "part_speech": "Часть речи",
                "score": "Глубина рифмы",
            }
        )
    else:
        pd_rhymes_from_db = pd.DataFrame(0, index=range(3), columns=range(8))
    return pd_rhymes_from_db
