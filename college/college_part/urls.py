from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
 	path('', views.index),
 	path('about/', views.about),
 	path('services/', views.service),
 	path('colleges/', views.college),
 	path('login/', views.signin),
 	path('logout/', views.signout),
 	path('merit/', views.merit),
 	path('view/<int:myid>/', views.show_college),
 	path('computer/', views.computer),
 	path('information/', views.information),
 	path('civil/', views.civil),
 	path('mechanical/', views.mechanical),
 	path('electrical/', views.electrical),
]