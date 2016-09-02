from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, HTML
from crispy_forms.bootstrap import FormActions

from meetings.models import Company, Event, Meeting

class EventForm(forms.ModelForm):
	class Meta:
		model = Event
		fields = ['name', 'start_date', 'end_date']

	def __init__(self, *args, **kwargs):
		super(EventForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_id = 'event-form'
		self.helper.form_class = 'form-horizontal'
		self.helper.label_class = 'col-lg-2'
		self.helper.field_class = 'col-lg-8'
		self.helper.form_method = 'POST'
		self.helper.form_action = 'submit_event'

		self.helper.add_input(Submit('submit', 'Submit'))