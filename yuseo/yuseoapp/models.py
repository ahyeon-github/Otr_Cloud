from django.db import models

# Create your models here.


class Yuseo(models.Model):
    id=models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    image = models.ImageField(upload_to='%Y/%m/%d', null=True)
    voice = models.FileField(upload_to='voice/', null=True)
    video = models.FileField(upload_to='video/', null=True)

    def __Str__(self):
        return self.title
    
    def summary(self):      # 연동 시 필요없다면 삭제해야함.
        return self.body [:30]
