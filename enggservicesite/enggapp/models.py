from django.db import models
from django.utils import timezone
# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=100,null=False)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name


class Employee(models.Model):
    emp_id = models.CharField(max_length=200, null=False, default='')
    name_of_candidate = models.CharField(max_length=100, null=False)
    user_status = models.BooleanField(null=False, default=0) # (Active - 1/Inactive - 0)
    certification_name = models.CharField(max_length=50, null=True)
    certification_code = models.CharField(max_length=50, null=True)
    certification_status = models.BooleanField(null=True) # Active - True/Expired - False

    # dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    # salary = models.IntegerField(default=0)
    # bonus = models.IntegerField(default=0)
    # role = models.ForeignKey(Role, on_delete=models.CASCADE)
    # phone = models.IntegerField(default=0)
    # hire_date = models.DateField()
    
    # SPE/Specialty
    competency = models.IntegerField(default=0)
    # TaggedOnPN
    # Internal/External/Both
    trackLevel = models.IntegerField(default=0)
    completetion_date = models.DateField()
    name_of_pn = models.CharField(max_length=50, null=True)
    course_code = models.CharField(max_length=50, null=True)
    comments = models.CharField(max_length=200, null=True)
    email_notification_status = models.BooleanField(null=True)
    created_date = models.DateTimeField(auto_now=True, null=True)
    updated_date = models.DateField(auto_now=True)
    validity_of_certificate = models.DateField(auto_now=True)

    def __str__(self):
        return "%s %s %s" %(self.name_of_candidate, self.user_status, self.course_code)