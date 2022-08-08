from django.db import models

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title

class Answer(models.Model):     # User Field 추가 필요
    question= models.ForeignKey(Question, on_delete=models.CASCADE)     # CASCADE: Question 사라지면 같이 삭제되도록 하는 것인데, 필요없을지도
    content = models.CharField(max_length=500)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content