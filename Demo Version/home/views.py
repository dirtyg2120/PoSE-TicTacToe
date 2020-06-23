from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
	return render(request, 'pages/home.html')

def newsPage(request):
	return render(request, 'pages/news.html')

def downloadPage(request):
	return render(request, 'pages/downloads.html')

def aboutPage(request):
	return render(request, 'pages/aboutus.html')

def playPage(request):
	return render(request, 'pages/play.html')
