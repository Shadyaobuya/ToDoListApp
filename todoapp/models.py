from django.db import models

# Create your models here.
class Task(models.Model):
    task=models.CharField(max_length=100)
    priority=models.IntegerField(default=1)
    duration=models.IntegerField(default=30)

    def __str__(self):
        return f"{self.task}......{self.priority}.......{self.duration}"
