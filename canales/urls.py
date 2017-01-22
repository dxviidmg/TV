from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^canales/(?P<slug>[-\w]+)', views.DetailViewCanal.as_view(),name="DetailViewCanal"),
	url(r'^canales', views.ListViewCanales.as_view(),name="ListViewCanales"),
]