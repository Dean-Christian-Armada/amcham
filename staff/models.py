from django.db import models

# Create your models here.

class Country(models.Model):
	country = models.CharField(max_length=50, null=True, unique=True)

	def __str__(self):
		return self.country

class Postal_Code(models.Model):
	postal_code = models.IntegerField(null=True, unique=True)

	def __str__(self):
		if self.postal_code == None:
			return ''
		else:
			return str(self.postal_code)

class Website(models.Model):
	website = models.CharField(max_length=50, null=True, unique=True)

	def __str__(self):
		return self.website

# class Company_Description(models.Model):
# 	description = models.CharField(max_length=255, null=True)

class State(models.Model):
	state = models.CharField(max_length=50, null=True, unique=True)

	def __str__(self):
		return self.state

class Company(models.Model):
	name = models.CharField(max_length=50, null=True)
	# country = models.CharField(max_length=50, null=True)
	# postal_code = models.CharField(max_length=50, null=True)
	# website = models.CharField(max_length=50, null=True)
	# state = models.CharField(max_length=50, null=True)
	country = models.ForeignKey('country')
	postal_code = models.ForeignKey('postal_code')
	website = models.ForeignKey('website')
	state = models.ForeignKey('state')

	def __str__(self):
		return self.name

	# def clean(self):
	# 	if type(self.country) != int:
	# 		country = Country.objects.get(country=self.country)
	# 		self.country = country.id
	# 	if type(self.postal_code) != int:
	# 		postal_code = Postal_Code.objects.get(postal_code=self.postal_code)
	# 		self.postal_code = postal_code.id
	# 	if type(self.website) != int:
	# 		website = Website.objects.get(website=self.website)
	# 		self.website = website.id
	# 	if type(self.state) != int:
	# 		state = State.objects.get(state=self.state)
	# 		self.state = state.id
