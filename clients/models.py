from django.db import models

# Create your models here.

class Client(models.Model):

	# commented out are the names of the various child classes which will be inheriting from Client class
    # CLIENT_TYPES = (
    #     ('individual','Individual'),
    #     ('llp','Limited Liability Partnership'),
    #     ('opc','One Person Company'),
    #     ('partnership','Partnership Firm'),
    #     ('pvt_ltd','Private Limited Company'),
    #     ('pub_ltd','Public Limited Company'),
    #     ('trust','Trust'),
    # )

    PAN = models.CharField(max_length = 10, blank = False, null = False, verbose_name = "PAN", help_text="Mandatory")
    TAN = models.CharField(max_length = 10, blank = True, null = True, verbose_name = "TAN")
    STN = models.CharField(max_length = 15, blank = True, null = True, verbose_name = "Service Tax Regn. No.")
    CExNo = models.CharField(max_length = 15, blank = True, null = True, verbose_name = "Central Excise Regn. No.")
    DOB = models.DateField(verbose_name = "Date of Birth / Registration", help_text="Mandatory")
    created = models.DateTimeField(auto_now_add = True)
    modified = models.DateTimeField(auto_now = True)
    comments = models.TextField(max_length = 1000, verbose_name = "User Comments")

class Individual(Client):
    GENDER_TYPES = (
        ('m','Male'),
        ('f','Female'),
    )

    First_Name = models.CharField(max_length = 20, blank = False, null = False, verbose_name = "First Name", help_text="Mandatory")
    Middle_Name = models.CharField(max_length = 20, blank = True, null = True, verbose_name = "Middle Name")
    Last_Name = models.CharField(max_length = 20, blank = False, null = False, verbose_name = "Last Name", help_text="Mandatory")
    Gender = models.CharField(max_length = 1, null = False, blank = False, choices = GENDER_TYPES, verbose_name = "Gender", help_text="Mandatory")

class Partnership(Client):
    Partnership_Name = models.CharField(max_length = 80, blank = False, null = False, verbose_name = "LLP Name", help_text="Mandatory")

class LLP(Client):
    LLP_Name = models.CharField(max_length = 80, blank = False, null = False, verbose_name = "LLP Name", help_text="Mandatory")
    LLPIN = models.CharField(max_length = 8, blank = False, null = False, verbose_name = "LLP Identification Number", help_text="Mandatory")

class Limited_Company(Client):
    COMPANY_TYPES = (
        ('pvt','Pvt_Ltd'),
        ('pub','Pub_Ltd'),
        ('opc','OPC'),
    )

    Company_Name = models.CharField(max_length = 120, blank = False, null = False, verbose_name = "Company Name", help_text="Mandatory")
    Company_CIN = models.CharField(max_length = 21, blank = False, null = False, verbose_name = "Company CIN", help_text="Mandatory")
    Company_Type = models.CharField(max_length = 3, blank = False, null = False, choices = COMPANY_TYPES, verbose_name = "Company Type", help_text="Mandatory", default="pvt")
