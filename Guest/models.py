from django.db import models
from Admin.models import Location,Workertype

# Create your models here.

class UserRegistration(models.Model):
    user_name=models.CharField(max_length=50)
    user_contact=models.CharField(max_length=10)
    user_email=models.EmailField(unique=True)
    user_address=models.TextField(null=True)
    user_location=models.ForeignKey(Location,on_delete=models.SET_NULL,null=True)
    user_photo=models.FileField(upload_to='userdocs/')
    user_proof=models.FileField(upload_to='userdocs/')
    user_pswrd=models.CharField(max_length=50,unique=True)
    user_doj=models.DateField(auto_now=True)

class Worker(models.Model):
    worker_name=models.CharField(max_length=50)
    worker_address=models.TextField(null=True)
    worker_contact=models.CharField(max_length=10)
    worker_email=models.EmailField(unique=True)
    worker_photo=models.FileField(upload_to='userdocs/')
    worker_password=models.CharField(max_length=50,unique=True)
    worker_proof=models.FileField(upload_to='userdocs/')
    worker_vstatus=models.IntegerField(default=0)
    worker_doj=models.DateField(auto_now=True)
    worker_typeid=models.ForeignKey(Workertype,on_delete=models.SET_NULL,null=True) 
    location_id=models.ForeignKey(Location,on_delete=models.SET_NULL,null=True)

class Landload(models.Model):
    landload_name=models.CharField(max_length=50)
    landload_address=models.TextField(null=True)
    landload_contact=models.CharField(max_length=10)
    landload_email=models.EmailField(unique=True)
    landload_photo=models.FileField(upload_to='userdocs/')
    landload_password=models.CharField(max_length=50,unique=True)
    landload_proof=models.FileField(upload_to='userdocs/')
    landload_vstatus=models.IntegerField(default=0)
    landload_doj=models.DateField(auto_now=True)
    location_id=models.ForeignKey(Location,on_delete=models.SET_NULL,null=True)

        

    