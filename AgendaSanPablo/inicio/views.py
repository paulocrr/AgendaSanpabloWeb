from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.core.serializers.json import DjangoJSONEncoder
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

def getSpecificCursos(request, ciclo, carrera):
	cursor = connection.cursor()
	cursor.execute('''SELECT * FROM tcursos WHERE ciclo=''' + ciclo+ ''' AND carrera ='''+carrera)
	data = cursor.fetchall()
	cursor.close()
	return HttpResponse(json.dumps(data), content_type='application/json')

def getCursosPersonales(request):
	cursor = connection.cursor()
	idUser = request.session['idUser'];
	cursor.execute('''SELECT DISTINCT tcursos.id,nombre FROM thorarios JOIN tcursos ON tcursos.id=thorarios.id_curso AND thorarios.id_usuario=%s''',[idUser])
	data = cursor.fetchall()
	cursor.close()
	return HttpResponse(json.dumps(data), content_type='application/json')

def tareas(request):
	template = loader.get_template('tareas.html')
	context = {}
	return HttpResponse(template.render(context, request))

def agregarTarea(request):
	template = loader.get_template('agregarTarea.html')
	context = {}
	return HttpResponse(template.render(context, request))

def getCursosPorDia(request):
	idDia = request.POST.get('id_dia');
	idUser = request.session['idUser'];
	cursor = connection.cursor()
	cursor.execute('''SELECT thorarios.id,nombre,dia,hora_inicio,hora_fin FROM thorarios JOIN tcursos ON tcursos.id=thorarios.id_curso JOIN tdia ON tdia.id=thorarios.id_curso AND thorarios.id_dia=%s AND thorarios.id_usuario=%s''',[idDia,idUser])
	data = cursor.fetchall()
	cursor.close()
	return HttpResponse(json.dumps(data), content_type='application/json')
def datetime_handler(x):
	if isinstance(x, datetime.datetime):
	    return x.isoformat()
	raise TypeError("Unknown type")
def getTareas(request):
	idUser = request.session['idUser']
	cursor = connection.cursor()
	cursor.execute('''SELECT tareas.id,tarea,fecha,tcursos.nombre FROM tareas JOIN tcursos on tcursos.id=tareas.id_curso AND id_usuario=%s''',[idUser])
	data = cursor.fetchall()
	cursor.close()
	return HttpResponse(json.dumps(data), content_type='application/json')

def borrarHorario(request, id):
	cursor = connection.cursor()
	cursor.execute('''DELETE FROM thorarios WHERE id='''+id)
	return HttpResponseRedirect("/inicio/horario/")
	
def borrarTarea(request, id):
	cursor = connection.cursor()
	cursor.execute('''DELETE FROM tareas WHERE id='''+id)
	return HttpResponseRedirect("/inicio/tareas/")

def getCursos(request):
	cursor = connection.cursor()
	cursor.execute('''SELECT * FROM tcursos WHERE ciclo=1 AND carrera =1''')
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
def insertTarea(request):
	if request.method == "POST":
		cursor = connection.cursor()
		idUsuario = request.session['idUser']
		idCurso = request.POST.get('curso',2)
		fecha = request.POST.get('fecha')
		tarea = request.POST.get('textarea1')
		cursor.execute('''INSERT INTO `agendadb`.`tareas`(`id_curso`,`tarea`,`fecha`,`id_usuario`)VALUES(%s,%s,%s,%s);''',[idCurso,tarea,fecha,idUsuario])
	return HttpResponseRedirect("/inicio/tareas/")

def calc_notas(request):
	template = loader.get_template('calc_notas.html')
	context = {}
	return HttpResponse(template.render(context,request))
