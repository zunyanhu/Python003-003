from django.db import models


# Create your models here.
class T1(models.Model):
    id = models.BigAutoField(primary_key=True)
    sentiment = models.IntegerField()
    short = models.CharField(max_length=500)
    n_star = models.IntegerField()

    def __str__(self):
        return self.short

    class Meta:
        managed = False
        db_table = 't1'
