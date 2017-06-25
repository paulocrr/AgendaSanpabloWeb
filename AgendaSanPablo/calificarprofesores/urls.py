from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^$',views.index, name="listaprofes"),
	url(r'^getProfesores/$',views.listadoProfesores, name="getprofes"),
	url(r'^CalificarProfesor/$',views.formCalificarProfesores, name="calprofes"),
	url(r'^getCriterios/$',views.getCriterios, name="calprofes"),
	url(r'^actionCalificar/$',views.actionCalificar, name="calprofes"),
]