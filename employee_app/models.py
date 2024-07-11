from django.db import models

# Create your models here.
class Employee(models.Model):
    employee_id=models.CharField(max_length=100)
    employee_name=models.CharField(max_length=50)
    email=models.CharField(max_length=100)
    phone_number=models.CharField(max_length=10)
    job_title=models.CharField(max_length=100)

