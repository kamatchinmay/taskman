from django.db import models
from taskman.utils import make_title_case
from model_utils.managers import InheritanceManager

# Create your models here.

class ClientAbstractBase(models.Model):
# as explained in http://blog.headspin.com/?p=474

	# Make a place to store the class name of the child
	_my_subclass = models.CharField(max_length=200)

	class Meta:
		abstract = True

	def as_child(self):
		return getattr(self, self._my_subclass)

	def save(self, *args, **kwargs):
		# save what kind we are.
		self._my_subclass = self.__class__.__name__.lower()
		super(ClientAbstractBase, self).save(*args, **kwargs)

class Client(ClientAbstractBase):

	objects = InheritanceManager()

	PAN = models.CharField(max_length=10, blank=False, null=False,
						   verbose_name="PAN", help_text="Mandatory", unique=True)
	TAN = models.CharField(max_length=10, blank=True, null=True,
						   verbose_name="TAN", unique=True)
	STN = models.CharField(max_length=15, blank=True, null=True,
						   verbose_name="Service Tax Regn. No.",unique=True)
	CExNo = models.CharField(max_length=15, blank=True, null=True,
							 verbose_name="Central Excise Regn. No.", unique=True)
	DOB = models.DateField(verbose_name="Date of Birth / Registration",
						   help_text="Mandatory")


	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	comments = models.TextField(max_length=1000,
								verbose_name="User Comments")

	def __str__(self):
		return self.as_child().name()


class Individual(Client):
	GENDER_TYPES = (
		('m', 'Male'),
		('f', 'Female'),
	)

	First_Name = models.CharField(max_length=20, blank=False, null=False,
								  verbose_name="First Name", help_text="Mandatory")
	Middle_Name = models.CharField(max_length=20, blank=True, null=True,
								   verbose_name="Middle Name")
	Last_Name = models.CharField(max_length=20, blank=False, null=False,
								 verbose_name="Last Name", help_text="Mandatory")
	Gender = models.CharField(max_length=1, null=False, blank=False,
							  choices=GENDER_TYPES, verbose_name="Gender", help_text="Mandatory")

	def name(self):
		if self.Middle_Name is None:
			return self.First_Name + " " + self.Last_Name
		else:
			return self.First_Name + " " + self.Middle_Name + " " + self.Last_Name

class Partnership(Client):
	Partnership_Name=models.CharField(max_length=80, blank=False, null=False,
									  verbose_name="LLP Name", help_text="Mandatory", unique=True)

	def name(self):
		return self.Partnership_Name

class LLP(Client):
	LLP_Name = models.CharField(max_length=80, blank=False, null=False,
								verbose_name="LLP Name", help_text="Mandatory", unique=True)
	LLPIN = models.CharField(max_length=8, blank=False, null=False,
							 verbose_name="LLP Identification Number", help_text="Mandatory", unique=True)

	def name(self):
		return self.LLP_Name

class Limited_Company(Client):
	COMPANY_TYPES = (
		('pvt', 'Pvt_Ltd'),
		('pub', 'Pub_Ltd'),
		('opc', 'OPC'),
	)

	Company_Name = models.CharField(max_length=120, blank=False, null=False,
                                    verbose_name="Company Name", help_text="Mandatory",unique=True)
	Company_CIN = models.CharField(max_length=21, blank=False, null=False,
                                   verbose_name="Company CIN", help_text="Mandatory", unique=True)
	Company_Type = models.CharField(max_length=3, blank=False, null=False,
                                    choices=COMPANY_TYPES, verbose_name="Company Type",
                                    help_text="Mandatory", default="pvt")

	def name(self):
		return self.Company_Name

class Address(models.Model):
	STATES_IN_INDIA = (
		('IN-GA', 'Goa'),
		('IN-AP', 'Andhra Pradesh'),
		('IN-AR', 'Arunachal Pradesh'),
		('IN-AS', 'Assam'),
		('IN-BR', 'Bihar'),
		('IN-CT', 'Chhattisgarh'),
		('IN-GJ', 'Gujarat'),
		('IN-HR', 'Haryana'),
		('IN-HP', 'Himachal Pradesh'),
		('IN-JK', 'Jammu and Kashmir'),
		('IN-JH', 'Jharkhand'),
		('IN-KA', 'Karnataka'),
		('IN-KL', 'Kerala'),
		('IN-MP', 'Madhya Pradesh'),
		('IN-MH', 'Maharashtra'),
		('IN-MN', 'Manipur'),
		('IN-ML', 'Meghalaya'),
		('IN-MZ', 'Mizoram'),
		('IN-NL', 'Nagaland'),
		('IN-OR', 'Odisha'),
		('IN-PB', 'Punjab'),
		('IN-RJ', 'Rajasthan'),
		('IN-SK', 'Sikkim'),
		('IN-TN', 'Tamil Nadu'),
		('IN-TG', 'Telangana'),
		('IN-TR', 'Tripura'),
		('IN-UT', 'Uttarakhand'),
		('IN-UP', 'Uttar Pradesh'),
		('IN-WB', 'West Bengal'),
		('IN-AN', 'Andaman and Nicobar Islands'),
		('IN-CH', 'Chandigarh'),
		('IN-DN', 'Dadra and Nagar Haveli'),
		('IN-DD', 'Daman and Diu'),
		('IN-DL', 'Delhi'),
		('IN-LD', 'Lakshadweep'),
		('IN-PY', 'Puducherry'),
		('OTHER', 'State outside India'),
	)

	COUNTRIES = (
		('IND', 'India'),
		('AFG', 'Afghanistan'),
		('ALA', 'Åland Islands'),
		('ALB', 'Albania'),
		('DZA', 'Algeria'),
		('ASM', 'American Samoa'),
		('AND', 'Andorra'),
		('AGO', 'Angola'),
		('AIA', 'Anguilla'),
		('ATA', 'Antarctica'),
		('ATG', 'Antigua and Barbuda'),
		('ARG', 'Argentina'),
		('ARM', 'Armenia'),
		('ABW', 'Aruba'),
		('AUS', 'Australia'),
		('AUT', 'Austria'),
		('AZE', 'Azerbaijan'),
		('BHS', 'Bahamas'),
		('BHR', 'Bahrain'),
		('BGD', 'Bangladesh'),
		('BRB', 'Barbados'),
		('BLR', 'Belarus'),
		('BEL', 'Belgium'),
		('BLZ', 'Belize'),
		('BEN', 'Benin'),
		('BMU', 'Bermuda'),
		('BTN', 'Bhutan'),
		('BOL', 'Bolivia (Plurinational State of)'),
		('BES', 'Bonaire, Sint Eustatius and Saba'),
		('BIH', 'Bosnia and Herzegovina'),
		('BWA', 'Botswana'),
		('BVT', 'Bouvet Island'),
		('BRA', 'Brazil'),
		('IOT', 'British Indian Ocean Territory'),
		('BRN', 'Brunei Darussalam'),
		('BGR', 'Bulgaria'),
		('BFA', 'Burkina Faso'),
		('BDI', 'Burundi'),
		('CPV', 'Cabo Verde'),
		('KHM', 'Cambodia'),
		('CMR', 'Cameroon'),
		('CAN', 'Canada'),
		('CYM', 'Cayman Islands'),
		('CAF', 'Central African Republic'),
		('TCD', 'Chad'),
		('CHL', 'Chile'),
		('CHN', 'China'),
		('CXR', 'Christmas Island'),
		('CCK', 'Cocos (Keeling) Islands'),
		('COL', 'Colombia'),
		('COM', 'Comoros'),
		('COG', 'Congo'),
		('COD', 'Congo (Democratic Republic of the)'),
		('COK', 'Cook Islands'),
		('CRI', 'Costa Rica'),
		('CIV', 'Côte d\'Ivoire'),
		('HRV', 'Croatia'),
		('CUB', 'Cuba'),
		('CUW', 'Curaçao'),
		('CYP', 'Cyprus'),
		('CZE', 'Czech Republic'),
		('DNK', 'Denmark'),
		('DJI', 'Djibouti'),
		('DMA', 'Dominica'),
		('DOM', 'Dominican Republic'),
		('ECU', 'Ecuador'),
		('EGY', 'Egypt'),
		('SLV', 'El Salvador'),
		('GNQ', 'Equatorial Guinea'),
		('ERI', 'Eritrea'),
		('EST', 'Estonia'),
		('ETH', 'Ethiopia'),
		('FLK', 'Falkland Islands (Malvinas)'),
		('FRO', 'Faroe Islands'),
		('FJI', 'Fiji'),
		('FIN', 'Finland'),
		('FRA', 'France'),
		('GUF', 'French Guiana'),
		('PYF', 'French Polynesia'),
		('ATF', 'French Southern Territories'),
		('GAB', 'Gabon'),
		('GMB', 'Gambia'),
		('GEO', 'Georgia'),
		('DEU', 'Germany'),
		('GHA', 'Ghana'),
		('GIB', 'Gibraltar'),
		('GRC', 'Greece'),
		('GRL', 'Greenland'),
		('GRD', 'Grenada'),
		('GLP', 'Guadeloupe'),
		('GUM', 'Guam'),
		('GTM', 'Guatemala'),
		('GGY', 'Guernsey'),
		('GIN', 'Guinea'),
		('GNB', 'Guinea-Bissau'),
		('GUY', 'Guyana'),
		('HTI', 'Haiti'),
		('HMD', 'Heard Island and McDonald Islands'),
		('VAT', 'Holy See'),
		('HND', 'Honduras'),
		('HKG', 'Hong Kong'),
		('HUN', 'Hungary'),
		('ISL', 'Iceland'),
		('IDN', 'Indonesia'),
		('IRN', 'Iran (Islamic Republic of)'),
		('IRQ', 'Iraq'),
		('IRL', 'Ireland'),
		('IMN', 'Isle of Man'),
		('ISR', 'Israel'),
		('ITA', 'Italy'),
		('JAM', 'Jamaica'),
		('JPN', 'Japan'),
		('JEY', 'Jersey'),
		('JOR', 'Jordan'),
		('KAZ', 'Kazakhstan'),
		('KEN', 'Kenya'),
		('KIR', 'Kiribati'),
		('PRK', 'Korea (Democratic People\'s Republic of)'),
		('KOR', 'Korea (Republic of)'),
		('KWT', 'Kuwait'),
		('KGZ', 'Kyrgyzstan'),
		('LAO', 'Lao People\'s Democratic Republic'),
		('LVA', 'Latvia'),
		('LBN', 'Lebanon'),
		('LSO', 'Lesotho'),
		('LBR', 'Liberia'),
		('LBY', 'Libya'),
		('LIE', 'Liechtenstein'),
		('LTU', 'Lithuania'),
		('LUX', 'Luxembourg'),
		('MAC', 'Macao'),
		('MKD', 'Macedonia (the former Yugoslav Republic of)'),
		('MDG', 'Madagascar'),
		('MWI', 'Malawi'),
		('MYS', 'Malaysia'),
		('MDV', 'Maldives'),
		('MLI', 'Mali'),
		('MLT', 'Malta'),
		('MHL', 'Marshall Islands'),
		('MTQ', 'Martinique'),
		('MRT', 'Mauritania'),
		('MUS', 'Mauritius'),
		('MYT', 'Mayotte'),
		('MEX', 'Mexico'),
		('FSM', 'Micronesia (Federated States of)'),
		('MDA', 'Moldova (Republic of)'),
		('MCO', 'Monaco'),
		('MNG', 'Mongolia'),
		('MNE', 'Montenegro'),
		('MSR', 'Montserrat'),
		('MAR', 'Morocco'),
		('MOZ', 'Mozambique'),
		('MMR', 'Myanmar'),
		('NAM', 'Namibia'),
		('NRU', 'Nauru'),
		('NPL', 'Nepal'),
		('NLD', 'Netherlands'),
		('NCL', 'New Caledonia'),
		('NZL', 'New Zealand'),
		('NIC', 'Nicaragua'),
		('NER', 'Niger'),
		('NGA', 'Nigeria'),
		('NIU', 'Niue'),
		('NFK', 'Norfolk Island'),
		('MNP', 'Northern Mariana Islands'),
		('NOR', 'Norway'),
		('OMN', 'Oman'),
		('PAK', 'Pakistan'),
		('PLW', 'Palau'),
		('PSE', 'Palestine, State of'),
		('PAN', 'Panama'),
		('PNG', 'Papua New Guinea'),
		('PRY', 'Paraguay'),
		('PER', 'Peru'),
		('PHL', 'Philippines'),
		('PCN', 'Pitcairn'),
		('POL', 'Poland'),
		('PRT', 'Portugal'),
		('PRI', 'Puerto Rico'),
		('QAT', 'Qatar'),
		('REU', 'Réunion'),
		('ROU', 'Romania'),
		('RUS', 'Russian Federation'),
		('RWA', 'Rwanda'),
		('BLM', 'Saint Barthélemy'),
		('SHN', 'Saint Helena, Ascension and Tristan da Cunha'),
		('KNA', 'Saint Kitts and Nevis'),
		('LCA', 'Saint Lucia'),
		('MAF', 'Saint Martin (French part)'),
		('SPM', 'Saint Pierre and Miquelon'),
		('VCT', 'Saint Vincent and the Grenadines'),
		('WSM', 'Samoa'),
		('SMR', 'San Marino'),
		('STP', 'Sao Tome and Principe'),
		('SAU', 'Saudi Arabia'),
		('SEN', 'Senegal'),
		('SRB', 'Serbia'),
		('SYC', 'Seychelles'),
		('SLE', 'Sierra Leone'),
		('SGP', 'Singapore'),
		('SXM', 'Sint Maarten (Dutch part)'),
		('SVK', 'Slovakia'),
		('SVN', 'Slovenia'),
		('SLB', 'Solomon Islands'),
		('SOM', 'Somalia'),
		('ZAF', 'South Africa'),
		('SGS', 'South Georgia and the South Sandwich Islands'),
		('SSD', 'South Sudan'),
		('ESP', 'Spain'),
		('LKA', 'Sri Lanka'),
		('SDN', 'Sudan'),
		('SUR', 'Suriname'),
		('SJM', 'Svalbard and Jan Mayen'),
		('SWZ', 'Swaziland'),
		('SWE', 'Sweden'),
		('CHE', 'Switzerland'),
		('SYR', 'Syrian Arab Republic'),
		('TWN', 'Taiwan, Province of China[a]'),
		('TJK', 'Tajikistan'),
		('TZA', 'Tanzania, United Republic of'),
		('THA', 'Thailand'),
		('TLS', 'Timor-Leste'),
		('TGO', 'Togo'),
		('TKL', 'Tokelau'),
		('TON', 'Tonga'),
		('TTO', 'Trinidad and Tobago'),
		('TUN', 'Tunisia'),
		('TUR', 'Turkey'),
		('TKM', 'Turkmenistan'),
		('TCA', 'Turks and Caicos Islands'),
		('TUV', 'Tuvalu'),
		('UGA', 'Uganda'),
		('UKR', 'Ukraine'),
		('ARE', 'United Arab Emirates'),
		('GBR', 'United Kingdom of Great Britain and Northern Ireland'),
		('USA', 'United States of America'),
		('UMI', 'United States Minor Outlying Islands'),
		('URY', 'Uruguay'),
		('UZB', 'Uzbekistan'),
		('VUT', 'Vanuatu'),
		('VEN', 'Venezuela (Bolivarian Republic of)'),
		('VNM', 'Viet Nam'),
		('VGB', 'Virgin Islands (British)'),
		('VIR', 'Virgin Islands (U.S.)'),
		('WLF', 'Wallis and Futuna'),
		('ESH', 'Western Sahara'),
		('YEM', 'Yemen'),
		('ZMB', 'Zambia'),
		('ZWE', 'Zimbabwe'),
	)


	Line1 = models.CharField(max_length=30, blank=False, null=False,
							 verbose_name="Address: Line 1", help_text="Mandatory",)
	Line2 = models.CharField(max_length=30, blank=False, null=False,
							 verbose_name="Address: Line 2", help_text="Mandatory",)
	State = models.CharField(max_length=5, null=False, blank=False,
							 choices=STATES_IN_INDIA, verbose_name="State", help_text="Mandatory", default="IN-GA")
	PIN = models.CharField(max_length=6, null=False, blank=False, verbose_name="PIN Code", help_text="Mandatory")
	COUNTRY = models.CharField(max_length=3, null=False, blank=False,
							   choices=COUNTRIES, verbose_name="Country", help_text="Mandatory", default="IND")
	client = models.ForeignKey(Client, on_delete=models.CASCADE)