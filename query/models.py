from django.db import models

# Create your models here.
class Asked(models.Model):
    owner=models.CharField(max_length=10)
    title=models.CharField(max_length=100)
    question=models.TextField(max_length=500)
   