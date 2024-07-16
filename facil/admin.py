from django.contrib import admin
from facil.models import Carga_clientes, Assistencia, Emprestimos, Seminova

class Carga_clientesAdmin(admin.ModelAdmin):
    list_display = ('bateria', 'numeracao_bateria', 'contato', 'valor', 'cliente', 'responsavel')
    search_fields = ('cliente',)


class assistenciaAdmin(admin.ModelAdmin):
    list_display = ('bateria','numeracao_bateria','contato','cliente','responsavel','foto')
    search_fields = ('cliente',)


class emprestimoAdmin(admin.ModelAdmin):
    list_display = ('cliente','parceiro','bateria','quantidade','data','numeracao_bateria','foto','responsavel')
    search_fields = ('cliente',)


class SeminovaAdmin(admin.ModelAdmin):
    list_display = ('bateria','numeracao_bateria','contato','cliente','responsavel','data_venda','garantia','foto')
    search_fields = ('cliente',)



admin.site.register(Carga_clientes, Carga_clientesAdmin)
admin.site.register(Assistencia, assistenciaAdmin)
admin.site.register(Emprestimos, emprestimoAdmin)
admin.site.register(Seminova, SeminovaAdmin)