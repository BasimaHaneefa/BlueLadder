from django.db import models


# Create your models here.

class District(models.Model):
    district_name=models.CharField(max_length=50)

    def __str__(self):
        return self.district_name

class Workertype(models.Model):
    workertype_name=models.CharField(max_length=50)

    def __str__(self):
        return self.workertype_name 

class Place(models.Model):
    place_name=models.CharField(max_length=50)
    district=models.ForeignKey(District,on_delete=models.CASCADE)

    def __str__(self):
        return self.place_name

class Location(models.Model):
    location_name=models.CharField(max_length=50)
    place=models.ForeignKey(Place,on_delete=models.CASCADE)

    def __str__(self):
        return self.location_name        


class AdminReg(models.Model):
    admin_name=models.CharField(max_length=50)
    admin_email=models.EmailField(unique=True)
    admin_password=models.CharField(max_length=50,unique=True)

