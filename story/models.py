from django.db import models

# Create your models here.
class Story(models.Model):
    GENDER_CHOICES = [
        (0, '남성'),
        (1, '여성'),
    ]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10)
    front_url = models.CharField(max_length=255)
    back_url = models.CharField(max_length=255)
    saying_url = models.CharField(max_length=255)
    saying = models.CharField(max_length=255)
    nation = models.CharField(max_length=10)
    field = models.CharField(max_length=10)
    access_cnt = models.BigIntegerField(default=0)
    video_url = models.CharField(max_length=255)
    gender = models.BooleanField(choices=GENDER_CHOICES)
    life = models.CharField(max_length=20)
    information_url = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'Story'