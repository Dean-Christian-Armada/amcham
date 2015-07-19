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

# class NullImporter(widgets.ForeignKeyWidget):
# 	def clean(self, value):
# 		val = super(NullImporter, self).clean(value)
# 		if val == None:
# 			# if self.field != 'postal_code':
# 			val = ''
# 			# else:
# 			# 	pass
# 		else:
# 			val = str(val)
# 		return self.model.objects.get(**{self.field: val})

class CompanyResource(resources.ModelResource):
	class Meta:
		model = Company

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

class MemberResource(resources.ModelResource):
	class Meta:
		model = Member

class MemberImport(ImportExportModelAdmin):
	resource_class = MemberResource

class MemberAdmin(admin.ModelAdmin):
	list_display = ['name', 'company', 'membership_date', 'position', 'email', 'street_1', 'street_2', 'city', 'postal_code', 'state', 'citizenship', 'birthday', 'gender', 'blood_type', 'suffix', 'referred_by']
	list_filter = ['gender']

admin.site.register(Member, MemberAdmin)
admin.site.register(Company, CompanyImport)
admin.site.register(ExecRepresentative, ExecRepImport)
admin.site.register(AltRepresentative, AltRepImport)