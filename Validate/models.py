from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    loc=models.CharField(max_length=100)
    email=models.EmailField()
    remail=models.EmailField()
    url=models.URLField()

    def __str__(self) -> str:
        return self.name