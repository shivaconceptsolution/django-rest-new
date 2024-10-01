
from django.db import models

class TutorReg(models.Model):
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=10)
    mobileno = models.CharField(max_length=10)
    fname = models.CharField(max_length=20)
    def __str__(self):
        return "username is "+self.username + "Password is "+self.password + " Mobile no is "+self.mobileno + " fname is "+self.fname

class Student(models.Model):
    rno=models.CharField(max_length=10)
    name=models.CharField(max_length=20)
    branch=models.CharField(max_length=10)
    fee = models.CharField(max_length=10)