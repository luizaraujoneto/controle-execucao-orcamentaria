import pandas as pd
from django.core.management.base import BaseCommand

from  execucaoorcamentariadetalhada.models import UGResponsavel, GrupoDespesa, GrupoDespesa

class Command(BaseCommand):
    help = "Load data from Excel file into Django models"

    def handle(self, *args, **kwargs):
        # Define the file path to the Excel file
        file_path = 'path/to/your/excel/file.xlsx'
        
        # Load the Excel file using pandas
        file_path = 'arquivo-execucao-orcamentaria-tre-al.xlsx'

        df = pd.read_excel(file_path, header=1)

        self.loadUGResponsavel(df)
        self.loadDespesaAgregada(df)
        self.loadGrupoDespesa(df)

        self.stdout.write(self.style.SUCCESS("Data loaded successfully from Excel file."))


    def loadUGResponsavel(self, df):

        unidade = df[ ['UG Responsável Código', 'UG Responsável Nome']]

        unidade = unidade.drop_duplicates()

        unidade = unidade[unidade['UG Responsável Nome'].str.startswith('UGR -')]

        unidade = unidade.sort_values(by='UG Responsável Nome')

        UGResponsavel.objects.all().delete()

        for _, row in unidade.iterrows():
            UGResponsavel.objects.get_or_create(codigo=row['UG Responsável Código'], nome=row['UG Responsável Nome'])

        unidades = UGResponsavel.objects.all()
        
        print("UG Responsavel-----------------------------------------------------------------------------")

        for unidade in unidades:
            print(unidade.codigo + ' - ' + unidade.nome )

        print("")

    def loadDespesaAgregada(self, df):

        despesa = df[ ['PI Código PI', 'PI Nome']]

        despesa = despesa.drop_duplicates()

        despesa = despesa.sort_values(by='PI Nome')

        GrupoDespesa.objects.all().delete()

        for _, row in despesa.iterrows():
            GrupoDespesa.objects.get_or_create(codigo=row['PI Código PI'], nome=row['PI Nome'])

        despesas = GrupoDespesa.objects.all()
        
        print("Despesa Agregada-----------------------------------------------------------------------------")

        for despesa in despesas:
            print(despesa.codigo + ' - ' + despesa.nome )

        print("")

    def loadGrupoDespesa(self, df):

        grupoDespesa = df[ ['Grupo Despesa Código Grupo', 'Grupo Despesa Nome']]

        grupoDespesa = grupoDespesa.drop_duplicates()

        grupoDespesa = grupoDespesa.sort_values(by='Grupo Despesa Nome')

        GrupoDespesa.objects.all().delete()

        for _, row in grupoDespesa.iterrows():
            GrupoDespesa.objects.get_or_create(codigo=row['Grupo Despesa Código Grupo'], nome=row['Grupo Despesa Nome'])

        gruposDespesas = GrupoDespesa.objects.all()
        
        print("Grupo Despesa-----------------------------------------------------------------------------")

        for grupoDespesa in gruposDespesas:
            print(grupoDespesa.codigo + ' - ' + grupoDespesa.nome )

        print('')

