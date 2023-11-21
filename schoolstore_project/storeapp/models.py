from django.db import models

# Create your models here.
class orders(models.Model):
    name=models.CharField(max_length=250)
    dob=models.DateField()
    age=models.IntegerField()
    gender=models.CharField(max_length=250)
    phone=models.IntegerField()
    email=models.EmailField()
    address=models.TextField()
    department=models.CharField(max_length=250)
    course=models.CharField(max_length=250)
    purpose=models.CharField(max_length=250)

    def __str__(self):
        return self.name