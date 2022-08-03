from django.db import models

# Create your models here.


class Yuseo(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    image = models.ImageField(upload_to='%Y/%m/%d', null=True)
  
    
    def __Str__(self):
        return self.title
    
    def summary(self):
        return self.body [:30]


