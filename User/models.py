from django.db import models
from Guest.models import *


# Create your models here.

class Complainttype(models.Model):
    complainttype_name=models.CharField(max_length=50)

    def __str__(self):
        return self.complainttype_name

class Complaint(models.Model):
    Complaint_content=models.TextField(null=True)
    Complaint_date=models.DateField(auto_now=True)
    Complaint_status=models.IntegerField(default=0)
    Complaint_reply=models.TextField(null=True)
    Complainttype_id=models.ForeignKey(Complainttype,on_delete=models.SET_NULL,null=True)
    worker_id=models.ForeignKey(Worker,on_delete=models.SET_NULL,null=True)
    Landload_id=models.ForeignKey(Landload,on_delete=models.SET_NULL,null=True)
    user_id=models.ForeignKey(UserRegistration,on_delete=models.SET_NULL,null=True)

class Feedback(models.Model):
    feedback_description=models.TextField(null=True)
    feedback_date=models.DateField(auto_now=True)
    user_id=models.ForeignKey(UserRegistration,on_delete=models.SET_NULL,null=True)
    worker_id=models.ForeignKey(Worker,on_delete=models.SET_NULL,null=True)
    Landload_id=models.ForeignKey(Landload,on_delete=models.SET_NULL,null=True)
                                        
                                         