from msilib.schema import Condition
from django.db import models

# Create your models here.
class student1(models.Model):
    prn_no      = models.IntegerField()
    fname       = models.CharField(max_length=20)
    lname       = models.CharField(max_length=20)
    dob         = models.DateField()
    address     = models.CharField(max_length=20)
    gender      = models.CharField(max_length=20)
    standard    = models.CharField(max_length=20)
    guardian_id = models.CharField(max_length=20)

    class Meta:
        app_label = 'page1'
        db_table='student'

class faculty1(models.Model):

    fid         = models.IntegerField()
    fname       = models.CharField(max_length=20)
    lname       = models.CharField(max_length=20)
    doj         = models.DateField()
    sub_id      = models.CharField(max_length=20)
    gender      = models.CharField(max_length=20)
    address     = models.CharField(max_length=20)
    M_no        = models.CharField(max_length=20)

    class Meta:
        app_label = 'page1'
        db_table='faculty'




class subject1(models.Model):

    sub_id      = models.CharField(max_length=20)
    sub_name    = models.CharField(max_length=20)

    class Meta:
        app_label = 'page1'
        db_table='subject'


class guardian1(models.Model):

    guardian_id    = models.CharField(max_length=20)
    guardian_name  = models.CharField(max_length=20)
    gender         = models.CharField(max_length=20)
    contact        = models.CharField(max_length=20)

    class Meta:
        app_label = 'page1'
        db_table='guardian'



class classroom1(models.Model):

    standard    = models.CharField(max_length=20)
    fid         = models.IntegerField()
    CR          = models.CharField(max_length=20)

    class Meta:
        app_label = 'page1'
        db_table='classroom'