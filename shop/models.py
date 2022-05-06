from django.db import models

# Create your models here.
class users(models.Model):
    uno=models.IntegerField()
    uname=models.CharField(max_length=30)
    upass=models.CharField(max_length=16)
    uemail=models.EmailField(max_length=30)
    umob=models.IntegerField()