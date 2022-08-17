from email.utils import format_datetime
from django.db import models

# Create your models here.

class YuseoText(models.Model):
    id=models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    body = models.TextField()

    def __Str__(self):
        return self.title
    
