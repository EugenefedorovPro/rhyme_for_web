from django.db import models


class Rhyme(models.Model):
    word_without_stress = models.CharField(
        max_length=100, default="any unstressed word"
    )
    word_with_stress = models.CharField(max_length=100, default="any stressed word")
    depth_time = models.IntegerField(default=2)
    rhyme = models.CharField(max_length=100, default="any rhymed word")
    pattern = models.JSONField()
    part_speech = models.CharField(max_length=50, default="any part of speech")
    score = models.IntegerField()

    def __str__(self):
        return self.word_with_stress + "_" + str(self.depth_time)
