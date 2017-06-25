from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^$',views.index, name="index"),
	url(r'^login/$',views.Login),
	url(r'^logout/$',views.Logout),
	url(r'^registro/$', views.registration, name="registro"),
	url(r'^registrar/$', views.registrar, name="registrar"),
	url(r'^success/$', views.success, name="success"),
]