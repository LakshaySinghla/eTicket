from django.shortcuts import render
from django.http import HttpResponse
from Buy.models import Match
from . import forms

# Create your views here.

def index(request):
	all_matches = {'matches': Match.objects.all() }
	return render(request,'Buy/index.html',all_matches)
	# return HttpResponse("Hello World")

def match1(request):
	return render(request,'Buy/match1.html',{})

def match2(request):
	return render(request,'Buy/match2.html',{})

def SignupFormView(request):
	form = forms.SignupForm()

	if request.method == 'POST':
		form = forms.SignupForm(request.POST)

		if form.is_valid():
			# DO SOMETHING CODE
			print("VALIDATION SUCCESS!")
			print("NAME: "+form.cleaned_data['name'])
			print("EMAIL: "+form.cleaned_data['email'])
			print("PASSWORD: "+form.cleaned_data['password'])

	return render(request,'Buy/signup.html',{'form':form})

def LoginFormView(request):
	form = forms.LoginForm()
	return render(request, 'Buy/login.html',{'form':form})