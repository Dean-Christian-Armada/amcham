
# Company and Personal Duplicate Fields from Excel

class State(models.Model):
	state = models.CharField(max_length=50, null=True, unique=True, blank=True)

	def __str__(self):
		return self.state

class Country(models.Model):
	country = models.CharField(max_length=50, null=True, unique=True, blank=True)

	def __str__(self):
		return self.country

class City(models.Model):
	city = models.CharField(max_length=50, null=True, unique=True, blank=True)

class Postal_Code(models.Model):
	postal_code = models.IntegerField(null=True, unique=True, blank=True)

	def __str__(self):
		if self.postal_code == None:
			return ''
		else:
			return str(self.postal_code)

class Email(models.Model):
	email = models.CharField(max_length=100, unique=True, null=True, blank=True)

class Mobile(models.Model):
	mobile = models.CharField(max_length=50, null=True, unique=True, blank=True)

# Company and Personal Duplicate Fields from Excel



# Company Fields

# class Phone(models.Model):
# 	phone = models.CharField(max_length=50, null=True, blank=True)

class Website(models.Model):
	website = models.URLField(null=True, unique=True, blank=True)

	def __str__(self):
		website = self.website
		# regex = re.search('(.)*[w]{3}.', website)
		# if regex:
		# 	regex = regex.group()
		# 	website = website.replace(regex, '')
		# website = website.replace('http://', '')
		return website

class Fax(models.Model):
	fax = models.CharField(max_length=50, null=True, blank=True)

class Tin(models.Model):
	tin = models.CharField(max_length=50, null=True, blank=True)

class USCity(models.Model):
	us_city = models.CharField(max_length=50, null=True, blank=True)

class USZip(models.Model):
	us_zip = models.CharField(max_length=50, null=True, blank=True)

class USState(models.Mobiledel):
	us_state = models.CharField(max_length=50, null=True, blank=True)

class Nationality(models.Model):
	nationality = models.CharField(max_length=50, null=True, blank=True)

class Company(models.Model):
	name = models.CharField(max_length=50, null=True)
	description = models.TextField(null=True, blank=True)
	membership_date = models.DateField(default=None)
	street_1 = models.CharField(max_length=200, null=True, blank=True)
	street_2 = models.CharField(max_length=200, null=True, blank=True)
	state = models.ForeignKey('State')
	country = models.ForeignKey('Country', default=None)
	city = models.ForeignKey('City', default=None)
	postal_code = models.ForeignKey('Postal_Code', default=None)
	# email = models.ForeignKey('Email', default=None) Transferred to personal and not FK
	# mobile = models.ForeignKey('Mobile', default=None) Transferred to personal
	# phone = models.ForeignKey('Phone', default=None) Transferred to personal
	website = models.ForeignKey('Website', default=None)
	fax = models.ForeignKey('Fax', default=None)
	tin = models.ForeignKey('Tin', default=None)
	USCity = models.ForeignKey('USCity', default=None)
	USZip = models.ForeignKey('USZip', default=None)
	USState = models.ForeignKey('USState', default=None)
	Nationality = models.ForeignKey('Nationality', default=None)

	def __str__(self):
		return self.name

# Company Fields