from django.forms import * 
from .models import Atividade, Sessao,Materiais,Horario,Espaco,Tema

def get_choices_time():
    return [(str(t),t) for t in range(5, 61, 5)]  

class AtividadeForm(ModelForm):
    tema = ChoiceField(choices=[(tema.id,tema.tema) for tema in Tema.objects.all()])
    duracaoesperada= ChoiceField(choices=get_choices_time())
    class Meta:  
        model = Atividade  
        exclude = ['coordenadorutilizadorid', 'professoruniversitarioutilizadorid','datasubmissao', 'dataalteracao','estado','id','diaabertoid','tema','espacoid']
        widgets = {
            'nome': TextInput(attrs={'class': 'input'}),
            'tipo': Select(),
            'descricao': Textarea(attrs={'class':'textarea'}),
            'publicoalvo': Select(),
            'nrcolaboradoresnecessario': NumberInput(attrs={'class': 'input'}),
            'duracaoesperada': NumberInput(attrs={'class': 'input'}),
            'participantesmaximo': NumberInput(attrs={'class': 'input'}),
            'duracaoesperada': Select(),
            }


class MateriaisForm(ModelForm):
    class Meta:
        model = Materiais  
        exclude = ["atividadeid"]
        widgets = {
            'nomematerial': TextInput(attrs={'class': 'input'}),
            }
