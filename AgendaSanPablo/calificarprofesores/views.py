from django.shortcuts import render
from django.db import connection
from django.core import serializers
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.template import loader
import json
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
	template = loader.get_template('calificarProfesores.html')
	context = {}
	return HttpResponse(template.render(context,request))
def listadoProfesores(request):
	cursor = connection.cursor()
	cursor.execute('''SELECT p.nombre,p.apellido,CAST(SUM(cp.nota)/(SELECT COUNT(*) FROM tcriterios_profesores cpp WHERE cpp.id_profesor=p.id)*1 as UNSIGNED) as nota_final, (SELECT COUNT(*) FROM tcriterios_profesores cpp WHERE cpp.id_profesor=p.id) as num_votos,p.id FROM tprofesores p JOIN tcriterios_profesores cp ON p.id=cp.id_profesor  group by p.id''')
	data = cursor.fetchall()
	return HttpResponse(json.dumps(data), content_type='application/json')
def getCriterios(request):
	cursor = connection.cursor()
	cursor.execute('''SELECT * FROM tcriterios''')
	data = cursor.fetchall()
	return HttpResponse(json.dumps(data), content_type='application/json')
def formCalificarProfesores(request):
	idp = request.GET.get('id', None)
	nombre = request.GET.get('nom', None)
	apellido = request.GET.get('ap', None)
	template = loader.get_template('formCalificarProfesores.html')
	context = {'id':idp,'nom':nombre,'app':apellido}
	return HttpResponse(template.render(context,request))
def actionCalificar(request):
	if request.method == "POST":
		cursor = connection.cursor()
		idp = request.POST['idProf']
		notas = [request.POST['0'],request.POST['1'],request.POST['2'],request.POST['3']]
		for i in range(1,5):
			cursor.execute('''INSERT INTO tcriterios_profesores(nota,id_profesor,id_criterio) VALUES (%s,%s,%s)''',[notas[i-1],idp,i])
	return HttpResponseRedirect("/calProfesores/")



# Create your views here.
