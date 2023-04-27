from django.shortcuts import render
from django.http import HttpResponse, request
from django.shortcuts import render
from .models import AddMail

# Create your views here.
def index(request):
	return render(request, "home.html")

def about(request):
	return render(request, "about.html")

def contact(request):
	if request.method == 'POST':
		email = request.POST['address']
		newMail = AddMail(email=email)
		newMail.save()
	return render(request, "contact.html")

def home(request):
	return render(request, "home.html")
