from django.db import models
from django.db.models.base import Model

# Create your models here.
<<<<<<< HEAD
=======


# class UserProfile(models.Model):
#     firstname=models.CharField(max_length=200)
#     lastname=models.CharField(max_length=30)
#     tasks=models.ManyToManyField()





>>>>>>> 77f5f6639a9f979429a2f888a4e49322804f60c2
class Task(models.Model):
    task=models.CharField(max_length=100)
    priority=models.IntegerField(default=1)
    duration=models.IntegerField(default=30)

    def __str__(self):
<<<<<<< HEAD
        return f"{self.task}......{self.priority}.......{self.duration}"
=======
        return f"{self.task}....{self.priority}.....{self.duration}"
>>>>>>> 77f5f6639a9f979429a2f888a4e49322804f60c2
