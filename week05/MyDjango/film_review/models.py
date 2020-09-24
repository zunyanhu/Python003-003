from django.db import models


# Create your models here.
class T1(models.Model):
    id = models.BigAutoField(primary_key=True)
    sentiment = models.IntegerField()
    short = models.CharField(max_length=500)
    n_star = models.IntegerField()

    class Meta:
        managed = False
        db_table = 't1'
