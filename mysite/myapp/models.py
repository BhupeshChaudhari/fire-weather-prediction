from django.db import models

# Create your models here.

class Predict(models.Model):

    Temperature = models.FloatField()
    RH = models.FloatField()
    Ws = models.FloatField()
    Rain = models.FloatField()
    FFMC = models.FloatField()
    DMC = models.FloatField()
    ISI = models.FloatField()
    Classes = models.FloatField()
    Region = models.FloatField()
    FWI = models.CharField(max_length=200)