from django.contrib import admin

from .models import Aluno, Aula, Presenca, Certificado, Administrador

admin.site.register(Aluno)
admin.site.register(Aula)
admin.site.register(Presenca)
admin.site.register(Administrador)