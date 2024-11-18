# forms.py
from django import forms

from .models import MesLancamento, UGResponsavel, EtapaCredito

class ExecucaoFilterForm(forms.Form):

    mesLancamento = forms.ModelChoiceField(
        required=True,
        label='Mês Lançamento',
        queryset=MesLancamento.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    ugResponsavel = forms.ModelChoiceField(
        required=False,
        label='UG Responsável',
        queryset=UGResponsavel.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    etapaCredito = forms.ModelChoiceField(
        required=False,
        label='Etapa Crédito',
        queryset=EtapaCredito.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
