from django.db import models
from django.urls import reverse
# Create your models here.
class students(models.Model):
    name = models.CharField(max_length=20)
    fathername = models.CharField(max_length=20)
    classname = models.IntegerField()
    contact = models.CharField(max_length=20)

class Teacher(models.Model):
    name = models.CharField(max_length=20)
    exp = models.IntegerField()
    subject = models.CharField(max_length=20)
    contact = models.CharField(max_length=20)

    def get_absolute_url(self):
        return reverse('listteacher')
