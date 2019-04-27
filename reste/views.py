from django.shortcuts import render,redirect
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth import login as user_login
from django.contrib.auth.models import User
from datetime import timedelta
import datetime
from reste.models import *
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required





def home(request):
	return render (request,"home.html")



def signin(request):
	if request.method == "POST":
		username = request.POST.get('username', None)	
		password = request.POST.get('password', None)
		print(username, password)
		user = authenticate(request, username=username, password=password)
		print(user)
		if user is not None:
			print("Im in")
			login(request,user)
			return redirect("/dashboard/")
	return render(request, "signin.html")


def signup(request):

	if request.method == "POST":
		fullname = request.POST.get('fullname', None)	
		email = request.POST.get('email', None)	
		username = request.POST.get('username', None)	
		password = request.POST.get('password', None)	
		print(password)
		
		user_exists = User.objects.filter(username=username).exists()
		if not user_exists:
			user = User.objects.create_user(
				username = username,
				password = password,
				email = email,
				first_name = fullname.split()[0],
				last_name = " ".join(fullname.split()[1:])
			)
			user_login(request,user)
			return redirect("/dashboard")
		else:
			return HttpResponse("User already exists. Try new username.")

	return render(request, "signup.html")


@login_required(login_url='/login/')
def signout(request):
	logout(request)
	return redirect("/")


@login_required(login_url='/login/')
def dashboard(request):
	return render(request,"dashboard.html")

@login_required(login_url='/login/')
def addremainders(request):
	if request.method == "POST":
		name = request.POST['NAME']
		description = request.POST['DESCRIPTION']
		date = request.POST['DATE']
		remainder = Remainders.objects.create(name=name,
			description=description,
			date=date,
			author=request.user
			)
		email(request,date)
		return redirect('/dashboard/')
	else:
		
		return render(request,"addremainders.html")


@login_required(login_url='/login/')
def oldremainders(request):
	return render(request,"oldremainders.html")


@login_required(login_url='/login/')
def currentremainders(request):

	today = datetime.date.today()
	user = User.objects.get(username=request.user)
	reminders = Remainders.objects.filter(author=user)
	
	return render(request,"currentremainders.html",{"reminders":reminders, "today":today})

# Create your views here.


@login_required(login_url='/login')
def email(request,date):
    subject = 'A Remainder Mail'
    message = f'Your remainder is set to {date}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [request.user.email]
    send_mail( subject, message, email_from, recipient_list )
    return 