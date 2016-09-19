from __future__ import unicode_literals

# import hashlib
# from binascii import hexlify
from django.db import models

import logging

# def _create_hash():
# 	the_hash = hashlib.sha1()
# 	return the_hash.hexdigest()[:-8]


class BaseModel(models.Model):
	created_at = models.DateTimeField(auto_now_add = True)
	modified_at = models.DateTimeField(auto_now = True)

	class Meta:
		abstract = True


class Event(BaseModel):
	name = models.CharField(max_length=200)
	start_date = models.DateTimeField()
	end_date = models.DateTimeField()

	def __str__(self):
		return self.name

	def generate_meetings(self):
		companies = Company.objects.all()
		past_companies = []
		for company in companies:
			for company2 in companies:
				if company == company2:
					continue
				elif company2 in past_companies:
					continue 
				meeting = Meeting(
					event=self,
					requestor=company,
					requestee=company2
				)
				past_companies.extend([company,])
				meeting.save()

	def delete_meetings(self):
		meetings = Meeting.objects.filter(event_id=self.id)
		meetings.delete()

	def determine_meetings(self):
		meetings = Meeting.objects.filter(event_id=self.id)
		should_meet = []
		should_not_meet = []
		undecided = []
		for meeting in meetings:
			if meeting.should_meet() == True:
				should_meet.extend([meeting,])
			elif meeting.should_meet() == False:
				should_not_meet.extend([meeting,])
			else:
				undecided.extend([meeting,])
		return {'should_meet': should_meet, 'should_not_meet': should_not_meet, 'undecided': undecided}

class CompanyGroup(BaseModel):
	name = models.CharField(max_length=200)

	def __str__(self):
		return 'Edit Companies'

class Company(BaseModel):
	TYPE_OF_COMPANY = (
		('srv', 'service'),
		('lbl', 'label'),
		('oth', 'other'),
	)

	name = models.CharField(max_length=200)
	email = models.EmailField()
	type_of_company = models.CharField(max_length=3, choices=TYPE_OF_COMPANY)
	company_group = models.ForeignKey(CompanyGroup, on_delete=models.CASCADE)

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

class Meeting(BaseModel):
	event = models.ForeignKey(Event, on_delete=models.CASCADE)
	requestor = models.ForeignKey(Company, related_name="%(app_label)s_%(class)s_requestor", on_delete=models.CASCADE)
	requestee = models.ForeignKey(Company, related_name="%(app_label)s_%(class)s_requestee", on_delete=models.CASCADE)
	requestor_wants_to_meet = models.NullBooleanField()
	requestee_wants_to_meet = models.NullBooleanField()
	# should_meet = models.NullBooleanField()
	# available_from = models.TimeField()
	# available_until = models.TimeField()
	comments = models.TextField(max_length=200, blank=True)
	# unique_url = models.CharField(max_length = 8)

	# def save(self, *args, **kwargs):
	# 	self.unique_url = _create_hash()
	# 	super(Meeting, self).save(*args, **kwargs)

	def __str__(self):
		return 'Meeting between %s and %s' % (self.requestor, self.requestee)

	def should_meet(self):
		if self.requestor_wants_to_meet == True and self.requestee_wants_to_meet == True:
			return True
		elif self.requestor_wants_to_meet == False or self.requestee_wants_to_meet == False:
			return False
		else:
			return 'Undecided'





