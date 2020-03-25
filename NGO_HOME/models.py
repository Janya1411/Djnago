from django.db import models


class NGO(models.Model):
    Ngo_Number = models.IntegerField(primary_key=True)
    name = models.TextField(max_length=100,null=False)
    Address = models.TextField(max_length=100,null=True)
    Contact_No = models.TextField(null=True)
    Email_ID = models.EmailField(null=True)
    Website = models.CharField(max_length=100,null=True)
    Area = models.CharField(max_length=100,null=True)
    Domain = models.CharField(max_length=100,null=True)





