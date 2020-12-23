from django.db import models
from django.utils.crypto import get_random_string
from django.contrib.auth.models import AbstractUser

 
class User(AbstractUser):
    is_individual = models.BooleanField(default=True)
    is_bulk       = models.BooleanField(default=False)
    is_commercial = models.BooleanField(default=False)
    is_industrial = models.BooleanField(default=False)
    

class Individual(models.Model):
    user  = models.OneToOneField(User,on_delete=models.CASCADE)
    customer_id  = models.CharField(max_length = 10,default=get_random_string(10).upper(),editable=False)
    email =  models.EmailField(null=False,blank=False)
    address =  models.CharField(max_length=500, null=False,blank=False)
    phone_number  = models.CharField(max_length=10,null=False,blank=False)

    def __str__(self):
        return self.customer_id

class Bulk(models.Model):
    user  = models.OneToOneField(User,on_delete=models.CASCADE)
    customer_id  = models.CharField(max_length = 10,default=get_random_string(10).upper(),editable=False)
    email =  models.EmailField(null=False,blank=False)
    address =  models.CharField(max_length=500, null=False,blank=False)
    phone_number  = models.CharField(max_length=10,null=False,blank=False)

    def __str__(self):
        return self.customer_id

class Commercial(models.Model):
    user  = models.OneToOneField(User,on_delete=models.CASCADE)
    customer_id  = models.CharField(max_length = 10,default=get_random_string(10).upper(),editable=False)
    email =  models.EmailField(null=False,blank=False)
    address =  models.CharField(max_length=500, null=False,blank=False)
    phone_number  = models.CharField(max_length=10,null=False,blank=False)

    def __str__(self):
        return self.customer_id

class Industrial(models.Model):
    user  = models.OneToOneField(User,on_delete=models.CASCADE)
    customer_id  = models.CharField(max_length = 10,default=get_random_string(10).upper(),editable=False)
    email =  models.EmailField(null=False,blank=False)
    address =  models.CharField(max_length=500, null=False,blank=False)
    phone_number  = models.CharField(max_length=10,null=False,blank=False)

    def __str__(self):
        return self.customer_id

class PickUp(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    bin_type = models.CharField(max_length=100, null=False, blank=False)
    weight  =  models.DecimalField(max_digits=50, decimal_places=12)
    schedule_date =  models.DateField(null=False,blank=False)
    picked_date =  models.DateField(null=True,blank=True)
    is_pickedup = models.CharField(max_length=3,default='No',null=True,blank=True)
    recurring  = models.CharField(max_length=120,null=False,blank=False)
    notes = models.CharField(max_length=700, null=True,blank=True)

    