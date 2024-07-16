from django.contrib import admin
from .models import CargaClientes, Assistencia, GarantiaSeminova, Cliente

class CargaClientesAdmin(admin.ModelAdmin):
    list_display = ('bateria', 'numeracao', 'contato', 'valor', 'cliente', 'responsavel')

admin.site.register(CargaClientes, CargaClientesAdmin)
admin.site.register(Assistencia)
admin.site.register(GarantiaSeminova)
admin.site.register(Cliente)
