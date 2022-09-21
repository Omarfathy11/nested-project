from statistics import mode
from django.db import models

# Create your models here.
class Instructor(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=200)


    def __str__(self):
        return self.email

class course(models.Model):  
    title = models.CharField(max_length=100)
    rating = models.IntegerField()
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, related_name='courses')
