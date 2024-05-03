from django.db import models

class TopsisResult(models.Model):
    id = models.AutoField(primary_key=True)
    rank = models.IntegerField()
    name = models.CharField(max_length=100)
    score = models.FloatField()


class ScoreRaw(models.Model):
    id = models.AutoField(primary_key=True)
    path = models.CharField(max_length=100)
    sample_size = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
