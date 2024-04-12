from django.db import models

# Create your models here.
class registertable(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    phoneno=models.CharField(max_length=10)
    date=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)


    class Meta:
        db_table="registertable"