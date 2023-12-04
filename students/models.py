from django.db import models

# Create your models here.
class Courses(models.Model):
    name = models.CharField(max_length=200)

class Students(models.Model):
    name = models.CharField(max_length=200)
    courses = models.ManyToManyField('Courses')