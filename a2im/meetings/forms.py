from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, HTML
from crispy_forms.bootstrap import FormActions

from .models import Company, Event, Meeting

class CompanyForm(forms.ModelForm):
	class Meta:
		model = Company
		fields = ('name', 'email', 'type_of_company')