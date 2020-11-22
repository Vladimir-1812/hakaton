from django.db import models

# Create your models here.

class Problem(models.Model):
    lat = models.FloatField()
    lng = models.FloatField()
    type = models.IntegerField()
    date = models.DateTimeField()
    description = models.CharField(max_length=1500)
    votes_pos = models.IntegerField()
    votes_neg = models.IntegerField()
    author_id = models.IntegerField()