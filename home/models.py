from django.db import models

# Create your models here.
class Sual (models.Model):
    Qowner=models.ForeignKey("auth.User" , on_delete=models.CASCADE)
    Title=models.CharField(max_length=100)
    Question=models.TextField(max_length=500)
    pub_date=models.DateTimeField(auto_now_add=True)




