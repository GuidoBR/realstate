from django.contrib import admin

from .models import Usuario, Endereco, Servico, Imovel, Foto, Video, Locacao, Propriedade

admin.site.register(Usuario)
admin.site.register(Endereco)
admin.site.register(Servico)
admin.site.register(Imovel)
admin.site.register(Foto)
admin.site.register(Video)
admin.site.register(Locacao)
admin.site.register(Propriedade)