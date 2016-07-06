from django.db import models

# Create your models here.

class Client(models.Model):

    PAN = models.CharField(max_length = 10, blank = False, null = False, verbose_name = "PAN", help_text="Mandatory")
    TAN = models.CharField(max_length = 10, blank = True, null = True, verbose_name = "TAN")
    STN = models.CharField(max_length = 15, blank = True, null = True, verbose_name = "Service Tax Regn. No.")
    CExNo = models.CharField(max_length = 15, blank = True, null = True, verbose_name = "Central Excise Regn. No.")
    DOB = models.DateField(verbose_name = "Date of Birth / Registration", help_text="Mandatory")
    created = models.DateTimeField(auto_now_add = True)
    modified = models.DateTimeField(auto_now = True)
    comments = models.TextField(max_length = 1000, verbose_name = "User Comments")

    class Meta:
        abstract = True


class Individual(Client):
    GENDER_TYPES = (
        ('m','Male'),
        ('f','Female'),
    )

    First_Name = models.CharField(max_length = 20, blank = False, null = False, verbose_name = "First Name", help_text="Mandatory")
    Middle_Name = models.CharField(max_length = 20, blank = True, null = True, verbose_name = "Middle Name")
    Last_Name = models.CharField(max_length = 20, blank = False, null = False, verbose_name = "Last Name", help_text="Mandatory")
    Gender = models.CharField(max_length = 1, null = False, choices = GENDER_TYPES, verbose_name = "Gender", help_text="Mandatory")