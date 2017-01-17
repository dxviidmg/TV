from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^prueba', views.Home.as_view(),name="home"),
]