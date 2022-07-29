from django.shortcuts import render, redirect
from django.contrib import auth
from . models import *

# Create your views here.

def index(request):
	try:
		m = Student_Merit_Score.objects.filter(user=request.user)
		sc = m[0].merit_score
	except:
		sc = "None"
	return render(request, 'index.html', {
		'score' : sc 
		})

def about(request):
	try:
		m = Student_Merit_Score.objects.filter(user=request.user)
		sc = m[0].merit_score
	except:
		sc = "None"
	return render(request, 'about.html', {'score' : sc})

def service(request):
	try:
		m = Student_Merit_Score.objects.filter(user=request.user)
		sc = m[0].merit_score
	except:
		sc = "None"
	return render(request, 'services.html', {'score' : sc})

def college(request):
	col = College.objects.all()
	try:
		m = Student_Merit_Score.objects.filter(user=request.user)
		sc = m[0].merit_score
	except:
		sc = "None"
	return render(request, 'colleges.html', {
		'college' : col,
		'score' : sc,
		})

def signin(request):
	if request.method == "POST":
		user = auth.authenticate(username=request.POST['uname'], password=request.POST['pass'])
		if user is not None:
			auth.login(request, user)
			return redirect('/')
	return render(request, 'login.html')

def signout(request):
	auth.logout(request)
	return redirect('/login/')

def merit(request):
	myuser = Student_info.objects.filter(user = request.user)
	pcm = (myuser[0].physics_mark + myuser[0].chemistry_mark + myuser[0].maths_mark) / 3 
	pcm_per = (pcm * 60) / 100
	g_jee_per = (myuser[0].gcet_jee_mark * 40) / 100
	merit = pcm_per + g_jee_per

	myscore = Student_Merit_Score(user = request.user, merit_score = merit)
	myscore.save()
	return redirect('/')

def show_college(request, myid):
	c = College.objects.filter(id=myid)
	try:
		m = Student_Merit_Score.objects.filter(user=request.user)
		sc = m[0].merit_score
	except:
		sc = "None"
	return render(request, 'view.html', {
		'col' : c[0],
		'score' : sc,
		})

def computer(request):
	c = College.objects.all()
	m = Student_Merit_Score.objects.filter(user=request.user)
	try:
		sc = m[0].merit_score
	except:
		sc = "None"
	return render(request, 'computer.html', {
		'col' : c,
		'score' : sc,
		})

def information(request):
	c = College.objects.all()
	m = Student_Merit_Score.objects.filter(user=request.user)
	try:
		sc = m[0].merit_score
	except:
		sc = "None"
	return render(request, 'information.html', {
		'col' : c,
		'score' : sc,
		})

def civil(request):
	c = College.objects.all()
	m = Student_Merit_Score.objects.filter(user=request.user)
	try:
		sc = m[0].merit_score
	except:
		sc = "None"
	return render(request, 'civil.html', {
		'col' : c,
		'score' : sc,
		})

def mechanical(request):
	c = College.objects.all()
	m = Student_Merit_Score.objects.filter(user=request.user)
	try:
		sc = m[0].merit_score
	except:
		sc = "None"
	return render(request, 'mechanical.html', {
		'col' : c,
		'score' : sc,
		})

def electrical(request):
	c = College.objects.all()
	m = Student_Merit_Score.objects.filter(user=request.user)
	try:
		sc = m[0].merit_score
	except:
		sc = "None"
	return render(request, 'electrical.html', {
		'col' : c,
		'score' : sc,
		})
