from __future__ import unicode_literals

from django.db import models

# Create your models here.
class StaffUser(models.Model):
	loginid = models.CharField(max_length=50, unique=True)
	password = models.CharField(max_length=50)
	fullname = models.CharField(max_length=100)
	contact_no = models.CharField(max_length=15)
	alternate_contact_no = models.CharField(max_length=15,null=True)
	address = models.TextField()

	def __str__(self):
		return self.fullname

class LandDetail(models.Model):
	belonging_to = models.CharField(max_length=50)
	ph_no = models.CharField(max_length=20)
	survey_no = models.CharField(max_length=20)
	village = models.CharField(max_length=50)
	panchayat = models.CharField(max_length=50)
	tehsil = models.CharField(max_length=50)
	district = models.CharField(max_length=50)
	taluka = models.CharField(max_length=50)
	irrigation = models.CharField(max_length=50)
	broker_name = models.CharField(max_length=100)
	purchase_date = models.DateField()
	total_area = models.FloatField()
	rate = models.FloatField()
	total_cost = models.FloatField()
	registeration_date = models.DateField()
	amount = models.FloatField()
	advance_amount = models.FloatField()
	description = models.TextField()

	def __str__(self):
		return self.survey_no




