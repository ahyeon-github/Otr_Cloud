from django.db import models


# Create your models here.
class QuestionSeven(models.Model):
    id=models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=200)
    subtitle=models.CharField(max_length=300, null=True)

    #day=models.IntegerField()   # 0-6

    created_at=models.DateTimeField(auto_now=True)
    #present=models.BooleanField(default=False)
    
    def __str__(self):
        return self.title

class AnswerSeven(models.Model):     
    id=models.BigAutoField(primary_key=True)
    q_id= models.ForeignKey(QuestionSeven, on_delete=models.CASCADE) 
    body = models.TextField(max_length=1500)
    created_at= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body

    def create(self, validated_data):
            return AnswerSeven.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.body = validated_data.get('body', instance.body)
        instance.save()
        return instance