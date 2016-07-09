from django.db import models

# Create your models here.

class Client(models.Model):

    PAN = models.CharField(max_length = 10, blank = False, null = False,
                           verbose_name = "PAN", help_text="Mandatory", unique=True)
    TAN = models.CharField(max_length = 10, blank = True, null = True,
                           verbose_name = "TAN", unique=True)
    STN = models.CharField(max_length = 15, blank = True, null = True,
                           verbose_name = "Service Tax Regn. No.",unique=True)
    CExNo = models.CharField(max_length = 15, blank = True, null = True,
                             verbose_name = "Central Excise Regn. No.", unique=True)
    DOB = models.DateField(verbose_name = "Date of Birth / Registration",
                           help_text="Mandatory")

    created = models.DateTimeField(auto_now_add = True)
    modified = models.DateTimeField(auto_now = True)
    comments = models.TextField(max_length = 1000,
                                verbose_name = "User Comments")

    def __str__(self):
        return self.name()

class Individual(Client):
    GENDER_TYPES = (
        ('m','Male'),
        ('f','Female'),
    )

    First_Name = models.CharField(max_length = 20, blank = False, null = False,
                                  verbose_name = "First Name", help_text="Mandatory")
    Middle_Name = models.CharField(max_length = 20, blank = True, null = True,
                                   verbose_name = "Middle Name")
    Last_Name = models.CharField(max_length = 20, blank = False, null = False,
                                 verbose_name = "Last Name", help_text="Mandatory")
    Gender = models.CharField(max_length = 1, null = False, blank = False,
                              choices = GENDER_TYPES, verbose_name = "Gender", help_text="Mandatory")

    def name(self):
        if self.Middle_Name is None:
            return self.First_Name + " " + self.Last_Name
        else:
            return self.First_Name + " " + self.Middle_Name + " " + self.Last_Name

class Partnership(Client):
    Partnership_Name = models.CharField(max_length = 80, blank = False, null = False,
                                        verbose_name = "LLP Name", help_text="Mandatory", unique=True)

    def name(self):
        return self.Partnership_Name

class LLP(Client):
    LLP_Name = models.CharField(max_length = 80, blank = False, null = False,
                                verbose_name = "LLP Name", help_text="Mandatory", unique=True)
    LLPIN = models.CharField(max_length = 8, blank = False, null = False,
                             verbose_name = "LLP Identification Number", help_text="Mandatory", unique=True)

    def name(self):
        return self.LLP_Name

class Limited_Company(Client):
    COMPANY_TYPES = (
        ('pvt','Pvt_Ltd'),
        ('pub','Pub_Ltd'),
        ('opc','OPC'),
    )

    Company_Name = models.CharField(max_length = 120, blank = False, null = False,
                                    verbose_name = "Company Name", help_text="Mandatory",unique=True)
    Company_CIN = models.CharField(max_length = 21, blank = False, null = False,
                                   verbose_name = "Company CIN", help_text="Mandatory", unique=True)
    Company_Type = models.CharField(max_length = 3, blank = False, null = False,
                                    choices = COMPANY_TYPES, verbose_name = "Company Type",
                                    help_text="Mandatory", default="pvt")

    def name(self):
        return self.Company_Name

class Address(models.Model):
    STATES_IN_INDIA = (
        ('IN-GA','Goa'),
        ('IN-AP','Andhra Pradesh'),
        ('IN-AR','Arunachal Pradesh'),
        ('IN-AS','Assam'),
        ('IN-BR','Bihar'),
        ('IN-CT','Chhattisgarh'),
        ('IN-GJ','Gujarat'),
        ('IN-HR','Haryana'),
        ('IN-HP','Himachal Pradesh'),
        ('IN-JK','Jammu and Kashmir'),
        ('IN-JH','Jharkhand'),
        ('IN-KA','Karnataka'),
        ('IN-KL','Kerala'),
        ('IN-MP','Madhya Pradesh'),
        ('IN-MH','Maharashtra'),
        ('IN-MN','Manipur'),
        ('IN-ML','Meghalaya'),
        ('IN-MZ','Mizoram'),
        ('IN-NL','Nagaland'),
        ('IN-OR','Odisha'),
        ('IN-PB','Punjab'),
        ('IN-RJ','Rajasthan'),
        ('IN-SK','Sikkim'),
        ('IN-TN','Tamil Nadu'),
        ('IN-TG','Telangana'),
        ('IN-TR','Tripura'),
        ('IN-UT','Uttarakhand'),
        ('IN-UP','Uttar Pradesh'),
        ('IN-WB','West Bengal'),
        ('IN-AN','Andaman and Nicobar Islands'),
        ('IN-CH','Chandigarh'),
        ('IN-DN','Dadra and Nagar Haveli'),
        ('IN-DD','Daman and Diu'),
        ('IN-DL','Delhi'),
        ('IN-LD','Lakshadweep'),
        ('IN-PY','Puducherry'),
    )

    Line1 = models.CharField(max_length = 30, blank = False, null = False,
                            verbose_name = "Address Line 1", help_text="Mandatory",)
    Line2 = models.CharField(max_length = 30, blank = False, null = False,
                            verbose_name = "Address Line 2", help_text="Mandatory",)
    State = models.CharField(max_length = 5, null = False, blank = False,
                            choices = STATES_IN_INDIA, verbose_name = "State", help_text="Mandatory", default="IN-GA")
    PIN = models.CharField(max_length = 6, null = False, blank = False,
                            choices = STATES_IN_INDIA, verbose_name = "State", help_text="Mandatory")