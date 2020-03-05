from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth 
from django.contrib import messages
# Create your views here.

def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = auth.authenticate(username = username, password = password)

		if user is not None:
			auth.login(request, user)
			return redirect("/")
		else:
			messages.info(request, 'invalid credentials')
			return redirect('login')

	else:
		return render(request, 'login.html')

def logout(request):
	auth.logout(request)
	return redirect('/')

def register(request):

	if request.method == 'POST':
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		username = request.POST['username']
		email = request.POST['email']
		if request.POST['password1'] == request.POST['password2']:
			if User.objects.filter(username = username).exists():
				messages.info(request,'Username already taken')
				return redirect('register')
			elif User.objects.filter(email = email).exists():
				messages.info(request, 'Email already taken')
				return redirect('register')
			password = request.POST['password1']
			user = User.objects.create_user(username =  username, password = password, email = email,
		 		first_name = first_name, last_name = last_name)
			user.save()
			print('User created')
			return redirect('login')
		else:
			print('Passwords dont match')
			return redirect('register')
		return redirect('/')
	
	else:
		return render(request,'register.html')