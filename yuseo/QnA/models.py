from django.db import models

from users.models import User

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=200)
    subtitle=models.CharField(max_length=300, null=True)

    day=models.IntegerField()   # 0-6

    created_at=models.DateTimeField(auto_now=True)
    present=models.BooleanField(default=False)
    
    def __str__(self):
        return self.title

class Answer(models.Model):     # User Field 추가 필요 > 하긴 했음
    question= models.ForeignKey(Question, on_delete=models.CASCADE)     # CASCADE: Question 사라지면 같이 삭제되도록 하는 것인데, 필요없을지도
    body = models.TextField(max_length=1500)
    created_at= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body

    def create(self, validated_data):
            return Answer.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.body = validated_data.get('body', instance.body)
        instance.save()
        return instance