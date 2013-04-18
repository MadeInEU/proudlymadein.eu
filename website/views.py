from django.shortcuts import render_to_response, render, get_object_or_404, redirect
from django.http import HttpResponse

def home(request):
	return render_to_response('home.html')
