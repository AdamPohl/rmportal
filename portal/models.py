import email
from django.db import models

class School(models.Model):
    urn = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    open_date = models.CharField(max_length=200, null=True)
    close_date = models.CharField(max_length=200, null=True)
    town = models.CharField(max_length=200, null=True)
    postcode = models.CharField(max_length=200, null=True)
    school_website = models.CharField(max_length=200, null=True)
    phone_number = models.CharField(max_length=200, null=True)


class User(models.Model):
    name = models.CharField(max_length=200, null=False)
    surname = models.CharField(max_length=200, null=False)
    email = models.CharField(max_length=200, null=False)
    school = models.CharField(max_length=64)
    dob = models.CharField("Date of birth", max_length=200, null=True)