from django.db import models
from Admin.models import Location
from Guest.models import *

# Create your models here.

class Plot(models.Model):
    plot_des=models.CharField(max_length=50)
    plot_image=models.FileField(upload_to='userdocs/')
    plot_amount=models.IntegerField(default=0)
    location_id=models.ForeignKey(Location,on_delete=models.SET_NULL,null=True)
    Landload_id=models.ForeignKey(Landload,on_delete=models.SET_NULL,null=True)

class Plotbooking(models.Model):
    plotbooking_date=models.DateField(auto_now=True)
    plotbooking_status=models.IntegerField(default=0)    
    payment_status=models.IntegerField(default=0)
    user_id=models.ForeignKey(UserRegistration,on_delete=models.SET_NULL,null=True)
    plot_id=models.ForeignKey(Plot,on_delete=models.SET_NULL,null=True)