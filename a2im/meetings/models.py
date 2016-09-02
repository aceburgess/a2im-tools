from __future__ import unicode_literals

from django.db import models

class Event(models.Model):
	name = models.CharField(max_length=200)
	start_date = models.DateTimeField()
	end_date = models.DateTimeField()

	def __str__(self):
		return self.event_name

class Company(models.Model):
	TYPE_OF_COMPANY = (
		('srv', 'service'),
		('lbl', 'label'),
		('oth', 'other'),
	)

	name = models.CharField(max_length=200)
	email = models.EmailField()
	type_of_company = models.CharField(max_length=3, choices=TYPE_OF_COMPANY)

	class Meta:
		verbose_name_plural = 'companies'

	def __str__(self):
		return self.name

# class Service(Company):
# 	class Meta:
# 		proxy = True

# class Label(Company):
# 	class Meta:
# 		proxy = True

# class Other(Company):
# 	class Meta:
# 		proxy = True

class Meeting(models.Model):
	event = models.ForeignKey(Event, on_delete=models.CASCADE)
	requestor = models.ForeignKey(Company, related_name="%(app_label)s_%(class)s_requestor", on_delete=models.CASCADE)
	requestee = models.ForeignKey(Company, related_name="%(app_label)s_%(class)s_requestee", on_delete=models.CASCADE)
	want_to_meet = models.NullBooleanField()
	available_from = models.TimeField()
	available_until = models.TimeField()
	comments = models.TextField(max_length=200)

	def __str__(self):
		return 'Meeting between %s and %s' % (self.requestor, self.requestee)



