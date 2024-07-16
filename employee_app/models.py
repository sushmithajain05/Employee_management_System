from django.db import models
from datetime import date, datetime

# Create your models here.
class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_name=models.CharField(max_length=255)
    email=models.EmailField(max_length=40)
    phone_number=models.CharField(max_length=10)
    job_title=models.CharField(max_length=100)
    created_at = models.DateTimeField(default=datetime.now,blank=True)
    updated_at = models.DateTimeField(auto_now=True)

class Attendance(models.Model):
    attendance_id=models.CharField(max_length=10)
    employee_id= models.ForeignKey(Employee, on_delete=models.CASCADE)
    date=models.DateField(max_length=10)
    present=models.CharField(max_length=20)
    created_at = models.DateTimeField(default=datetime.now,blank=True)
    updated_at = models.DateTimeField(auto_now=True)






