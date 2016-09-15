from django.contrib import admin
from .models import Event, Company, Meeting, CompanyGroup
from django.forms import TextInput, Textarea
from django.db import models

# Register your models here.

# admin.site.register(Company)
# admin.site.register(Meeting)

class CompanyInline(admin.TabularInline):
	model = Company

class CompanyGroupAdmin(admin.ModelAdmin):
	# list_display = ('name', 'email', 'type_of_company')
	inlines = [
		CompanyInline,
	]

class MeetingInline(admin.TabularInline):
	model = Meeting
	formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':1, 'cols':40})},
    }


class EventAdmin(admin.ModelAdmin):
	inlines = [
		MeetingInline,
	]

admin.site.register(Event, EventAdmin)
admin.site.register(CompanyGroup, CompanyGroupAdmin)
