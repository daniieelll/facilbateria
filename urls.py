

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from facil.views import carga_cliente_view
from facil.views import base_view
from facil.views import assistencia_view
from facil.views import Emprestimos_view
from facil.views import garantia_Seminova_view
from accounts.views import register_view
from accounts.views import  login_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('carga_clientes/',carga_cliente_view,name='carga_clientes'),
    path('assistencia/',assistencia_view, name='assistencia'),
    path('emprestimos/',Emprestimos_view, name='emprestimos'),
    path('register/',register_view, name='register'),
    path('login/',login_view, name='login'),
    path('accounts/', include('accounts.urls')),
    path('garantia_seminovas/',garantia_Seminova_view,name='garantia_seminovas'),
    path ('', base_view, name='base'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
