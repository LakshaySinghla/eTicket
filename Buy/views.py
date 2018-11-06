from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
	return render(request,'Buy/index.html',{})
	# return HttpResponse("Hello World")

def match1(request):
	return render(request,'Buy/match1.html',{})

def match2(request):
	return render(request,'Buy/match2.html',{})