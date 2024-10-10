from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    text = models.TextField()
    status = models.CharField(max_length=13)
    date_creation = models.DateTimeField(auto_now_add=True)
    
    class meta():
        db_table = 'Task'
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
