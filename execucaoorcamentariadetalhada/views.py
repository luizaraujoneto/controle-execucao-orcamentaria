from django.shortcuts import render

from .models import ExecucaoDetalhada, ExecucaoDetalhadaTable

# Create your views here.

def execucaoDetalhada_list(request):
    table = ExecucaoDetalhadaTable(ExecucaoDetalhada.objects.all())
    table.paginate(page=request.GET.get("page", 1), per_page=100)
    return render(request, "execucaoorcamentariadetalhada/execucaodetalhada_list.html", {"table": table})