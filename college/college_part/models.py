from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class College(models.Model):
	name = models.CharField(max_length=50)
	logo = models.ImageField(upload_to='college_part/college')
	address = models.CharField(max_length=255)
	city = models.CharField(max_length=50)
	state = models.CharField(max_length=50)
	phone = models.IntegerField()
	qoute = models.CharField(max_length=255)
	description = models.TextField()
	computer_seats = models.IntegerField()
	computer_cutoff = models.FloatField()	
	IT_seats = models.IntegerField()
	IT_cutoff = models.FloatField()
	civil_seats = models.IntegerField()
	civil_cutoff = models.FloatField()
	mechanical_seats = models.IntegerField()
	mechanical_cutoff = models.FloatField()
	electrical_seats = models.IntegerField()
	electrical_cutoff = models.FloatField()

class Student_info(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	photo = models.ImageField(upload_to='college_part/student')
	phone = models.IntegerField()
	school = models.CharField(max_length=100)
	physics_mark = models.FloatField()
	chemistry_mark = models.FloatField()
	maths_mark = models.FloatField()
	gcet_jee_mark = models.FloatField()

class Student_Merit_Score(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	merit_score = models.FloatField()