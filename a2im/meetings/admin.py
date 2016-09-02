from django.contrib import admin
from .models import Event, Company, Meeting

# Register your models here.

admin.site.register(Event)
admin.site.register(Company)
admin.site.register(Meeting)

