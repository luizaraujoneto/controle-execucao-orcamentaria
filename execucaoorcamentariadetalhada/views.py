from django.shortcuts import render, get_object_or_404

from .models import ExecucaoDetalhada, ExecucaoDetalhadaTable

# Create your views here.

def execucaoDetalhada_list(request):
    table = ExecucaoDetalhadaTable(ExecucaoDetalhada.objects.all())
    table.paginate(page=request.GET.get("page", 1), per_page=100)
    return render(request, "execucaoorcamentariadetalhada/execucaodetalhada_list.html", {"table": table})

def execucaoDetalhada_detail(request, pk):
    ed = get_object_or_404(ExecucaoDetalhada, id=pk)

    context = {"execucaodetalhada": ed}

    return render(request, "execucaoorcamentariadetalhada/execucaodetalhada_detail.html", context)
