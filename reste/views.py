from django.shortcuts import render,redirect
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth import logout,authenticate
from django.contrib.auth import login as user_login
from django.contrib.auth.models import User


def home(request):
	return render (request,"home.html")
def login(request):

	if not request.user.is_authenticated:
		return redirect("/login/")
def signin(request):
	if request.method == "POST":
		username = request.POST.get('username', None)	
		password = request.POST.get('password', None)
		print(username, password)
		user = authenticate(request, username=username, password=password)
		print(user)
		if user is not None:
			print("Im in")
			user_login(request, user)
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

def signout(request):
	logout(request)
	return redirect("/")

def dashboard(request):
	return render(request,"dashboard.html")

def addremainders(request):
	return render(request,"addremainders.html")

def oldremainders(request):
	return render(request,"oldremainders.html")



def currentremainders(request):
	return render(request,"curentremainders.html")

# Create your views here.
