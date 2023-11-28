from django.views.generic.edit import CreateView
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import FileResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import AlunoForm 
from .models import Aluno 
from .forms import PresencaForm
from .models import Aula
from .forms import AulaForm
from django.urls import reverse
from django.shortcuts import render, redirect
from io import BytesIO
from reportlab.lib import colors


class IndexView(TemplateView):
    template_name = 'index.html'

class CertificadosView(TemplateView):
    template_name = 'certificados.html'

class AdministradoresView(TemplateView):
    template_name = 'administradores.html'

class AulasView(TemplateView):
    template_name = 'aulas.html'

class AlunosView(TemplateView):
    template_name = 'alunos.html'

class PresencasView(TemplateView):
    template_name = 'presencas.html'

class Sucesso_registroView(TemplateView):
    template_name = 'sucesso_registro.html'

class SobreView(TemplateView):
    template_name = 'sobre.html'

def gerar_certificado(request):
    buffer = BytesIO()

    p = canvas.Canvas(buffer, pagesize=letter)
    p.setFont("Helvetica-Bold", 30) 
    p.setLineWidth(8) 

    
    p.drawString(100, 750, "Certificado de Conclusão")
    p.setFont("Helvetica-Bold", 18)  
    p.drawString(150, 715, "Curso de TI Básico")
    p.setFont("Helvetica", 15) 
    p.drawString(100, 530, f"Nome do Aluno: {request.GET.get('nomeAluno')}")
    p.drawString(100, 510, f"Nome do Curso: {request.GET.get('nomeCurso')}")
    p.drawString(100, 490, f"Data de Conclusão: {request.GET.get('dataConclusao')}")
    p.drawString(100, 470, f"Coordenador(a) do Colégio: {request.GET.get('coordenadorColegio')}")
    p.drawString(100, 450, f"Coordenador(a) da Faculdade: {request.GET.get('coordenadorFaculdade')}")
    p.drawString(100, 230, "Certificamos que o aluno concluiu o curso com sucesso.")

    p.showPage()
    p.save()

    buffer.seek(0)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="certificado.pdf"'
    response.write(buffer.read())
    return response
def registrar_aluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            novo_aluno = form.save()
            return redirect('sucesso_registro')
    
    else:
        form = AlunoForm()
    
    return render(request, 'alunos.html', {'form': form})
    
  


def registrar_presenca(request):
    if request.method == 'POST':
        form = PresencaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sucesso_registro')
    

    else:
       form = PresencaForm()

    return render(request, 'presencas.html', {'form': form})
    return redirect('sucesso_registro')

def registrar_aula(request):
    if request.method == 'POST':
        form = AulaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registrar_aula')
    else:
        form = AulaForm()

    aulas = Aula.objects.all()
    return render(request, 'aulas.html', {'form': form, 'aulas': aulas})
   