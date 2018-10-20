# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Associado(models.Model):
	ESTADO = (
		('AC', 'Acre'),
		('AL', 'Alagoas'),
		('AP', 'Amapa'),
		('AM', 'Amazonas'),
		('BA', 'Bahia'),
		('CE', 'Ceará'),
		('DF', 'Distrito Federal'),
		('ES', 'Espirito Santo'),
		('GO', 'Goiás'),
		('MA', 'Maranhão'),
		('MT', 'Mato Grosso'), 
		('MS', 'Mato Grosso do Sul'),
		('MG', 'Minas Gerais'),
		('PA', 'Pará'),
		('PB', 'Paraiba'),
		('PE', 'Pernambuco'),
		('PI', 'Piauí'),
		('RJ', 'Rio de Janeiro'),
		('RN', 'Rio Grande do Norte'),
		('RS', 'Rio Grande do Sul'),
		('RO', 'Rondônia'),
		('RR', 'Roraima'),
		('SC', 'Santa Catarina'),
		('SP', 'São Paulo'),
		('SE', 'Sergipe'),
		('TO', 'Tocantins')
	)  

	TIPO = (
		('L', 'Profisssional Liberal'),
		('J', 'Pessoa Juridica')
	)

	BPW = (
		(1,'Brasilia'),
		(2,'Bento Goncalves'),
		(3,'Caçador'),
		(4,'Cuiabá'),
		(5,'Curitiba'),
		(6,'Florianopolis'),
		(7,'Fortaleza'),
		(8,'Porto Alegre'),
		(9,'Presidente Prudente'),
		(10,'Rio de Janeiro'),
		(11,'Florianopolis')
	)

 	nome = models.CharField(max_length=100,verbose_name="Seu Nome: ", help_text="Informe seu nome Completo")
	email= models.EmailField(max_length=100, verbose_name="Seu e-mail: ", help_text="Informe um e-mail que você sempre acessa")
	enderecop = models.CharField(max_length=100, verbose_name="Seu endereço: ", help_text="Informe seu endereço de correspondência")
	cidadep = models.CharField(max_length=100, verbose_name="Cidade: ", help_text="Cidade")
	estadop = models.CharField(max_length=2, choices=ESTADO, verbose_name="Estado: ", help_text="Estado")
	cepp = models.CharField(max_length=9, verbose_name="CEP: ", help_text="CEP")
	telefonep = models.CharField(max_length=11,verbose_name="Telefone: ",help_text="Telefone Fixo Pessoal")
	celularp = models.CharField(max_length=11,verbose_name="Celular: ", help_text="Celular Pessoal")
	skypep = models.CharField(max_length=20,verbose_name="Skype: ", help_text="Skype Pessoal")
	BPWassociada = models.CharField(max_length=2, choices=BPW,verbose_name="A qual BPW você é aasociada? ",help_text="Se a sua BPW não estiver na lista, entre em contato")	
	tipo 	=	models.CharField(max_length=1, choices = TIPO,verbose_name="Tipo: ", help_text="")
	razaosocial = models.CharField(max_length=100,verbose_name="Razão Social da Empresa: ",help_text="Informe a razão social de uma empresa onde você seja a sócia majoritária")
	nomefantasia = models.CharField(max_length=100,verbose_name="Nome Fantasia: ")
	enderecoe = models.CharField(max_length=100,verbose_name="Endereço: ", help_text="Endereço da Empresa")
	cidadee = models.CharField(max_length=100, verbose_name="Cidade: ", help_text="")
	estadoe = models.CharField(max_length=2, choices=ESTADO,verbose_name="Estado: ")
	cepe = models.CharField(max_length=9,verbose_name="CEP", help_text="")
	telefonee = models.CharField(max_length=11,verbose_name="Telefone: ", help_text="Telefone principal da empresa")
	emaile = models.EmailField(max_length=100, verbose_name="e-mail profissional: ",help_text="e-mail para contato de outras associadas")
	site = models.CharField(max_length=100,verbose_name="Site: ",help_text="Site Sorporativo")	
	dtfundacao = models.DateField(verbose_name="Fundação")
	descricao = models.CharField(max_length=100,verbose_name="Principais Atividades",)	
	cotas = models.CharField(max_length=2,verbose_name="Sua participação no quadro societário é: ", help_text="% quue representa a sua participação no quadro societário")	
	funcionarios = models.PositiveIntegerField(max_length=2,verbose_name="Funcionários: ",help_text="quantos funcioários tem a empresa atualmente")	
	exportatempo = models.PositiveIntegerField(max_length=3,verbose_name="Em anos, qual a sua experiência com exportação? ",help_text="Preencha com 0 se você não tem experiência com exportação")	
	principalpais = models.CharField(max_length=100,verbose_name="Pais(es) para onde exporta: ")	
	liberainfs = models.BooleanField(max_length=100,verbose_name="Autorizo a divulgação dos dados da empresa para outras associadas ",help_text="Não divulgamos dados pessoais. Divulganos somente dados relacionados a empresas associadas ao Business Net.")	
	segmentotemp = models.CharField(max_length=100, verbose_name="Segmento de negócio: ")
	certificacaotemp = models.CharField(max_length=100,verbose_name="Certificações da empresa: ")


#pais
#descricao

#certificacao
#descricao

#empresasegmento
#empresaid
#segmentoid

#empresaexporta
#empresaid
#paisid

#empresacertificacao
#empresaid
#certificacaoid


#empresaarquivo
#empresaid
#tipo
#arquivo

