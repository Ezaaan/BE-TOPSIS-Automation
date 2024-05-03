from django.db import models

class TopsisResult(models.Model):
    id = models.AutoField(primary_key=True)
    rank = models.IntegerField()
    name = models.CharField(max_length=100)
    score = models.FloatField()
