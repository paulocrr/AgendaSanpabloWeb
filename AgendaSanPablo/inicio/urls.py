from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^$',views.index, name="index"),
	url(r'^horario/$', views.horario, name="horario"),
	url(r'^agregarHorario/$', views.agregarCurso, name="agregarCurso"),
	url(r'^calc_notas/$', views.calc_notas, name="calc_notas"),
	url(r'^getCursos/$', views.getCursos, name="getCursos"),
	url(r'^getDias/$', views.getDias, name="getDias"),
	url(r'^insertCurso/$', views.insertCurso, name="insertCurso"),
	url(r'^getCursosPorDia/$', views.getCursosPorDia, name="getCursosPorDia"),
	url(r'^getSpecificCursos/(?P<ciclo>[0-9]+)/(?P<carrera>[0-9]+)/$',views.getSpecificCursos, name = 'getSpecificCursos'),
]
 	
