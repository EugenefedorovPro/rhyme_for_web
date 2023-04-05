from django.db import models


class Meta:
    indexes = [
        models.Index(fields = ['unstressed_word', ]),
        models.Index(fields = ['stressed_word', ]),
        models.Index(fields = ['rhyme', ]),
        models.Index(fields = ['score', ]),
        models.Index(fields = ['assonance', ]),
        ]
class Word(models.Model):
    unstressed_word = models.CharField(max_length = 100)
    all_stresses = models.JSONField(default = '')
    stressed_word = models.CharField(max_length = 100, default = '')

    def __str__(self):
        return self.unstressed_word


class Rhymes(models.Model):
    word = models.ForeignKey(Word, on_delete = models.CASCADE)
    rhyme = models.CharField(max_length = 100)
    score = models.IntegerField()
    assonance = models.IntegerField()
    pattern = models.JSONField()

    def __str__(self):
        return self.rhyme
