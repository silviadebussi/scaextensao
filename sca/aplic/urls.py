from django.urls import path
from . import views
from .views import IndexView, CertificadosView, gerar_certificado, AdministradoresView, PresencasView, AulasView, AlunosView, registrar_aluno, registrar_presenca, Sucesso_registroView, registrar_aula

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("certificados.html", CertificadosView.as_view(), name="certificados"),
    path('gerar_certificado/', gerar_certificado, name='gerar_certificado'),
    path("administradores.html", AdministradoresView.as_view(), name="administradores"),
    path("aulas.html", AulasView.as_view(), name="administradores"),
    path("alunos.html", AlunosView.as_view(), name="administradores"),
    path("presencas.html", PresencasView.as_view(), name="administradores"),
    path('registrar_aluno/', registrar_aluno, name='registrar_aluno'),
    path('registrar_presenca/', registrar_presenca, name='registrar_presenca'),
    path('sucesso_registro.html', Sucesso_registroView.as_view(), name='sucesso_registro'),
    path('registrar_aula/', registrar_aula, name='registrar_aula'),
    path("aulas.html", AulasView.as_view(), name="aulas"),
]