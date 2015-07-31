from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from import_export import resources, widgets
from import_export.admin import ImportExportModelAdmin, ImportExportActionModelAdmin, DEFAULT_FORMATS
from import_export.formats import base_formats
from import_export import fields
from . models import *
import calendar
# Register your models here.

class MemberInline(admin.TabularInline):
	model = Member
	# fk_name = 'Company'



class CompanyAdmin(admin.ModelAdmin):
	inlines = [
		MemberInline
	]

class Variables(object):
	AppObject = Member.objects

class CompanyFilter(admin.SimpleListFilter, Variables):
	title = _('Company')
	parameter_name = 'company'

	def lookups(self, request, model_admin):
		position = request.GET.get('position')
		company = request.GET.get('company')
		citizenship = request.GET.get('citizenship')
		company = request.GET.get('company')
		gender = request.GET.get('gender')
		blood_type = request.GET.get('blood_type')
		suffix = request.GET.get('suffix')
		city = request.GET.get('city')
		country = request.GET.get('country')
		state = request.GET.get('state')
		postal_code = request.GET.get('postal_code')
		nationality = request.GET.get('nationality')
		birthday = request.GET.get('birthday')
		membership_date = request.GET.get('membership_date')

		app = Variables.AppObject

		if position or position == '':
			app = app.filter(position__position__exact=position)
		if citizenship or citizenship == '':
			app = app.filter(citizenship__nationality__exact=citizenship)
		if gender or gender == '':
			app = app.filter(gender__gender__exact=gender)
		if blood_type or blood_type == '':
			app = app.filter(blood_type__blood_type__exact=blood_type)
		if suffix or suffix == '':
			app = app.filter(suffix__suffix__exact=suffix)
		if city or city == '':
			app = app.filter(company__city__city__exact=city)
		if country or country == '':
			app = app.filter(company__country__country__exact=country)
		if state or state == '':
			app = app.filter(company__state__state__exact=state)
		if postal_code or postal_code == '':
			app = app.filter(company__postal_code__postal_code__exact=postal_code)
		if nationality or nationality == '':
			app = app.filter(company__nationality__nationality__exact=nationality)
		if birthday or birthday == '':
			app = app.filter(birthday__month=birthday)
		if membership_date or membership_date == '':
			app = app.filter(membership_date__year=membership_date)			
		else:
			pass

		distinct = app.distinct().order_by('company__company')
		return distinct.values_list('company__company', 'company__company')


	def queryset(self, request, queryset):
		param = self.value()
		if param or param == '':
			return queryset.filter(company__company=param)

class PositionFilter(admin.SimpleListFilter, Variables):
	title = _('Position')
	parameter_name = 'position'

	def lookups(self, request, model_admin):
		position = request.GET.get('position')
		citizenship = request.GET.get('citizenship')
		company = request.GET.get('company')
		gender = request.GET.get('gender')
		blood_type = request.GET.get('blood_type')
		suffix = request.GET.get('suffix')
		city = request.GET.get('city')
		country = request.GET.get('country')
		state = request.GET.get('state')
		postal_code = request.GET.get('postal_code')
		nationality = request.GET.get('nationality')
		birthday = request.GET.get('birthday')
		membership_date = request.GET.get('membership_date')

		app = Variables.AppObject

		if citizenship or citizenship == '':
			app = app.filter(citizenship__nationality__exact=citizenship)
		if company or company == '':
			app = app.filter(company__company__exact=company)
		if gender or gender == '':
			app = app.filter(gender__gender__exact=gender)
		if blood_type or blood_type == '':
			app = app.filter(blood_type__blood_type__exact=blood_type)
		if suffix or suffix == '':
			app = app.filter(suffix__suffix__exact=suffix)
		if city or city == '':
			app = app.filter(company__city__city__exact=city)
		if country or country == '':
			app = app.filter(company__country__country__exact=country)
		if state or state == '':
			app = app.filter(company__state__state__exact=state)
		if postal_code or postal_code == '':
			app = app.filter(company__postal_code__postal_code__exact=postal_code)
		if nationality or nationality == '':
			app = app.filter(company__nationality__nationality__exact=nationality)
		if birthday or birthday == '':
			app = app.filter(birthday__month=birthday)
		if membership_date or membership_date == '':
			app = app.filter(membership_date__year=membership_date)			
		else:
			pass

		distinct = app.distinct().order_by('position__position')
		return distinct.values_list('position__position', 'position__position')


	def queryset(self, request, queryset):
		param = self.value()
		if param or param == '':
			return queryset.filter(position__position=param)

class CitizenshipFilter(admin.SimpleListFilter, Variables):
	title = _('Citizenship')
	parameter_name = 'citizenship'

	def lookups(self, request, model_admin):
		position = request.GET.get('position')
		company = request.GET.get('company')
		gender = request.GET.get('gender')
		blood_type = request.GET.get('blood_type')
		suffix = request.GET.get('suffix')
		city = request.GET.get('city')
		country = request.GET.get('country')
		state = request.GET.get('state')
		postal_code = request.GET.get('postal_code')
		nationality = request.GET.get('nationality')
		birthday = request.GET.get('birthday')
		membership_date = request.GET.get('membership_date')

		app = Variables.AppObject

		if position or position == '':
			app = app.filter(position__position__exact=position)
		if company or company == '':
			app = app.filter(company__company__exact=company)
		if gender or gender == '':
			app = app.filter(gender__gender__exact=gender)
		if blood_type or blood_type == '':
			app = app.filter(blood_type__blood_type__exact=blood_type)
		if suffix or suffix == '':
			app = app.filter(suffix__suffix__exact=suffix)
		if city or city == '':
			app = app.filter(company__city__city__exact=city)
		if country or country == '':
			app = app.filter(company__country__country__exact=country)
		if state or state == '':
			app = app.filter(company__state__state__exact=state)
		if postal_code or postal_code == '':
			app = app.filter(company__postal_code__postal_code__exact=postal_code)
		if nationality or nationality == '':
			app = app.filter(company__nationality__nationality__exact=nationality)
		if birthday or birthday == '':
			app = app.filter(birthday__month=birthday)
		if membership_date or membership_date == '':
			app = app.filter(membership_date__year=membership_date)			
		else:
			pass

		distinct = app.distinct().order_by('citizenship__nationality')
		return distinct.values_list('citizenship__nationality', 'citizenship__nationality')


	def queryset(self, request, queryset):
		param = self.value()
		if param or param == '':
			return queryset.filter(citizenship__nationality=param)

class GenderFilter(admin.SimpleListFilter, Variables):
	title = _('Gender')
	parameter_name = 'gender'

	def lookups(self, request, model_admin):
		position = request.GET.get('position')
		citizenship = request.GET.get('citizenship')
		company = request.GET.get('company')
		blood_type = request.GET.get('blood_type')
		suffix = request.GET.get('suffix')
		city = request.GET.get('city')
		country = request.GET.get('country')
		state = request.GET.get('state')
		postal_code = request.GET.get('postal_code')
		nationality = request.GET.get('nationality')
		birthday = request.GET.get('birthday')
		membership_date = request.GET.get('membership_date')

		app = Variables.AppObject

		if position or position == '':
			app = app.filter(position__position__exact=position)
		if citizenship or citizenship == '':
			app = app.filter(citizenship__nationality__exact=citizenship)
		if company or company == '':
			app = app.filter(company__company__exact=company)
		if blood_type or blood_type == '':
			app = app.filter(blood_type__blood_type__exact=blood_type)
		if suffix or suffix == '':
			app = app.filter(suffix__suffix__exact=suffix)
		if city or city == '':
			app = app.filter(company__city__city__exact=city)
		if country or country == '':
			app = app.filter(company__country__country__exact=country)
		if state or state == '':
			app = app.filter(company__state__state__exact=state)
		if postal_code or postal_code == '':
			app = app.filter(company__postal_code__postal_code__exact=postal_code)
		if nationality or nationality == '':
			app = app.filter(company__nationality__nationality__exact=nationality)
		if birthday or birthday == '':
			app = app.filter(birthday__month=birthday)
		if membership_date or membership_date == '':
			app = app.filter(membership_date__year=membership_date)			
		else:
			pass

		distinct = app.distinct().order_by('gender__gender')
		return distinct.values_list('gender__gender', 'gender__gender')


	def queryset(self, request, queryset):
		param = self.value()
		if param or param == '':
			return queryset.filter(gender__gender=param)

class BloodTypeFilter(admin.SimpleListFilter, Variables):
	title = _('Blood Type')
	parameter_name = 'blood_type'

	def lookups(self, request, model_admin):
		position = request.GET.get('position')
		citizenship = request.GET.get('citizenship')
		company = request.GET.get('company')
		gender = request.GET.get('gender')
		suffix = request.GET.get('suffix')
		city = request.GET.get('city')
		country = request.GET.get('country')
		state = request.GET.get('state')
		postal_code = request.GET.get('postal_code')
		nationality = request.GET.get('nationality')
		birthday = request.GET.get('birthday')
		membership_date = request.GET.get('membership_date')

		app = Variables.AppObject

		if position or position == '':
			app = app.filter(position__position__exact=position)
		if citizenship or citizenship == '':
			app = app.filter(citizenship__nationality__exact=citizenship)
		if company or company == '':
			app = app.filter(company__company__exact=company)
		if gender or gender == '':
			app = app.filter(gender__gender__exact=gender)
		if suffix or suffix == '':
			app = app.filter(suffix__suffix__exact=suffix)
		if city or city == '':
			app = app.filter(company__city__city__exact=city)
		if country or country == '':
			app = app.filter(company__country__country__exact=country)
		if state or state == '':
			app = app.filter(company__state__state__exact=state)
		if postal_code or postal_code == '':
			app = app.filter(company__postal_code__postal_code__exact=postal_code)
		if nationality or nationality == '':
			app = app.filter(company__nationality__nationality__exact=nationality)
		if birthday or birthday == '':
			app = app.filter(birthday__month=birthday)
		if membership_date or membership_date == '':
			app = app.filter(membership_date__year=membership_date)			
		else:
			pass

		distinct = app.distinct().order_by('blood_type__blood_type')
		return distinct.values_list('blood_type__blood_type', 'blood_type__blood_type')


	def queryset(self, request, queryset):
		param = self.value()
		if param or param == '':
			return queryset.filter(blood_type__blood_type=param)

class SuffixFilter(admin.SimpleListFilter, Variables):
	title = _('Suffix')
	parameter_name = 'suffix'

	def lookups(self, request, model_admin):
		position = request.GET.get('position')
		citizenship = request.GET.get('citizenship')
		company = request.GET.get('company')
		gender = request.GET.get('gender')
		blood_type = request.GET.get('blood_type')
		city = request.GET.get('city')
		country = request.GET.get('country')
		state = request.GET.get('state')
		postal_code = request.GET.get('postal_code')
		nationality = request.GET.get('nationality')
		birthday = request.GET.get('birthday')
		membership_date = request.GET.get('membership_date')

		app = Variables.AppObject

		if position or position == '':
			app = app.filter(position__position__exact=position)
		if citizenship or citizenship == '':
			app = app.filter(citizenship__nationality__exact=citizenship)
		if company or company == '':
			app = app.filter(company__company__exact=company)
		if gender or gender == '':
			app = app.filter(gender__gender__exact=gender)
		if blood_type or blood_type == '':
			app = app.filter(blood_type__blood_type__exact=blood_type)
		if city or city == '':
			app = app.filter(company__city__city__exact=city)
		if country or country == '':
			app = app.filter(company__country__country__exact=country)
		if state or state == '':
			app = app.filter(company__state__state__exact=state)
		if postal_code or postal_code == '':
			app = app.filter(company__postal_code__postal_code__exact=postal_code)
		if nationality or nationality == '':
			app = app.filter(company__nationality__nationality__exact=nationality)
		if birthday or birthday == '':
			app = app.filter(birthday__month=birthday)
		if membership_date or membership_date == '':
			app = app.filter(membership_date__year=membership_date)			
		else:
			pass

		distinct = app.distinct().order_by('suffix__suffix')
		return distinct.values_list('suffix__suffix', 'suffix__suffix')


	def queryset(self, request, queryset):
		param = self.value()
		if param or param == '':
			return queryset.filter(suffix__suffix=param)

class CityFilter(admin.SimpleListFilter, Variables):
	title = _('City')
	parameter_name = 'city'

	def lookups(self, request, model_admin):
		position = request.GET.get('position')
		citizenship = request.GET.get('citizenship')
		company = request.GET.get('company')
		gender = request.GET.get('gender')
		blood_type = request.GET.get('blood_type')
		suffix = request.GET.get('suffix')
		country = request.GET.get('country')
		state = request.GET.get('state')
		postal_code = request.GET.get('postal_code')
		nationality = request.GET.get('nationality')
		birthday = request.GET.get('birthday')
		membership_date = request.GET.get('membership_date')

		app = Variables.AppObject

		if position or position == '':
			app = app.filter(position__position__exact=position)
		if citizenship or citizenship == '':
			app = app.filter(citizenship__nationality__exact=citizenship)
		if company or company == '':
			app = app.filter(company__company__exact=company)
		if gender or gender == '':
			app = app.filter(gender__gender__exact=gender)
		if blood_type or blood_type == '':
			app = app.filter(blood_type__blood_type__exact=blood_type)
		if suffix or suffix == '':
			app = app.filter(suffix__suffix__exact=suffix)
		if country or country == '':
			app = app.filter(company__country__country__exact=country)
		if state or state == '':
			app = app.filter(company__state__state__exact=state)
		if postal_code or postal_code == '':
			app = app.filter(company__postal_code__postal_code__exact=postal_code)
		if nationality or nationality == '':
			app = app.filter(company__nationality__nationality__exact=nationality)
		if birthday or birthday == '':
			app = app.filter(birthday__month=birthday)	
		if membership_date or membership_date == '':
			app = app.filter(membership_date__year=membership_date)		
		else:
			pass

		distinct = app.distinct().order_by('company__city__city')
		return distinct.values_list('company__city__city', 'company__city__city')


	def queryset(self, request, queryset):
		param = self.value()
		if param or param == '':
			return queryset.filter(company__city__city=param)

class CountryFilter(admin.SimpleListFilter, Variables):
	title = _('Country')
	parameter_name = 'country'

	def lookups(self, request, model_admin):
		position = request.GET.get('position')
		citizenship = request.GET.get('citizenship')
		company = request.GET.get('company')
		gender = request.GET.get('gender')
		blood_type = request.GET.get('blood_type')
		suffix = request.GET.get('suffix')
		city = request.GET.get('city')
		state = request.GET.get('state')
		postal_code = request.GET.get('postal_code')
		nationality = request.GET.get('nationality')
		birthday = request.GET.get('birthday')
		membership_date = request.GET.get('membership_date')

		app = Variables.AppObject

		if position or position == '':
			app = app.filter(position__position__exact=position)
		if citizenship or citizenship == '':
			app = app.filter(citizenship__nationality__exact=citizenship)
		if company or company == '':
			app = app.filter(company__company__exact=company)
		if gender or gender == '':
			app = app.filter(gender__gender__exact=gender)
		if blood_type or blood_type == '':
			app = app.filter(blood_type__blood_type__exact=blood_type)
		if suffix or suffix == '':
			app = app.filter(suffix__suffix__exact=suffix)
		if city or city == '':
			app = app.filter(company__city__city__exact=city)
		if state or state == '':
			app = app.filter(company__state__state__exact=state)
		if postal_code or postal_code == '':
			app = app.filter(company__postal_code__postal_code__exact=postal_code)
		if nationality or nationality == '':
			app = app.filter(company__nationality__nationality__exact=nationality)
		if birthday or birthday == '':
			app = app.filter(birthday__month=birthday)
		if membership_date or membership_date == '':
			app = app.filter(membership_date__year=membership_date)			
		else:
			pass

		distinct = app.distinct().order_by('company__country__country')
		return distinct.values_list('company__country__country', 'company__country__country')


	def queryset(self, request, queryset):
		param = self.value()
		if param or param == '':
			return queryset.filter(company__country__country=param)

class StateFilter(admin.SimpleListFilter, Variables):
	title = _('State')
	parameter_name = 'state'

	def lookups(self, request, model_admin):
		position = request.GET.get('position')
		citizenship = request.GET.get('citizenship')
		company = request.GET.get('company')
		gender = request.GET.get('gender')
		blood_type = request.GET.get('blood_type')
		suffix = request.GET.get('suffix')
		city = request.GET.get('city')
		country = request.GET.get('country')
		postal_code = request.GET.get('postal_code')
		nationality = request.GET.get('nationality')
		birthday = request.GET.get('birthday')
		membership_date = request.GET.get('membership_date')

		app = Variables.AppObject

		if position or position == '':
			app = app.filter(position__position__exact=position)
		if citizenship or citizenship == '':
			app = app.filter(citizenship__nationality__exact=citizenship)
		if company or company == '':
			app = app.filter(company__company__exact=company)
		if gender or gender == '':
			app = app.filter(gender__gender__exact=gender)
		if blood_type or blood_type == '':
			app = app.filter(blood_type__blood_type__exact=blood_type)
		if suffix or suffix == '':
			app = app.filter(suffix__suffix__exact=suffix)
		if city or city == '':
			app = app.filter(company__city__city__exact=city)
		if country or country == '':
			app = app.filter(company__country__country__exact=country)
		if postal_code or postal_code == '':
			app = app.filter(company__postal_code__postal_code__exact=postal_code)
		if nationality or nationality == '':
			app = app.filter(company__nationality__nationality__exact=nationality)
		if birthday or birthday == '':
			app = app.filter(birthday__month=birthday)
		if membership_date or membership_date == '':
			app = app.filter(membership_date__year=membership_date)			
		else:
			pass

		distinct = app.distinct().order_by('company__state__state')
		return distinct.values_list('company__state__state', 'company__state__state')


	def queryset(self, request, queryset):
		param = self.value()
		if param or param == '':
			return queryset.filter(company__state__state=param)

class PostalCodeFilter(admin.SimpleListFilter, Variables):
	title = _('Postal Code')
	parameter_name = 'postal_code'

	def lookups(self, request, model_admin):
		position = request.GET.get('position')
		citizenship = request.GET.get('citizenship')
		company = request.GET.get('company')
		gender = request.GET.get('gender')
		blood_type = request.GET.get('blood_type')
		suffix = request.GET.get('suffix')
		city = request.GET.get('city')
		country = request.GET.get('country')
		state = request.GET.get('state')
		nationality = request.GET.get('nationality')
		birthday = request.GET.get('birthday')
		membership_date = request.GET.get('membership_date')

		app = Variables.AppObject

		if position or position == '':
			app = app.filter(position__position__exact=position)
		if citizenship or citizenship == '':
			app = app.filter(citizenship__nationality__exact=citizenship)
		if company or company == '':
			app = app.filter(company__company__exact=company)
		if gender or gender == '':
			app = app.filter(gender__gender__exact=gender)
		if blood_type or blood_type == '':
			app = app.filter(blood_type__blood_type__exact=blood_type)
		if suffix or suffix == '':
			app = app.filter(suffix__suffix__exact=suffix)
		if city or city == '':
			app = app.filter(company__city__city__exact=city)
		if country or country == '':
			app = app.filter(company__country__country__exact=country)
		if state or state == '':
			app = app.filter(company__state__state__exact=state)
		if nationality or nationality == '':
			app = app.filter(company__nationality__nationality__exact=nationality)
		if birthday or birthday == '':
			app = app.filter(birthday__month=birthday)
		if membership_date or membership_date == '':
			app = app.filter(membership_date__year=membership_date)			
		else:
			pass

		distinct = app.distinct().order_by('company__postal_code__postal_code')
		return distinct.values_list('company__postal_code__postal_code', 'company__postal_code__postal_code')


	def queryset(self, request, queryset):
		param = self.value()
		if param or param == '':
			return queryset.filter(company__postal_code__postal_code=param)

class NationalityFilter(admin.SimpleListFilter, Variables):
	title = _('Nationality')
	parameter_name = 'nationality'

	def lookups(self, request, model_admin):
		position = request.GET.get('position')
		citizenship = request.GET.get('citizenship')
		company = request.GET.get('company')
		gender = request.GET.get('gender')
		blood_type = request.GET.get('blood_type')
		suffix = request.GET.get('suffix')
		city = request.GET.get('city')
		country = request.GET.get('country')
		state = request.GET.get('state')
		postal_code = request.GET.get('postal_code')
		birthday = request.GET.get('birthday')
		membership_date = request.GET.get('membership_date')

		app = Variables.AppObject

		if position or position == '':
			app = app.filter(position__position__exact=position)
		if citizenship or citizenship == '':
			app = app.filter(citizenship__nationality__exact=citizenship)
		if company or company == '':
			app = app.filter(company__company__exact=company)
		if gender or gender == '':
			app = app.filter(gender__gender__exact=gender)
		if blood_type or blood_type == '':
			app = app.filter(blood_type__blood_type__exact=blood_type)
		if suffix or suffix == '':
			app = app.filter(suffix__suffix__exact=suffix)
		if city or city == '':
			app = app.filter(company__city__city__exact=city)
		if country or country == '':
			app = app.filter(company__country__country__exact=country)
		if state or state == '':
			app = app.filter(company__state__state__exact=state)
		if postal_code or postal_code == '':
			app = app.filter(company__postal_code__postal_code__exact=postal_code)
		if birthday or birthday == '':
			app = app.filter(birthday__month=birthday)
		if membership_date or membership_date == '':
			app = app.filter(membership_date__year=membership_date)			
		else:
			pass

		distinct = app.distinct().order_by('company__nationality__nationality')
		return distinct.values_list('company__nationality__nationality', 'company__nationality__nationality')


	def queryset(self, request, queryset):
		param = self.value()
		if param or param == '':
			return queryset.filter(company__nationality__nationality=param)

class BirthdayFilter(admin.SimpleListFilter, Variables):
	title = _('Birthday')
	parameter_name = 'birthday'

	def lookups(self, request, model_admin):
		position = request.GET.get('position')
		citizenship = request.GET.get('citizenship')
		company = request.GET.get('company')
		gender = request.GET.get('gender')
		blood_type = request.GET.get('blood_type')
		suffix = request.GET.get('suffix')
		city = request.GET.get('city')
		country = request.GET.get('country')
		state = request.GET.get('state')
		postal_code = request.GET.get('postal_code')
		nationality = request.GET.get('nationality')
		membership_date = request.GET.get('membership_date')
		birthday = []
		choices = []

		app = Variables.AppObject

		if position or position == '':
			app = app.filter(position__position__exact=position)
		if citizenship or citizenship == '':
			app = app.filter(citizenship__nationality__exact=citizenship)
		if company or company == '':
			app = app.filter(company__company__exact=company)
		if gender or gender == '':
			app = app.filter(gender__gender__exact=gender)
		if blood_type or blood_type == '':
			app = app.filter(blood_type__blood_type__exact=blood_type)
		if suffix or suffix == '':
			app = app.filter(suffix__suffix__exact=suffix)
		if city or city == '':
			app = app.filter(company__city__city__exact=city)
		if country or country == '':
			app = app.filter(company__country__country__exact=country)
		if state or state == '':
			app = app.filter(company__state__state__exact=state)
		if postal_code or postal_code == '':
			app = app.filter(company__postal_code__postal_code__exact=postal_code)
		if nationality or nationality == '':
			app = app.filter(company__nationality__nationality__exact=nationality)
		if birthday or birthday == '':
			app = app.filter(birthday__month=birthday)
		if membership_date or membership_date == '':
			app = app.filter(membership_date__year=membership_date)				
		else:
			pass
		istinct = app.distinct().order_by('birthday')
		for x in range(1,13):
			# choices.append((x, "20's"))
			choices.append((x, calendar.month_name[x]))
		return choices

	def queryset(self, request, queryset):
		param = self.value()
		if param or param == '':
			return queryset.filter(birthday__month=param)

class MembershipFilter(admin.SimpleListFilter, Variables):
	title = _('Membership Date')
	parameter_name = 'membership_date'

	def lookups(self, request, model_admin):
		position = request.GET.get('position')
		citizenship = request.GET.get('citizenship')
		company = request.GET.get('company')
		gender = request.GET.get('gender')
		blood_type = request.GET.get('blood_type')
		suffix = request.GET.get('suffix')
		city = request.GET.get('city')
		country = request.GET.get('country')
		state = request.GET.get('state')
		postal_code = request.GET.get('postal_code')
		nationality = request.GET.get('nationality')
		birthday = request.GET.get('birthday')
		membership = []

		app = Variables.AppObject

		if position or position == '':
			app = app.filter(position__position__exact=position)
		if citizenship or citizenship == '':
			app = app.filter(citizenship__nationality__exact=citizenship)
		if company or company == '':
			app = app.filter(company__company__exact=company)
		if gender or gender == '':
			app = app.filter(gender__gender__exact=gender)
		if blood_type or blood_type == '':
			app = app.filter(blood_type__blood_type__exact=blood_type)
		if suffix or suffix == '':
			app = app.filter(suffix__suffix__exact=suffix)
		if city or city == '':
			app = app.filter(company__city__city__exact=city)
		if country or country == '':
			app = app.filter(company__country__country__exact=country)
		if state or state == '':
			app = app.filter(company__state__state__exact=state)
		if postal_code or postal_code == '':
			app = app.filter(company__postal_code__postal_code__exact=postal_code)
		if nationality or nationality == '':
			app = app.filter(company__nationality__nationality__exact=nationality)
		if birthday or birthday == '':
			app = app.filter(birthday__month=birthday)			
		else:
			pass

		distinct = app.distinct().order_by('membership_date')
		for distincts in distinct:
			if distincts.membership_date != None:
				print membership.append((distincts.membership_date.year, distincts.membership_date.year))
		membership = set(membership)
		membership = list(membership)
		membership = sorted(membership)
		return membership		
		# return distinct.values_list('membership_date', 'membership_date')

	def queryset(self, request, queryset):
		param = self.value()
		if param or param == '':
			return queryset.filter(membership_date__year=param)


class MemberResource(resources.ModelResource):
	first_name = fields.Field(column_name='First Name', attribute='first_name' )
	middle_name = fields.Field(column_name='Middle Name', attribute='middle_name' )
	last_name = fields.Field(column_name='Last Name', attribute='last_name' )
	membership_date = fields.Field(column_name='Membership Date', attribute='membership_date' )
	company = fields.Field(column_name='Company', attribute='company__company' )
	position = fields.Field(column_name='Position', attribute='position__position' )
	personal_email = fields.Field(column_name='Personal Email', attribute='personal_email__email' )
	company_email = fields.Field(column_name='Company Email', attribute='company_email__email' )
	telephone = fields.Field(column_name='Telephone', attribute='telephone' )
	fax = fields.Field(column_name='Fax', attribute='fax' )
	mobile = fields.Field(column_name='Mobile', attribute='mobile' )
	citizenship = fields.Field(column_name='citizenship', attribute='citizenship__nationality' )
	birthday = fields.Field(column_name='Birthday', attribute='birthday' )
	gender = fields.Field(column_name='Gender', attribute='gender__gender' )
	blood_type = fields.Field(column_name='Blood Type', attribute='blood_type__blood_type' )
	suffix = fields.Field(column_name='Suffix', attribute='suffix__suffix' )

	class Meta:
		model = Member
		exclude = ('id', )
		export_order = ('first_name', 'middle_name', 'last_name', 
			'membership_date', 'company', 'position', 'personal_email', 
			'company_email', 'telephone', 'fax', 'mobile', 'citizenship', 
			'birthday', 'gender', 'blood_type', 'suffix',)


class MemberAdmin(ImportExportActionModelAdmin):
	resource_class = MemberResource
	formats = ( base_formats.XLS, base_formats.CSV )
	list_filter = (CompanyFilter, PositionFilter, CitizenshipFilter, GenderFilter, 
					BloodTypeFilter, SuffixFilter, CityFilter, CountryFilter, StateFilter, 
					PostalCodeFilter, NationalityFilter, BirthdayFilter, MembershipFilter)
	list_display = ('full_name', 'company', 'company_email', 'telephone', 'fax', 'mobile', 
					'personal_email', 'position', 'citizenship', 'membership_date','birthday', 'gender', 
					'blood_type', 'suffix', 'company_website', 'company_description', 
					'company_website', 'company_street_1', 'company_street_2', 'company_city', 
					'company_country', 'company_postal_code', 'company_state', 
					'company_nationality', 'company_us_address_1', 'company_us_address_2', 
					'company_us_city', 'company_us_zip', 'company_us_state', 'company_tin', 
					'company_annual_revenue',)
	search_fields = ('first_name', 'last_name', 'mobile', 'telephone', 'fax', 
					'company__company', 'personal_email__email', 'company_email__email' )

	def company_description(self, obj):
		return obj.company.description

	def company_website(self, obj):
		return obj.company.website

	def company_street_1(self, obj):
		return obj.company.street_1

	def company_street_2(self, obj):
		return obj.company.street_2

	def company_city(self, obj):
		return obj.company.city

	def company_country(self, obj):
		return obj.company.country

	def company_postal_code(self, obj):
		return obj.company.postal_code

	def company_state(self, obj):
		return obj.company.state

	def company_nationality(self, obj):
		return obj.company.nationality

	def company_us_address_1(self, obj):
		return obj.company.us_address_1

	def company_us_address_2(self, obj):
		return obj.company.us_address_2

	def company_us_city(self, obj):
		return obj.company.us_city

	def company_us_zip(self, obj):
		return obj.company.us_zip

	def company_us_state(self, obj):
		return obj.company.us_state

	def company_tin(self, obj):
		return obj.company.tin

	def company_annual_revenue(self, obj):
		return obj.company.annual_revenue




# admin.site.register(ExecRepresentative, ExecRepImport)
# admin.site.register(AltRepresentative, AltRepImport)
# admin.site.register(BloodType, BloodTypeImport)
# admin.site.register(City, CityImport)
# admin.site.register(Email, EmailImport)
# admin.site.register(Country, CountryImport)
# admin.site.register(Gender)
# admin.site.register(Nationality, NationalityImport)
# admin.site.register(Position, PositionImport)
# admin.site.register(PostalCode, PostalCodeImport)
# admin.site.register(ReferredBy, ReferredByImport)
# admin.site.register(State, StateImport)
# admin.site.register(Suffix, SuffixImport)
# admin.site.register(Company, CompanyImport)
# admin.site.register(Member, MemberImport)
admin.site.register(Member, MemberAdmin)
admin.site.register(Company, CompanyAdmin)


# class NullImporter(widgets.ForeignKeyWidget):
# 	def clean(self, value):
# 		val = value
# 		# val = super(NullImporter, self).clean(value)
# 		if val == None:
# 			# if self.field != 'postal_code':
# 			val = ''
# 			# else:
# 			# 	pass
# 		# else:
# 		# Remove string conversion to enable ascii
# 		# 	val = str(val)
# 		return self.model.objects.get(**{self.field: val})

# class MemberResource(resources.ModelResource):
# 	company = fields.Field(column_name='company', attribute='company', widget=NullImporter(Company, 'company', ))
# 	position = fields.Field(column_name='position', attribute='position', widget=NullImporter(Position, 'position', ))
# 	personal_email = fields.Field(column_name='personal_email', attribute='personal_email', widget=NullImporter(Email, 'email', ))
# 	company_email = fields.Field(column_name='company_email', attribute='company_email', widget=NullImporter(Email, 'email', ))
# 	citizenship = fields.Field(column_name='citizenship', attribute='citizenship', widget=NullImporter(Nationality, 'nationality', ))
# 	gender = fields.Field(column_name='gender', attribute='gender', widget=NullImporter(Gender, 'gender', ))
# 	blood_type = fields.Field(column_name='blood_type', attribute='blood_type', widget=NullImporter(BloodType, 'blood_type', ))
# 	suffix = fields.Field(column_name='suffix', attribute='suffix', widget=NullImporter(Suffix, 'suffix', ))

# 	class Meta:
# 		model = Member
# 		field = ['id', 'first_name', 'middle_name', 'last_name', 'membership_date', 
# 				'telephone', 'fax', 'mobile', 'birthday']

# class MemberImport(ImportExportModelAdmin):
# 	resource_class = MemberResource

# class CompanyResource(resources.ModelResource):
# 	city = fields.Field(column_name='city', attribute='city', widget=NullImporter(City, 'city', ))
# 	country = fields.Field(column_name='country', attribute='country', widget=NullImporter(Country, 'country', ))
# 	postal_code = fields.Field(column_name='postal_code', attribute='postal_code', widget=NullImporter(PostalCode, 'postal_code', ))
# 	state = fields.Field(column_name='state', attribute='state', widget=NullImporter(State, 'state', ))
# 	nationality = fields.Field(column_name='nationality', attribute='nationality', widget=NullImporter(Nationality, 'nationality', ))
# 	us_city = fields.Field(column_name='us_city', attribute='us_city', widget=NullImporter(City, 'city', ))
# 	us_zip = fields.Field(column_name='us_zip', attribute='us_zip', widget=NullImporter(PostalCode, 'postal_code', ))
# 	us_state = fields.Field(column_name='us_state', attribute='us_state', widget=NullImporter(State, 'state', ))
# 	class Meta:
# 		model = Company
# 		# fields = ['id', 'name', 'company__country__country', 'company__postal_code__postal_code', 'website__website', 'company__state__state']
# 		fields = ['id', 'company', 'description', 'website', 'street_1', 'street_2', 'us_address_1', 'us_address_2', 'tin', 'annual_revenue']

# class CompanyImport(ImportExportModelAdmin):
# 	resource_class = CompanyResource

# class ExecRepResource(resources.ModelResource):
# 	class Meta:
# 		model = ExecRepresentative

# class ExecRepImport(ImportExportModelAdmin):
# 	exclude = ['last_name']
# 	resource_class = ExecRepResource

# class AltRepResource(resources.ModelResource):
# 	class Meta:
# 		model = AltRepresentative

# class AltRepImport(ImportExportModelAdmin):
# 	exclude = ['last_name']
# 	resource_class = AltRepResource

# class BloodTypeResource(resources.ModelResource):
# 	class Meta:
# 		model = BloodType

# class BloodTypeImport(ImportExportModelAdmin):
# 	resource_class = BloodTypeResource

# class CityResource(resources.ModelResource):
# 	class Meta:
# 		model = City

# class CityImport(ImportExportModelAdmin):
# 	resource_class = CityResource

# class EmailResource(resources.ModelResource):
# 	class Meta:
# 		model = Email

# class EmailImport(ImportExportModelAdmin):
# 	resource_class = EmailResource

# class CountryResource(resources.ModelResource):
# 	class Meta:
# 		model = Country

# class CountryImport(ImportExportModelAdmin):
# 	resource_class = CountryResource

# class NationalityResource(resources.ModelResource):
# 	class Meta:
# 		model = Nationality

# class NationalityImport(ImportExportModelAdmin):
# 	resource_class = NationalityResource

# class PositionResource(resources.ModelResource):
# 	class Meta:
# 		model = Position

# class PositionImport(ImportExportModelAdmin):
# 	resource_class = PositionResource

# class PostalCodeResource(resources.ModelResource):
# 	class Meta:
# 		model = PostalCode

# class PostalCodeImport(ImportExportModelAdmin):
# 	resource_class = PostalCodeResource

# class ReferredByResource(resources.ModelResource):
# 	class Meta:
# 		model = ReferredBy

# class ReferredByImport(ImportExportModelAdmin):
# 	resource_class = ReferredByResource

# class StateResource(resources.ModelResource):
# 	class Meta:
# 		model = State

# class StateImport(ImportExportModelAdmin):
# 	resource_class = StateResource

# class SuffixResource(resources.ModelResource):
# 	class Meta:
# 		model = Suffix

# class SuffixImport(ImportExportModelAdmin):
# 	resource_class = SuffixResource

# class MemberAdmin(admin.ModelAdmin):
# 	list_filter = ('company', 'position', 'citizenship', 'gender', 'blood_type', 'suffix', 
# 					'company__city__city', 'company__country__country', 'company__state__state', 'company__postal_code__postal_code',
# 					'company__nationality__nationality', )
# 	list_display = ('full_name', 'company', 'company_email', 'telephone', 'fax', 'mobile', 
# 					'personal_email', 'position', 'citizenship', 'birthday', 'gender', 
# 					'blood_type', 'suffix', 'company_website', 'company_description', 
# 					'company_website', 'company_street_1', 'company_street_2', 'company_city', 
# 					'company_country', 'company_postal_code', 'company_state', 
# 					'company_nationality', 'company_us_address_1', 'company_us_address_2', 
# 					'company_us_city', 'company_us_zip', 'company_us_state', 'company_tin', 
# 					'company_annual_revenue',)
# 	search_fields = ('first_name', 'middle_name', 'last_name', 'mobile', 'telephone', 'fax')

# 	def company_description(self, obj):
# 		return obj.company.description

# 	def company_website(self, obj):
# 		return obj.company.website

# 	def company_street_1(self, obj):
# 		return obj.company.street_1

# 	def company_street_2(self, obj):
# 		return obj.company.street_2

# 	def company_city(self, obj):
# 		return obj.company.city

# 	def company_country(self, obj):
# 		return obj.company.country

# 	def company_postal_code(self, obj):
# 		return obj.company.postal_code

# 	def company_state(self, obj):
# 		return obj.company.state

# 	def company_nationality(self, obj):
# 		return obj.company.nationality

# 	def company_us_address_1(self, obj):
# 		return obj.company.us_address_1

# 	def company_us_address_2(self, obj):
# 		return obj.company.us_address_2

# 	def company_us_city(self, obj):
# 		return obj.company.us_city

# 	def company_us_zip(self, obj):
# 		return obj.company.us_zip

# 	def company_us_state(self, obj):
# 		return obj.company.us_state

# 	def company_tin(self, obj):
# 		return obj.company.tin

# 	def company_annual_revenue(self, obj):
# 		return obj.company.annual_revenue
