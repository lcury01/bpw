# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.views.decorators.http import require_POST

from django.shortcuts import render
from forms import AssociadoForm

# Create your views here.

def home(request):
	return render(request, 'bn_app/index.html')

def rede(request):
	return render(request, 'bn_app/rede.html')

def cadrede(request):
	form	=	AssociadoForm()
	
	return render(request, 'bn_app/cadrede.html', {'form': form})

@require_POST
def cadastrar(request):
	nome_usuario	=	request.POST['campo-nome-usuario']
	email			=	request.POST['campo-email']
	senha			=	request.POST['campo-senha']
	novoUsuario = User.objects.create_user(username=nome_usuario, email=email, password=senha)
    #novoUsuario.save()	

