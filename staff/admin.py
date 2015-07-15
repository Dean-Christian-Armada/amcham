from django.contrib import admin
from import_export import resources, widgets
from import_export.admin import ImportExportModelAdmin
from . models import *
# Register your models here.

class Dean(widgets.ForeignKeyWidget):
	# class Meta:
	def __init__(self, model, field='pk', *args, **kwargs):
		self.model = Country
		self.field= 'country'
		super(Country, self).__init__(*args, **kwargs)

	def clean(self, value):
		val = super(Country, self).clean(value)
		return self.model.objects.get(**{self.field: val}) if val else None


class CompanyResource(resources.ModelResource):
	# This is still error fix this
	# author = fields.Field(column_name='country', attribute='country', widget=Dean(Country, 'country') )
	class Meta:
		model = Company
		# fields = ['id', 'name', 'country__country', 'postal_code__postal_code', 'website__website', 'state__state']
		fields = ['id', 'name', 'country']

class CountryResource(resources.ModelResource):
	class Meta:
		model = Country

class PostalCodeResource(resources.ModelResource):
	class Meta:
		model = Postal_Code

class WebsiteResource(resources.ModelResource):
	class Meta:
		model = Website

class StateResource(resources.ModelResource):
	class Meta:
		model = State

class CompanyImport(ImportExportModelAdmin):
	resource_class = CompanyResource

class CountryImport(ImportExportModelAdmin):
	resource_class = CountryResource

class PostalCodeImport(ImportExportModelAdmin):
	resource_class = PostalCodeResource

class WebsiteImport(ImportExportModelAdmin):
	resource_class = WebsiteResource

class StateImport(ImportExportModelAdmin):
	resource_class = StateResource

class CompanyAdmin(admin.ModelAdmin):
	# resource_class = CompanyResource
	list_display = ('name', 'country', 'postal_code', 'website', 'state',)
	list_per_page = 20



admin.site.register(Company, CompanyImport)
admin.site.register(Country, CountryImport)
admin.site.register(Postal_Code, PostalCodeImport)
admin.site.register(Website, WebsiteImport)
admin.site.register(State, StateImport)