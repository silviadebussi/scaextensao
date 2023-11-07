from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=30, blank=False)
    sala = models.IntegerField(blank=False)
    email = models.EmailField(max_length=100, default='seuemail@gmail.com', blank=False)

    def __str__(self):
        return self.nome

class Aula(models.Model):
    nome = models.CharField(max_length=30, blank=False)
    data = models.DateField()

    def __str__(self):
        return self.nome

class Presenca(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    aula = models.ForeignKey(Aula, on_delete=models.CASCADE)
    faltas = models.IntegerField(blank=True)

    def __str__(self):
        return f"{self.aluno.nome} - {self.aula.nome} - Faltas: {self.faltas}"

class Certificado(Aluno):
    nome_coordenador_faculdade = models.CharField(blank = False)
    nome_coordenador_colegio = models.CharField( blank = False)
    nome_aula = models.ForeignKey('Aula',on_delete = models.CASCADE)

    def __str__(self):
        return f"{self.nome_coordenador_faculdade}, {nome_coordenador_colegio}"

class Administrador(models.Model):
    nome = models.CharField(blank = False)
    senha = models.FloatField( blank = False )

    def __str__(self):
        return f"{self.nome},{self.senha}"







# Create your models here.
