from django.db import models

class task(models.Model):
    text = models.TextField()
    status = models.CharField(max_length=13)
    date_creation = models.DateTimeField(auto_now=True)
