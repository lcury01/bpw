from django import forms

from .models import Associado

class	AssociadoForm(forms.ModelForm):
	class	Meta:
		model	=	Associado
		fields	=	('nome','email','enderecop', 'cidadep', 'estadop', 'cepp', 'telefonep', 'celularp', 'skypep', 'BPWassociada', 'tipo',
			'razaosocial', 'nomefantasia', 'enderecoe', 'cidadee', 'estadoe', 'cepe', 'telefonee', 'emaile', 'site', 'dtfundacao',
			'descricao', 'cotas', 'funcionarios', 'exportatempo', 'principalpais', 'liberainfs', 'segmentotemp', 'certificacaotemp')
		
