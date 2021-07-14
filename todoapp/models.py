from django.db import models
from django.db.models.base import Model

# Create your models here.


# class UserProfile(models.Model):
#     firstname=models.CharField(max_length=200)
#     lastname=models.CharField(max_length=30)
#     tasks=models.ManyToManyField()





class Task(models.Model):
    task=models.CharField(max_length=100)
    priority=models.IntegerField(default=1)
    duration=models.IntegerField(default=30)

    def __str__(self):
        return f"{self.task}....{self.priority}.....{self.duration}"
