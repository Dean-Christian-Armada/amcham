from django.db import models
import re
# Create your models here.

class Company(models.Model):
	name = models.CharField(max_length=50, null=True, blank=True)
	description = models.TextField(max_length=50, null=True, blank=True)
	website = models.CharField(max_length=50, null=True, blank=True)
	email = models.CharField(max_length=50, null=True, blank=True)
	phone = models.CharField(max_length=50, null=True, blank=True)
	fax = models.CharField(max_length=50, null=True, blank=True)
	mobile = models.CharField(max_length=50, null=True, blank=True)
	street_1 = models.CharField(max_length=100, null=True, blank=True)
	street_2 = models.CharField(max_length=100, null=True, blank=True)
	city = models.CharField(max_length=50, null=True, blank=True)
	country = models.CharField(max_length=50, null=True, blank=True)
	postal_code = models.CharField(max_length=50, null=True, blank=True)
	state = models.CharField(max_length=50, null=True, blank=True)
	US_address_1 = models.CharField(max_length=100, null=True, blank=True)
	US_address_2 = models.CharField(max_length=100, null=True, blank=True)
	US_city = models.CharField(max_length=50, null=True, blank=True)
	US_zip = models.CharField(max_length=50, null=True, blank=True)
	US_state = models.CharField(max_length=50, null=True, blank=True)
	nationality = models.CharField(max_length=50, null=True, blank=True)
	tin = models.CharField(max_length=50, null=True, blank=True)
	annual_revenue = models.CharField(max_length=50, null=True, blank=True)

	def __str__(self):
		# return str(self.id)
		return self.name

class AltRepresentative(models.Model):
	first_name = models.CharField(max_length=50, null=True, blank=True)
	# middle_name = models.CharField(max_length=50, null=True, blank=True)
	last_name = models.CharField(max_length=50, null=True, blank=True)
	telephone = models.CharField(max_length=50, null=True, blank=True)
	mobile = models.CharField(max_length=50, null=True, blank=True)
	email = models.CharField(max_length=50, null=True, blank=True)

	def __str__(self):
		# return str(self.id)
		return "%s %s" % (self.first_name, self.last_name)

class ExecRepresentative(models.Model):
	first_name = models.CharField(max_length=50, null=True, blank=True)
	# middle_name = models.CharField(max_length=50, null=True, blank=True)
	last_name = models.CharField(max_length=50, null=True, blank=True)
	telephone = models.CharField(max_length=50, null=True, blank=True)
	mobile = models.CharField(max_length=50, null=True, blank=True)
	email = models.CharField(max_length=50, null=True, blank=True)

	def __str__(self):
		# return str(self.id)
		return "%s %s" % (self.first_name, self.last_name)

class Member(models.Model):
	first_name = models.CharField(max_length=50, null=True, blank=True)
	middle_name = models.CharField(max_length=50, null=True, blank=True)
	last_name = models.CharField(max_length=50, null=True, blank=True)
	membership_date = models.DateField(null=True, blank=True)
	position = models.CharField(max_length=50, null=True, blank=True)
	email = models.CharField(max_length=50, null=True, blank=True)
	mobile = models.CharField(max_length=50, null=True, blank=True)
	country = models.CharField(max_length=50, null=True, blank=True)
	street_1 = models.CharField(max_length=100, null=True, blank=True)
	street_2 = models.CharField(max_length=100, null=True, blank=True)
	city = models.CharField(max_length=100, null=True, blank=True)
	postal_code = models.CharField(max_length=100, null=True, blank=True)
	state = models.CharField(max_length=50, null=True, blank=True)
	citizenship = models.CharField(max_length=50, null=True, blank=True)
	birthday = models.DateField(null=True, blank=True)
	gender = models.CharField(max_length=50, null=True, blank=True)
	blood_type = models.CharField(max_length=50, null=True, blank=True)
	suffix = models.CharField(max_length=50, null=True, blank=True)
	referred_by = models.CharField(max_length=50, null=True, blank=True)
	company = models.ForeignKey('Company', default=None)
	alt_representative = models.ForeignKey('AltRepresentative', default=None)
	exec_representative = models.ForeignKey('ExecRepresentative', default=None)

	def __str__(self):
		# return str(self.id)
		return "%s %s %s" % (self.first_name, self.middle_name, self.last_name)

	def name(self):
		return "%s %s %s" % (self.first_name, self.middle_name, self.last_name)