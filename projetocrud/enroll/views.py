from django.shortcuts import render, HttpResponseRedirect
from .forms import CadastroEstudante
from .forms import AtualizarCadastroEstudante
from .models import Usuario
# Create your views here.


def adicionar_mostrar(req):
    if req.method == 'POST':
        fm = CadastroEstudante(req.POST)
        if fm.is_valid():
            cod = fm.cleaned_data['codigo']
            nme = fm.cleaned_data['nome']
            eml = fm.cleaned_data['email']
            crs = fm.cleaned_data['curso']
            sen = fm.cleaned_data['senha']
            reg = Usuario(codigo=cod, nome=nme, email=eml, curso= crs, senha=sen)
            reg.save()
            fm = CadastroEstudante()
    else:
        fm = CadastroEstudante()
    estudante = Usuario.objects.all()
    
    return render(req, 'enroll/adicionarEMostrar.html', {'form':fm, 'estudante':estudante})


def atualizar_dados(req, codigo):
    pi = Usuario.objects.get(codigo=codigo)
    fm = AtualizarCadastroEstudante(instance=pi)
    if req.method == 'POST':
        fm = AtualizarCadastroEstudante(req.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/');
        else:
            return handler_erros_formulario(req, fm)
    return render(req, 'enroll/atualizarEstudante.html', {'form':fm})



def deletar_usuario(req, codigo):
    if req.method == "POST":
        pi = Usuario.objects.get(codigo=codigo)
        pi.delete()
        return HttpResponseRedirect('/')
    
def handler_erros_formulario(req, form):
    if form.errors:
        return HttpResponseRedirect('/')
    else:
         return render(req, 'enroll/atualizarEstudante.html', {'form': form})

