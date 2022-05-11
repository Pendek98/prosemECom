from django.shortcuts import render     
from django.contrib.auth.models import User

# Create your views here.

def createUser(response):
	userName = request.REQUEST.get('username',None)
	userPass = request.REQUEST.get('password', None)
	userMail = request.REQUEST.get('email', None)

	user = User.objects.create_user(userName,userPass,userMail)
	user.save()
