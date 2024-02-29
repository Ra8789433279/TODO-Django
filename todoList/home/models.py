from django.db import models

# Create your models here.

class tasks(models.Model):
    tasksTitle = models.CharField(max_length=30)
    tasksDesc = models.TextField()
    time = models.DateTimeField(auto_now_add=True)


def __str__(self):
    return self.tasksTitle