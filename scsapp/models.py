from django.db import models
class Dept(models.Model):
    dept_name = models.CharField(max_length=50)
    def __str__(self):
        return self.dept_name
class Emp(models.Model):
    emp_name=models.CharField(max_length=50)
    job = models.CharField(max_length=50)
    salary = models.IntegerField(default=0)
    dept = models.ForeignKey(Dept,on_delete=models.CASCADE)
    def __str__(self):
        return "empname is "+self.emp_name + " Job is " + (self.job) + "Salary is "+ str(self.salary)