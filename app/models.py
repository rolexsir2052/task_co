from django.db import models

# Create your models here.
class Normal(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    salary=models.IntegerField()
    def __str__(self):
        return self.name
class Google(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    salary=models.IntegerField()
    def __str__(self):
        return self.name