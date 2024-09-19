from django.contrib import admin

from .models import Cargo, Servico, Funcionario, Recurso, Assinatura, Depoimento

admin.site.site_header = "Painel de Administração"
admin.site.site_title = "Fusion"
admin.site.index_title = "Bem-vindo ao Painel de Administração da Fusion!"


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'ativo', 'modificado')


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('servico', 'icone', 'ativo', 'modificado')


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'ativo', 'modificado')


@admin.register(Recurso)
class RecursoAdmin(admin.ModelAdmin):
    list_display = ('recurso', 'icone', 'ativo', 'modificado')


@admin.register(Assinatura)
class AssinaturaAdmin(admin.ModelAdmin):
    list_display = ('assinatura', 'icone', 'ativo', 'modificado')


@admin.register(Depoimento)
class DepoimentoAdmin(admin.ModelAdmin):
    list_display = ('depoimento', 'nome', 'cargo', 'estrelas', 'ativo', 'modificado')
    list_filter = ('estrelas',)  # Permite filtrar depoimentos pela quantidade de estrelas
