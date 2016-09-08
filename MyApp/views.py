from django.shortcuts import render
from .models import Text
from django.http import HttpResponse, HttpResponseRedirect
import json


# Create your views here.
def home(request):
	return render(request, 'home.html')

def view_texts(request):
	return render(request, 'view_texts.html', {'text_list': Text.objects.all()})
	
def create_text(request):
	return render(request, 'create_text.html')

def post_text(request):
	text = request.POST['text']
	text_obj = Text(text=text)
	text_obj.save()
	return HttpResponseRedirect("/home/")
	
def redirect_to_home(request):
	return HttpResponseRedirect("/home/")
