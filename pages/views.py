from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from decimal import Decimal


class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        ultimospagamentos = [
            ["01/01/2023", "nome UG", "descrição", Decimal(100)],
            ["01/01/2023", "nome UG", "descrição", Decimal(100)],
            ["01/01/2023", "nome UG", "descrição", Decimal(100)],
        ]

        ultimasvendas = [
            ["01/01/2023", "nome UG", "descrição", Decimal(100)],
            ["01/01/2023", "nome UG", "descrição", Decimal(100)],
            ["01/01/2023", "nome UG", "descrição", Decimal(100)],
        ]

        context = super().get_context_data(**kwargs)
        context["totalareceber"] = Decimal(9999.99)
        context["totalapagar"] = Decimal(9999.99)
        context["ultimospagamentos"] = ultimospagamentos
        context["ultimasvendas"] = ultimasvendas
        return context


class AboutPageView(TemplateView):
    template_name = "about.html"

