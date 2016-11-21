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


class AgentAccount(models.Model):
	account_number = models.CharField(max_length=20)

	def __str__(self):
		return self.account_number



class AgentType(models.Model):
	type_name = models.CharField(max_length=50)

	def __str__(self):
		return self.type_name


class NominiDetail(models.Model):
	MALE = "Male"
	FEMALE = "Female"
	gender_choices = (
		(MALE, 'Male'),
		(FEMALE, 'Female'),
		)
	fullname = models.CharField(max_length=50)
	age = models.IntegerField()
	gender = models.CharField(max_length=6, choices=gender_choices)
	relation = models.CharField(max_length=20)
	address = models.TextField()
	contact_no = models.CharField(max_length=15)
	email = models.EmailField(max_length=100, null=True)
	belong_to = models.CharField(max_length=10)

	def __str__(self):
		return self.fullname


class AgentDetail(models.Model):
	first_name = models.CharField(max_length=20)
	middle_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20)
	father_name = models.CharField(max_length=50)
	mother_name = models.CharField(max_length=50)
	pancard = models.CharField(max_length=50, null=True)
	address = models.TextField()
	date_of_birth = models.DateField()
	contact_no = models.CharField(max_length=15)
	alternate_contact_no = models.CharField(max_length=15, null=True) 
	email = models.EmailField(null=True)
	date_of_joining = models.DateField()
	percentage_alloted = models.FloatField()
	Nomini_id = models.ForeignKey('NominiDetail', on_delete=models.CASCADE)
	type_id = models.ForeignKey('AgentType')
	introducor_id = models.ForeignKey('self')
	introducer_percentage = models.FloatField()
	account_id = models.ForeignKey('AgentAccount')

	def __str__(self):
		return self.first_name


class CustomerDetail(models.Model):
	MALE = "Male"
	FEMALE = "Female"
	gender_choices = (
		(MALE, 'Male'),
		(FEMALE, 'Female'),
		)
	first_name = models.CharField(max_length=20)
	middle_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20)
	date_of_birth = models.DateField()
	pancard = models.CharField(max_length=50, null=True)
	address = models.TextField()
	contact_no = models.CharField(max_length=15)
	alternate_contact_no = models.CharField(max_length=15, null=True) 
	email = models.EmailField(null=True)
	date_of_joining = models.DateField()
	gender = models.CharField(max_length=6, choices=gender_choices)

	def __str__(self):
		return self.first_name

class ProjectDetail(models.Model):
	project_name = models.CharField(max_length = 50)
	description = models.TextField()
	land_detail_id = models.ForeignKey('LandDetail')
	layout_detail_id = models.ForeignKey('LayoutDetail')


class LayoutDetail(models.Model):
	layout_name = models.CharField(max_length = 50)
	remark = models.TextField()
	date = models.DateField()
	area_under_layout = models.FloatField()
	area_under_plot = models.FloatField()
	area_under_possession = models.FloatField()
	area_under_open_space = models.FloatField()
	area_under_public_utility = models.FloatField()
	area_under_road = models.FloatField()
	land_detail_id = models.ForeignKey('LandDetail')


class PlotDetail(models.Model):
	plot_number = models.CharField(max_length = 10)
	remark = models.TextField()
	date = models.DateField()
	total_area = models.FloatField()
	tan_area = models.FloatField()
	net_area = models.FloatField()
	status = models.CharField(max_length = 15)
	project_id = models.ForeignKey('ProjectDetail')
	plot_category_id = models.ForeignKey('PlotCategory')


class PlotCategory(models.Model):
	layout_name = models.CharField(max_length = 50)
	remark = models.TextField()
	date = models.DateField()
	area_under_layout = models.FloatField()
	area_under_plot = models.FloatField()
	area_under_possession = models.FloatField()
	area_under_open_space = models.FloatField()
	area_under_public_utility = models.FloatField()
	area_under_road = models.FloatField()
	land_detail_id = models.ForeignKey('LandDetail')
