from django.db import models

# Create your models here.





class course(models.Model):
    subjects = models.CharField(max_length=50)
    duration = models.CharField(max_length=50)
    fee = models.IntegerField()


class create(models.Model):
    sname = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    fee = models.IntegerField()