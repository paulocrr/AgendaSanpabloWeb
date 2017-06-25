from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.template import loader

from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import UserForm
from django.contrib.auth.models import User
from django import forms
import json

def index(request):
	template = loader.get_template('index.html')
	context = {}
	return HttpResponse(template.render(context,request))

def Login(request):
	next = request.GET.get('next','/inicio/')
	if request.method == "POST":
		username = request.POST['inp_usuario'];
		password = request.POST['inp_pass'];
		user = authenticate(username=username,password=password)

		if user is not None:
			if user.is_active:
				request.session['idUser'] = user.id
				request.session['userNombre']=user.first_name
				login(request,user)
				return HttpResponseRedirect(next)
			else:
				HttpResponse("Usuario Inactivo")
		else:
			return HttpResponseRedirect("/")
	return render(request,"index.html",{'redirect_to':next})
# Create your views here.
def Logout(request):
	logout(request)
	return HttpResponseRedirect("/")
def registration(request):
	template = loader.get_template('registro.html')
	context = {}
	return HttpResponse(template.render(context,request))
def registrar(request):
	nombre = request.POST.get('first_name','')
	apellido = request.POST.get('last_name','')
	username = request.POST.get('username','')
	password = request.POST.get('password','')
	email = request.POST.get('email','')
	user = User.objects.create_user(username, email, password)
	user.first_name = nombre
	user.last_name = apellido
	user.save()
	return HttpResponseRedirect("/success/")
def success(request):
	template = loader.get_template('exito.html')
	context = {}
	return HttpResponse(template.render(context,request))


