from django.contrib import admin
from empresa.models import Funcionario

class Funcionarios(admin.ModelAdmin):
    list_display = ('id', 'nome', 'rg')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)

admin.site.register(Funcionario, Funcionarios)
