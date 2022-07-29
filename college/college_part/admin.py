from django.contrib import admin
from .models import *

# Register your models here.

class College_show(admin.ModelAdmin):
	list_display = ('name', 'computer_cutoff', 'IT_cutoff', 'civil_cutoff', 'mechanical_cutoff', 'electrical_cutoff')

admin.site.register(College, College_show)

class Student_show(admin.ModelAdmin):
	list_display = ('user', 'phone', 'school')

admin.site.register(Student_info, Student_show)

class Student_Merit_show(admin.ModelAdmin):
	list_display = ('user', 'merit_score')

admin.site.register(Student_Merit_Score, Student_Merit_show)