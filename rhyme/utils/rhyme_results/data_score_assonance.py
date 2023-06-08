import pandas as pd
import json

class DataScoreAssonance:
    table_of_rhymes: pd.DataFrame
    scores: pd.Series
    assonances: pd.Series
    def __init__(self, table_of_rhymes, scores, assonances):
        self.table_of_rhymes = table_of_rhymes
        self.scores = scores
        self.assonances = assonances
        self.data_assonances_by_score: json = self.__get_data(
            self.table_of_rhymes,
            self.scores,
            self.assonances,
            'score',
            'assonance'
            )
        self.data_scores_by_assonance: json = self.__get_data(
            self.table_of_rhymes,
            self.assonances,
            self.scores,
            'assonance',
            'score'
            )
        self.all_score_values: json = json.dumps(list(set(table_of_rhymes['score'])))
        self.all_assonance_values: json = json.dumps(list(set(table_of_rhymes['assonance'])))

    def __get_data(self, df, series_keys, series_values, name_key, name_value):
        all_values: set = set(series_values)
        data: dict | json = dict()
        for key in series_keys:
            values_by_key: pd.Series = df[df[name_key] == key][name_value]
            values_by_key: set = set(values_by_key)
            values_to_hide: list|set = list(all_values.difference(values_by_key))
            data[key] = values_to_hide
        data = json.dumps(data)
        return data

