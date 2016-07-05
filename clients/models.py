from django.db import models

# Create your models here.

class Client(models.Model):
    CLIENT_TYPES = (
        ('individual','Individual'),
        ('llp','Limited Liability Partnership'),
        ('opc','One Person Company'),
        ('partnership','Partnership Firm'),
        ('pvt_ltd','Private Limited Company'),
        ('pub_ltd','Public Limited Company'),
        ('trust','Trust'),
    )

    PAN = models.CharField(max_length=10, blank=False, null=False)
    DOB = models.DateField()
    Type = models.CharField(max_length=11, null=False, choices=CLIENT_TYPES)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    comments = models.TextField(max_length=1000)

    class Meta:
        abstract = True


class Individual(Client):
    GENDER_TYPES = (
        ('m','Male'),
        ('f','Female'),
    )

    First_Name = models.CharField(max_length=20, blank=False, null=False)
    Middle_Name = models.CharField(max_length=20, blank=True, null=True)
    Last_Name = models.CharField(max_length=20, blank=False, null=False)
    Gender = models.CharField(max_length=1, null=False, choices=GENDER_TYPES)