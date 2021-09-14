from django.db import models

# Create your models here.

class Emp(models.Model):
    eno = models.IntegerField(primary_key=True) #pri key used to make field default
    ename = models.CharField(max_length=40)
    esal = models.IntegerField()
    #email must be unique, should not be null and not be leave blank
    email = models.EmailField(max_length=255,unique=True,null=True,blank=True)

    def __str__(self):
        return self.email