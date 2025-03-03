from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=100, default='Nome Padrão')
    rg = models.CharField(max_length=9)
    cpf = models.CharField(max_length=11)
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome

class Curso(models.Model):
    NIVEL = (
        ('B', 'Básico'),
        ('I', 'Intermediário'),
        ('A', 'Avançado'),
    )
    
    codigo_curso= models.CharField(max_length=10) #charfield serve para armazenar uma string em django
    descricao= models.CharField(max_length=1002)
    nivel = models.CharField(max_length=1, choices= NIVEL, blank= False, null=False, default= 'B')

class Matricula(models.Model):
        PERIODO = (
                ('M', 'Matutino'),
                ('V', 'Vespertino'),
                ('N', 'Noturno'),
        )
        aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE) #ForeignKey 'tabela' que vai passar CASCADE, quando o aluno for deletado a matricula deleta
        curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
        periodo = models.CharField(max_length=1, choices=PERIODO, blank=False, null=False, default='M')