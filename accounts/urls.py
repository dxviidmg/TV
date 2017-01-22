from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout, password_reset, password_reset_done

#	 django.contrib.auth.views.  password_reset_done
urlpatterns = [
	
	url(r'^logout/$', logout, name="logout"),
	url(r'^login', login, name="login"),
	url(r'^accounts/profile/$', views.ViewProfile.as_view(), name="ViewProfile"),

	url(r'^accounts/nuevo/$', views.CreateViewAccount.as_view(), name="CreateViewAccount"),
#	url(r'^accounts/actualizar/(?P<pk>\d+)/$', views.UpdateViewAccount.as_view(), name="UpdateViewAccount"),
#	url(r'^accounts/eliminar/(?P<pk>\d+)/$', views.DeleteViewAccount.as_view(), name="DeleteViewAccount"),
#	url(r'^accounts/(?P<pk>\d+)/$', views.DetailViewAccount.as_view(), name="DetailViewAccount"),
#	url(r'^accounts', views.ListViewAccounts.as_view(),name="ListViewAccounts"),
	
	url(r'^change-password/$', views.ViewChangePassword.as_view(), name='ViewChangePassword'),
#	url(r'^reset-password/$', password_reset, name='reset_password'),

#	url(r'^reset-password/done/$', password_reset_done, name='password_reset_done'),
]