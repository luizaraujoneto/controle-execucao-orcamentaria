from django.shortcuts import render, get_object_or_404

from django_tables2 import SingleTableMixin, RequestConfig
from django_filters.views import FilterView
from .forms import ExecucaoFilterForm


from .models import ExecucaoDetalhada, ExecucaoDetalhadaTable

# Create your views here.

def execucaoDetalhada_list(request):

    # Obter os dados do formulário de filtro
    filter_form = ExecucaoFilterForm(request.GET)

    # Obter o queryset inicial
    queryset = ExecucaoDetalhada.objects.all()

    # Aplicar os filtros
    if filter_form.is_valid():
        ugResponsavel = filter_form.cleaned_data.get('ugResponsavel')
        etapaCredito = filter_form.cleaned_data.get('etapaCredito')

        if ugResponsavel:
            queryset = queryset.filter(ugResponsavel=ugResponsavel)  # Substitua "nome" pelo campo adequado
        if etapaCredito:
            queryset = queryset.filter(etapaCredito=etapaCredito)

    # Configurar a tabela com os dados filtrados
    table = ExecucaoDetalhadaTable(queryset)

    RequestConfig(request, paginate={"per_page": 100}).configure(table)

    # Renderizar o template com a tabela e o formulário
    context = {
        "table": table,
        "filter_form": filter_form,
    }


    return render(request, "execucaoorcamentariadetalhada/execucaodetalhada_list.html", context)


def execucaoDetalhada_detail(request, pk):
    ed = get_object_or_404(ExecucaoDetalhada, id=pk)

    context = {"execucaodetalhada": ed}

    return render(request, "execucaoorcamentariadetalhada/execucaodetalhada_detail.html", context)

