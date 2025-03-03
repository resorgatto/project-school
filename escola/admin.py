from django.contrib import admin
from escola.models import Aluno, Curso, Matricula

class Alunos(admin.ModelAdmin): #admin de todos models
    list_display = ('id', 'nome', 'rg', 'cpf', 'data_nascimento')
    list_display_links = ('id','nome')
    search_fields = ('nome',)
    list_per_page = 20 #para não passar todos alunos em uma única página
    
admin.site.register(Aluno, Alunos)

class Cursos(admin.ModelAdmin):
    list_display = ('id', 'codigo_curso', 'descricao')
    list_display_links = ('id', 'codigo_curso')
    search_fields = ['codigo_curso']
    
admin.site.register(Curso, Cursos)


class Matriculas(admin.ModelAdmin):
        list_display = ('id', 'aluno', 'curso', 'periodo')
        list_display_links = ('id')
        
admin.site.register(Matricula, Matriculas)