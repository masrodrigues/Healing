from django.shortcuts import redirect, render
from .models import Especialidades, DadosMedico, is_medico
from django.contrib import messages
from django.contrib.messages import constants

def cadastro_medico(request):
    
    if is_medico(request.user):
        messages.add_message(request, constants.WARNING, 'Você já é médico')
        return redirect('/medicos/abrir_horario')#vai dar erro ainda
        
        
    
    if request.method == "GET":
        especialidades = Especialidades.objects.all()
        return render(request, 'cadastro_medico.html', {'especialidades':especialidades})

    elif request.method == "POST":
        crm = request.POST.get('crm')
        nome = request.POST.get('nome')
        cep = request.POST.get('cep')
        rua = request.POST.get('rua')
        bairro = request.POST.get('bairro')
        numero = request.POST.get('numero')
        cim = request.FILES.get('cim')
        rg = request.FILES.get('rg')
        foto = request.FILES.get('foto')
        especialidade = request.POST.get('especialidade')
        descricao = request.POST.get('decricao')
        valor_consulta = request.POST.get('valor_consulta')
        
        dados_medico = DadosMedico(
            crm = crm,
            nome = nome,
            cep=cep,
            rua=rua,
            bairro=bairro,
            numero=numero,
            rg=rg,
            cedula_identidade_medica=cim,
            foto=foto,
            especialidade_id=especialidade,
            descricao=descricao,
            valor_consulta=valor_consulta,
            user=request.user
            
        )
        
        dados_medico.save()

        messages.add_message(request, constants.SUCCESS, 'Cadatro médico realizado com sucesso.')
        return redirect('/medicos/abrir_horario')# vaidar error


def abrir_horario(request):

    if not is_medico(request.user):
        messages.add_message(request, constants.WARNING, 'Somente médicos podem acessar essa página.')
        return redirect('/usuarios/sair')

    if request.method == "GET":
        dados_medicos = DadosMedico.objects.get(user=request.user)
        return render(request, 'abrir_horario.html', {'dados_medicos': dados_medicos})