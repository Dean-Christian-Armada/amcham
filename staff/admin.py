from django.contrib import admin
from import_export import resources, widgets
from import_export.admin import ImportExportModelAdmin
from import_export import fields
from . models import *
# Register your models here.

# class MemberInline(admin.TabularInline):
# 	model = Member
# 	# fk_name = 'Company'



# class CompanyAdmin(admin.ModelAdmin):
# 	inlines = [
# 		MemberInline
# 	]

# admin.site.register(Member)
# admin.site.register(Company, CompanyAdmin)
# admin.site.register(AltRepresentative)

class NullImporter(widgets.ForeignKeyWidget):
	def clean(self, value):
		val = value
		# val = super(NullImporter, self).clean(value)
		if val == None:
			# if self.field != 'postal_code':
			val = ''
			# else:
			# 	pass
		# else:
		# Remove string conversion to enable ascii
		# 	val = str(val)
		return self.model.objects.get(**{self.field: val})

class CompanyResource(resources.ModelResource):
	city = fields.Field(column_name='city', attribute='city', widget=NullImporter(City, 'city', ))
	country = fields.Field(column_name='country', attribute='country', widget=NullImporter(Country, 'country', ))
	postal_code = fields.Field(column_name='postal_code', attribute='postal_code', widget=NullImporter(PostalCode, 'postal_code', ))
	state = fields.Field(column_name='state', attribute='state', widget=NullImporter(State, 'state', ))
	nationality = fields.Field(column_name='nationality', attribute='nationality', widget=NullImporter(Nationality, 'nationality', ))
	us_city = fields.Field(column_name='us_city', attribute='us_city', widget=NullImporter(City, 'city', ))
	us_zip = fields.Field(column_name='us_zip', attribute='us_zip', widget=NullImporter(PostalCode, 'postal_code', ))
	us_state = fields.Field(column_name='us_state', attribute='us_state', widget=NullImporter(State, 'state', ))
	class Meta:
		model = Company
		# fields = ['id', 'name', 'country__country', 'postal_code__postal_code', 'website__website', 'state__state']
		fields = ['id', 'company', 'description', 'website', 'street_1', 'street_2', 'us_address_1', 'us_address_2', 'tin', 'annual_revenue']

class CompanyImport(ImportExportModelAdmin):
	resource_class = CompanyResource

class ExecRepResource(resources.ModelResource):
	class Meta:
		model = ExecRepresentative

class ExecRepImport(ImportExportModelAdmin):
	resource_class = ExecRepResource

class AltRepResource(resources.ModelResource):
	class Meta:
		model = AltRepresentative

class AltRepImport(ImportExportModelAdmin):
	resource_class = AltRepResource

class BloodTypeResource(resources.ModelResource):
	class Meta:
		model = BloodType

class BloodTypeImport(ImportExportModelAdmin):
	resource_class = BloodTypeResource

class CityResource(resources.ModelResource):
	class Meta:
		model = City

class CityImport(ImportExportModelAdmin):
	resource_class = CityResource

class EmailResource(resources.ModelResource):
	class Meta:
		model = Email

class EmailImport(ImportExportModelAdmin):
	resource_class = EmailResource

class CountryResource(resources.ModelResource):
	class Meta:
		model = Country

class CountryImport(ImportExportModelAdmin):
	resource_class = CountryResource

class NationalityResource(resources.ModelResource):
	class Meta:
		model = Nationality

class NationalityImport(ImportExportModelAdmin):
	resource_class = NationalityResource

class PositionResource(resources.ModelResource):
	class Meta:
		model = Position

class PositionImport(ImportExportModelAdmin):
	resource_class = PositionResource

class PostalCodeResource(resources.ModelResource):
	class Meta:
		model = PostalCode

class PostalCodeImport(ImportExportModelAdmin):
	resource_class = PostalCodeResource

class ReferredByResource(resources.ModelResource):
	class Meta:
		model = ReferredBy

class ReferredByImport(ImportExportModelAdmin):
	resource_class = ReferredByResource

class StateResource(resources.ModelResource):
	class Meta:
		model = State

class StateImport(ImportExportModelAdmin):
	resource_class = StateResource

class SuffixResource(resources.ModelResource):
	class Meta:
		model = Suffix

class SuffixImport(ImportExportModelAdmin):
	resource_class = SuffixResource

# class MemberResource(resources.ModelResource):
# 	class Meta:
# 		model = Member

# class MemberImport(ImportExportModelAdmin):
# 	resource_class = MemberResource

# class MemberAdmin(admin.ModelAdmin):
# 	list_display = ['name', 'company', 'membership_date', 'position', 'email', 'street_1', 'street_2', 'city', 'postal_code', 'state', 'citizenship', 'birthday', 'gender', 'blood_type', 'suffix', 'referred_by']
# 	list_filter = ['gender']

# admin.site.register(Member, MemberAdmin)
# admin.site.register(Company, CompanyImport)
admin.site.register(ExecRepresentative, ExecRepImport)
admin.site.register(AltRepresentative, AltRepImport)
admin.site.register(BloodType, BloodTypeImport)
admin.site.register(City, CityImport)
admin.site.register(Email, EmailImport)
admin.site.register(Country, CountryImport)
admin.site.register(Gender)
admin.site.register(Nationality, NationalityImport)
admin.site.register(Position, PositionImport)
admin.site.register(PostalCode, PostalCodeImport)
admin.site.register(ReferredBy, ReferredByImport)
admin.site.register(State, StateImport)
admin.site.register(Suffix, SuffixImport)
admin.site.register(Company, CompanyImport)