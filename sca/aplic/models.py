from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=30, blank=False)
    sala = models.IntegerField(blank=False)
    email = models.EmailField(max_length=100, default='seuemail@gmail.com', blank=False)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Alunos"

class Aula(models.Model):
    nome = models.CharField(max_length=30, blank=False)
    data = models.DateField()
    descricao = models.CharField(max_length=30,blank=True)


    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Aulas"

class Presenca(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    aula = models.ForeignKey(Aula, on_delete=models.CASCADE)
    faltas = models.IntegerField(blank=True)

    def __str__(self):
        return f"{self.aluno.nome} - {self.aula.nome} - Faltas: {self.faltas}"

    class Meta:
        verbose_name_plural = "Presenças"

class Certificado(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    nome_coordenador_faculdade = models.CharField(blank=False)
    nome_coordenador_colegio = models.CharField(blank=False)

    def __str__(self):
        return f"{self.nome_coordenador_faculdade}, {self.nome_coordenador_colegio}"
    class Meta:
        verbose_name_plural = "Certificados"

class Administrador(models.Model):
    nome = models.CharField(blank=False)
    senha = models.FloatField(blank=False)

    def __str__(self):
        return f"{self.nome},{self.senha}"

    class Meta:
        verbose_name_plural = "Administradores"