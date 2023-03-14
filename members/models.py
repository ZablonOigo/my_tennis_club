from django.db import models


class Member(models.Model):
    firstname=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)
    gender=models.CharField(max_length=100)
    phone=models.IntegerField()
    joined_date=models.DateTimeField()

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

# Create your models here.
