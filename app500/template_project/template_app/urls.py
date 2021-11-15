from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required

from . import views
from . import soap

urlpatterns = [
	path('', views.login_index, name="login"),
	path('logout', views.logout_index, name="logout"),
	path('registrarse', views.registrarse, name="register"),
	path('home', views.template_view, name="home"),
	path('soap', soap.consulta(), name="soap"),
	path('banca', views.banca, name="banca"),
    #path('', views.VistaPrecioDolar.as_view(template_name ='index.html'), name = 'vistapreciodolar'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)