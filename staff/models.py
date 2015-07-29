from django.db import models
import re
# Create your models here.

class AltRepresentative(models.Model):
	first_name = models.CharField(max_length=50, default=None)
	last_name = models.CharField(max_length=50, default=None)
	full_name = models.CharField(max_length=100, default=None)
	telephone = models.CharField(max_length=50, default=None, blank=True, null=True)
	mobile = models.CharField(max_length=50, default=None, blank=True, null=True)
	email = models.CharField(max_length=50, default=None, blank=True, null=True)

	def save(self, *args, **kwargs):
		# if self.date_added != None:
		# 	self.date_modified = datetime.datetime.today()
		self.full_name = self.first_name+' '+self.last_name
		super(AltRepresentative, self).save(*args, **kwargs)

	def __str__(self):
		name = "%s %s" % (self.first_name, self.last_name)
		return name

class ExecRepresentative(models.Model):
	first_name = models.CharField(max_length=50, default=None)
	last_name = models.CharField(max_length=50, default=None)
	full_name = models.CharField(max_length=100, default=None)
	telephone = models.CharField(max_length=50, default=None, blank=True, null=True)
	mobile = models.CharField(max_length=50, default=None, blank=True, null=True)
	email = models.CharField(max_length=50, default=None, blank=True, null=True)

	def save(self, *args, **kwargs):
		# if self.date_added != None:
		# 	self.date_modified = datetime.datetime.today()
		self.full_name = self.first_name+' '+self.last_name
		super(ExecRepresentative, self).save(*args, **kwargs)

	def __str__(self):
		name = "%s %s" % (self.first_name, self.last_name)
		return name

class BloodType(models.Model):
	blood_type = models.CharField(max_length=5, default=None, unique=True)

	def __str__(self):
		return self.blood_type

class City(models.Model):
	city = models.CharField(max_length=50, default=None, unique=True)

	def __str__(self):
		return self.city.encode('ascii', errors='replace')

class Country(models.Model):
	country = models.CharField(max_length=50, default=None, unique=True)

	def __str__(self):
		return self.country

class Email(models.Model):
	email = models.CharField(max_length=100, default=None, unique=True)

	def __str__(self):
		return self.email.encode('ascii', errors='replace')

class Gender(models.Model):
	gender = models.CharField(max_length=50, default=None, null=True, blank=True, unique=True)

	def __str__(self):
		return self.gender

class MembershipDate(models.Model):
	membership_date = models.DateField(unique=True)

class Nationality(models.Model):
	nationality = models.CharField(max_length=50, default=None, unique=True)

	def __str__(self):
		return self.nationality

class Position(models.Model):
	position = models.CharField(max_length=100, default=None, unique=True)

	def __str__(self):
		return self.position.encode('ascii', errors='replace')

class PostalCode(models.Model):
	postal_code = models.CharField(max_length=50, default=None, unique=True)

	def __str__(self):
		return self.postal_code.encode('ascii', errors='replace')

class ReferredBy(models.Model):
	referred_by = models.CharField(max_length=50, default=None, unique=True)

	def __str__(self):
		return self.referred_by

class State(models.Model):
	state = models.CharField(max_length=50, default=None, unique=True)

	def __str__(self):
		return self.state

class Suffix(models.Model):
	suffix = models.CharField(max_length=50, default=None, unique=True)

	def __str__(self):
		return self.suffix

# class USAddress(models.Model):
# 	us_address = models.CharField(max_length=50, default=None, unique=True)

class Company(models.Model):
	company = models.CharField(max_length=100, default=None, unique=True)
	description = models.TextField(null=True, blank=True)
	website = models.CharField(max_length=50, null=True, blank=True, default=None)
	street_1 = models.CharField(max_length=100, null=True, blank=True, default=None)
	street_2 = models.CharField(max_length=100, null=True, blank=True, default=None)
	city = models.ForeignKey('City', default=None)
	country = models.ForeignKey('Country', default=1)
	postal_code = models.ForeignKey('PostalCode', default=None)
	state = models.ForeignKey('State', default=2)
	nationality = models.ForeignKey('Nationality', default=1)
	us_address_1 = models.CharField(max_length=100, null=True, blank=True, default=None)
	us_address_2 = models.CharField(max_length=100, null=True, blank=True, default=None)
	us_city = models.ForeignKey('City', related_name='us_city', default=None)
	us_zip = models.ForeignKey('PostalCode', related_name='us_zip', default=None)
	us_state = models.ForeignKey('State', related_name='us_state', default=None)
	tin = models.CharField(max_length=50, null=True, blank=True, default=None)
	annual_revenue = models.CharField(max_length=50, null=True, blank=True, default=None)

	def __str__(self):
		return self.company.encode('ascii', errors='replace')


class Member(models.Model):
	first_name = models.CharField(max_length=50, default=None)
	middle_name = models.CharField(max_length=50, default=None)
	last_name = models.CharField(max_length=50, default=None)
	company = models.ForeignKey('Company', default=None)
	position = models.ForeignKey('Position', default=None)
	personal_email = models.ForeignKey('Email', default=None)
	company_email = models.ForeignKey('Email', default=None, related_name='company_email')
	telephone = models.CharField(max_length=50, default=None)
	fax = models.CharField(max_length=50, default=None)
	mobile = models.CharField(max_length=50, default=None)
	citizenship = models.ForeignKey('Nationality', default=1)
	birthday = models.DateField(null=True, blank=True, default=None)
	gender = models.ForeignKey('Gender', default=1)
	blood_type = models.ForeignKey('BloodType', default=None)
	suffix = models.ForeignKey('Suffix', default=None)

	def __str__(self):
		first_name = self.first_name
		middle_name = self.middle_name
		last_name = self.last_name
		full_name = "%s %s %s" % (first_name, middle_name, last_name)
		if full_name == '  ':
			full_name = '-'
		return full_name

	def full_name(self):
		first_name = self.first_name
		middle_name = self.middle_name
		last_name = self.last_name
		full_name = "%s %s %s" % (first_name, middle_name, last_name)
		if full_name == '  ':
			full_name = '-'
		return full_name
	full_name.short_description = 'Full Name'