from django.shortcuts import render
from django.http import HttpResponse

def chatIndex(request):
	return render(request, 'chat/chat_index.html')
	