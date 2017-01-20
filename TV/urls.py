"""TV URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from prueba import urls as pruebaUrls
from canales import urls as canalesUrls
from accounts import urls as accountsUrls
from main import urls as mainUrls
#Libreria para importar imagenes
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(canalesUrls, namespace="canales")),
    url(r'^', include(accountsUrls, namespace="accounts")),
    url(r'^', include(pruebaUrls, namespace="prueba")),
    url(r'^', include(mainUrls, namespace="main")),
    url(
        regex=r'^media/(?P<path>.*)$',
        view=serve,
        kwargs ={'document_root':settings.MEDIA_ROOT}
    ),
    # Python Social Auth URLs
   # url('', include('social.apps.django_app.urls', namespace='social')),
]
