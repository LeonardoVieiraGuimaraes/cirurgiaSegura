from cProfile import label
from django import forms

from .models import DadosUsuario
from django.forms import ModelForm

choicesSN = [('Sim', 'Sim'), ('Sim', 'Não')]


class DadosUsuarioModelForm(ModelForm):
    modalidade = forms.ChoiceField(
        choices=choicesSN, widget=forms.RadioSelect())
    daatNascimento = forms.DateInput()

    class Meta:
        model = DadosUsuario
        fields = ['nome', 'dataNascimento', 'prontuario', 'nomeMae',
                  'cirurgiaProposta', 'cirurgiaRealizada', 'salaCirurgia', 'dataCirurugia', 'modalidade']
        # widgets = {'modalidade': forms.RadioSelect(), }

        label = {'nome': 'Nome'}

        # widgets = {
        #     'dataNascimento': DatePicker(),
        # }
