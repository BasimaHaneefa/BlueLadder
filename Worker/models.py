from django.db import models
from Guest.models import UserRegistration,Worker

# Create your models here.

class Work(models.Model):
    work_details=models.CharField(max_length=50)
    work_image=models.FileField(upload_to='userdocs/')
    work_amount=models.IntegerField(default=0)
    worker_id=models.ForeignKey(Worker,on_delete=models.SET_NULL,null=True)

class Workbooking(models.Model):
    workbooking_date=models.DateField(auto_now=True)
    workbooking_fordate=models.DateField()
    workbooking_status=models.IntegerField(default=0)
    payment_status=models.IntegerField(default=0)
    work_id=models.ForeignKey(Work,on_delete=models.SET_NULL,null=True)
    user_id=models.ForeignKey(UserRegistration,on_delete=models.SET_NULL,null=True)


class WorkerBooking(models.Model):
    w_details=models.TextField()
    wbookingdate=models.DateField(auto_now=True)
    wbooking_fordate=models.DateField()
    w_bstatus=models.IntegerField(default=0)
    p_status=models.IntegerField(default=0)
    worker_id=models.ForeignKey(Worker,on_delete=models.SET_NULL,null=True)
    user_id=models.ForeignKey(UserRegistration,on_delete=models.SET_NULL,null=True)



