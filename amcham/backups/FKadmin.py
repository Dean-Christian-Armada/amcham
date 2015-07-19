from django.contrib import admin
from import_export import resources, widgets
from import_export.admin import ImportExportModelAdmin
from import_export import fields
from . models import *
# Register your models here.

# # 
# class NullImporter(widgets.ForeignKeyWidget):
# 	def clean(self, value):
# 		val = super(NullImporter, self).clean(value)
# 		if val == None:
# 			if self.field != 'postal_code':
# 				val = ''
# 			else:
# 				pass
# 		else:
# 			val = str(val)
# 		return self.model.objects.get(**{self.field: val})

# class CompanyResource(resources.ModelResource):
# 	country = fields.Field(column_name='country', attribute='country', widget=NullImporter(Country, 'country', ))
# 	postal_code = fields.Field(column_name='postal_code', attribute='postal_code', widget=NullImporter(Postal_Code, 'postal_code', ))
# 	website = fields.Field(column_name='website', attribute='website', widget=NullImporter(Website, 'website', ))
# 	state = fields.Field(column_name='state', attribute='state', widget=NullImporter(State, 'state', ))
# 	class Meta:
# 		model = Company
# 		# fields = ['id', 'name', 'country__country', 'postal_code__postal_code', 'website__website', 'state__state']
# 		fields = ['id', 'name']

# class CountryResource(resources.ModelResource):
# 	class Meta:
# 		model = Country

# class PostalCodeResource(resources.ModelResource):
# 	class Meta:
# 		model = Postal_Code

# class WebsiteResource(resources.ModelResource):
# 	class Meta:
# 		model = Website

# class StateResource(resources.ModelResource):
# 	class Meta:
# 		model = State

# class CompanyImport(ImportExportModelAdmin):
# 	resource_class = CompanyResource

# class CountryImport(ImportExportModelAdmin):
# 	resource_class = CountryResource

# class PostalCodeImport(ImportExportModelAdmin):
# 	resource_class = PostalCodeResource

# class WebsiteImport(ImportExportModelAdmin):
# 	resource_class = WebsiteResource

# class StateImport(ImportExportModelAdmin):
# 	resource_class = StateResource

# class CompanyAdmin(admin.ModelAdmin):
# 	# resource_class = CompanyResource
# 	list_display = ('name', 'country', 'postal_code', 'website', 'state',)
# 	list_per_page = 20



# admin.site.register(Company, CompanyImport)
# admin.site.register(Country, CountryImport)
# admin.site.register(Postal_Code, PostalCodeImport)
# admin.site.register(Website, WebsiteImport)
# admin.site.register(State, StateImport)

# # admin.site.register(Company)
# admin.site.register(Country)
# admin.site.register(Postal_Code)
# admin.site.register(Website)
# admin.site.register(State)