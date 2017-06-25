from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db import connection
import json

@login_required
# Create your views here.
def index(request):
	template = loader.get_template('main.html')
	context = {}
	return HttpResponse(template.render(context,request))
def horario(request):
	template = loader.get_template('horario.html')
	context = {}
	return HttpResponse(template.render(context,request))
def agregarCurso(request):
	template = loader.get_template('agregar_horario.html');
	context = {}
	return HttpResponse(template.render(context,request));
def getDias(request):
	cursor = connection.cursor()
	cursor.execute('''SELECT * FROM tdia''')
	data = cursor.fetchall()
	cursor.close()
	return HttpResponse(json.dumps(data), content_type='application/json')
def getCursosPorDia(request):
	idDia = request.POST['id_dia'];
	idUser = request.session['idUser'];
	cursor = connection.cursor()
	cursor.execute('''SELECT thorarios.id,nombre,dia,hora_inicio,hora_fin FROM thorarios JOIN tcursos ON tcursos.id=thorarios.id_curso JOIN tdia ON tdia.id=thorarios.id_curso AND tdia.id=%s AND thorarios.id_usuario=%s''',[idDia,idUser])
	data = cursor.fetchall()
	cursor.close()
	return HttpResponse(json.dumps(data), content_type='application/json')
def getCursos(request):
	cursor = connection.cursor()
	cursor.execute('''SELECT * FROM tcursos''')
	data = cursor.fetchall()
	cursor.close()
	return HttpResponse(json.dumps(data), content_type='application/json')
def insertCurso(request):
	if request.method == "POST":
		cursor = connection.cursor()
		idCurso = request.POST.get('inp_curso',2)
		idDia = request.POST['inp_dia']
		idUsuario = request.session['idUser']
		horaInicio = request.POST['inp_horaInicio']
		horaFin = request.POST['inp_horaFin']
		#datos = [idCurso,idDia,idUsuario,horaInicio,horaFin]
		cursor.execute('''INSERT INTO `agendadb`.`thorarios`(`id_curso`,`id_dia`,`hora_inicio`,`hora_fin`,`id_usuario`)VALUES(%s,%s,%s,%s,%s);''',[idCurso,idDia,horaInicio,horaFin,idUsuario])
	return HttpResponseRedirect("/inicio/horario/")
def calc_notas(request):
	template = loader.get_template('calc_notas.html')
	context = {}
	return HttpResponse(template.render(context,request))