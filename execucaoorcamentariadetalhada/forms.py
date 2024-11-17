# forms.py
from django import forms

from .models import EtapaCredito, UGResponsavel

class ExecucaoFilterForm(forms.Form):
    
    ugResponsavel = forms.ModelChoiceField(
        required=False,
        label='PesquiUG Responsável',
        queryset=UGResponsavel.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    
    etapaCredito = forms.ModelChoiceField(
        required=False,
        label='Etapa Crédito',
        queryset=EtapaCredito.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select'})
    )
