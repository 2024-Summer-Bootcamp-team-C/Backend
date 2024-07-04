from django.db import models

# Create your models here.
class greatslist(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10)
    silhouette_url = models.CharField(max_length=255)
    photo_url = models.CharField(max_length=255)
    saying = models.CharField(max_length=255)
    puzzleCnt = models.IntegerField(default=0)

    class Meta:
        db_table = 'greatslist'

