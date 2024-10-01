from django.db import models

class People(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField()

class Students(People):
    grade = models.IntegerField()

class Teachers(People):
    branch = models.CharField(max_length=30)
    numberOfClasses = models.IntegerField()
