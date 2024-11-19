from decimal import Decimal
import pandas as pd
from django.core.management.base import BaseCommand

from  execucaoorcamentariadetalhada.models import UGResponsavel, AcaoGoverno, AcaoGoverno, EtapaCredito, MesLancamento
from  execucaoorcamentariadetalhada.models import DespesaAgregada, GrupoDespesa, NaturezaDespesa, ExecucaoDetalhada

class Command(BaseCommand):
    help = "Carregar dados do Planejamento Orçamentário"

    def handle(self, *args, **kwargs):
      
        # Load the Excel file using pandas
        file_path = 'programacao-orcamentaria.xlsx'

        df = pd.read_excel(file_path, header=1, sheet_name='Despesas')

        ExecucaoDetalhada.objects.all().delete()

        self.loadMesLancamento(df)
        self.loadUGResponsavel(df)
        self.loadDespesaAgregada(df)
        self.loadGrupoDespesa(df)
        self.loadNaturezaDespesa(df)
        self.loadAcaoGoverno(df)
        self.loadEtapaCredito(df)
        self.loadExecucaoDetalhada(df)

        self.printAcaoGoverno()
        self.printDespesaAgregada()
        self.printEtapaCredito()
        self.printGrupoDespesa()
        self.printNaturezaDespesa()

        self.stdout.write(self.style.SUCCESS("Data loaded successfully from Excel file."))


    def loadUGResponsavel(self, df):

        unidade = df[ ['UG Responsável Código', 'UG Responsável Nome']]

        unidade = unidade.drop_duplicates()

        # unidade = unidade[unidade['UG Responsável Nome'].str.startswith('UGR -')]

        unidade = unidade.sort_values(by='UG Responsável Nome')

        UGResponsavel.objects.all().delete()

        for _, row in unidade.iterrows():
            UGResponsavel.objects.get_or_create(codigo=row['UG Responsável Código'], nome=row['UG Responsável Nome'])

    
    def printUGResponsavel(self ):
    
        unidades = UGResponsavel.objects.all()
        
        print("UG Responsavel-----------------------------------------------------------------------------")

        for unidade in unidades:
            print(unidade.codigo + ' - ' + unidade.nome )

        print("")


    def loadDespesaAgregada(self, df):

        despesa = df[ ['PI Código PI', 'PI Nome']]

        despesa = despesa.drop_duplicates()

        despesa = despesa.sort_values(by='PI Nome')

        DespesaAgregada.objects.all().delete()

        for _, row in despesa.iterrows():
            DespesaAgregada.objects.get_or_create(codigo=row['PI Código PI'], nome=row['PI Nome'])


    def printDespesaAgregada(self):

        despesas = DespesaAgregada.objects.all()
        
        print("Despesa Agregada-----------------------------------------------------------------------------")

        for despesa in despesas:
            print(despesa.codigo + ' - ' + despesa.nome )

        print("")


    def loadGrupoDespesa(self, df):

        grupoDespesa = df[ ['Grupo Despesa Código Grupo', 'Grupo Despesa Nome']]

        grupoDespesa = grupoDespesa.drop_duplicates()

        grupoDespesa = grupoDespesa.sort_values(by='Grupo Despesa Nome')

        AcaoGoverno.objects.all().delete()

        for _, row in grupoDespesa.iterrows():
            AcaoGoverno.objects.get_or_create(codigo=row['Grupo Despesa Código Grupo'], nome=row['Grupo Despesa Nome'])


    def printGrupoDespesa(self):

        gruposDespesas = AcaoGoverno.objects.all()
        
        print("Grupo Despesa-----------------------------------------------------------------------------")

        for grupoDespesa in gruposDespesas:
            print(grupoDespesa.codigo + ' - ' + grupoDespesa.nome )

        print('')


    def loadNaturezaDespesa(self, df):

        naturezaDespesa = df[ ['Natureza Despesa Código', 'Natureza Despesa Nome']]

        naturezaDespesa = naturezaDespesa.drop_duplicates()

        naturezaDespesa = naturezaDespesa.sort_values(by='Natureza Despesa Nome')

        NaturezaDespesa.objects.all().delete()

        for _, row in naturezaDespesa.iterrows():
            NaturezaDespesa.objects.get_or_create(codigo=row['Natureza Despesa Código'], nome=row['Natureza Despesa Nome'])

    
    def printNaturezaDespesa(self):

        naturezasDespesas = NaturezaDespesa.objects.all()
        
        print("Natureza Despesa-----------------------------------------------------------------------------")

        for naturezaDespesa in naturezasDespesas:
            print(naturezaDespesa.codigo + ' - ' + naturezaDespesa.nome )

        print('')


    def loadEtapaCredito(self, df):

        etapaCredito = df[ ['Conta Contábil']]

        etapaCredito = etapaCredito.drop_duplicates()

       # EtapaCredito = EtapaCredito.sort_values(by='Grupo Despesa Nome')

        EtapaCredito.objects.all().delete()

        for _, row in etapaCredito.iterrows():
            EtapaCredito.objects.get_or_create(nome=row['Conta Contábil'])

    
    def printEtapaCredito(self ):

        etapasCredito = EtapaCredito.objects.all()
        
        print("Etapa Crédito-----------------------------------------------------------------------------")

        for etapaCredito in etapasCredito:
            print(etapaCredito.nome )

        print('')


    def loadMesLancamento(self, df):

        mesLancamento = df[ ['Mês Lançamento']]

        mesLancamento = mesLancamento.drop_duplicates()

        # mesLancamento = mesLancamento.sort_values(by='Mês Lançamento')

        MesLancamento.objects.all().delete()

        for _, row in mesLancamento.iterrows():
            MesLancamento.objects.get_or_create(mesLancamento=row['Mês Lançamento'])

    
    def printMesLancamento(self ):

        mesesLancamento = MesLancamento.objects.all()
        
        print("Mês Lançamento-----------------------------------------------------------------------------")

        for mes in mesesLancamento:
            print(mes.mesLancamento )

        print('')


    def loadAcaoGoverno(self, df):

        acaoGoverno = df[ ['Ação Governo Código', 'Ação Governo Nome']]

        acaoGoverno = acaoGoverno.drop_duplicates()

        acaoGoverno = acaoGoverno.sort_values(by='Ação Governo Nome')

        AcaoGoverno.objects.all().delete()

        for _, row in acaoGoverno.iterrows():
            AcaoGoverno.objects.get_or_create(codigo=row['Ação Governo Código'], nome=row['Ação Governo Nome'])

    
    def printAcaoGoverno(self):

        acoesGoverno = AcaoGoverno.objects.all()
        
        print("Ação Governo-----------------------------------------------------------------------------")

        for acaoGoverno in acoesGoverno:
            print(acaoGoverno.codigo + ' - ' + acaoGoverno.nome )

        print('')


    def loadExecucaoDetalhada(self, df):

        execucaoDetalhada = df

        for _, row in execucaoDetalhada.iterrows():

            try:

                ml = row['Mês Lançamento']
                ag = AcaoGoverno.objects.get(codigo=row['Ação Governo Código'])
                ugr = UGResponsavel.objects.get(codigo=row['UG Responsável Código'])
                da = DespesaAgregada.objects.get(codigo=row['PI Código PI'])
                gd = GrupoDespesa.objects.get(codigo=row['Grupo Despesa Código Grupo'])
                nd = NaturezaDespesa.objects.get(codigo=row['Natureza Despesa Código'])
                ec = EtapaCredito.objects.get(nome=row['Conta Contábil'])
                saldo = Decimal( row['Saldo - R$ (Conta Contábil)'] )

                ExecucaoDetalhada.objects.get_or_create( 
                                        mesLancamento=ml,
                                        acaoGoverno=ag, 
                                        ugResponsavel=ugr,
                                        despesaAgregada=da,
                                        grupoDespesa=gd,
                                        naturezaDespesa=nd,
                                        etapaCredito=ec,
                                        saldo=saldo )

            except Exception as e:
                print(f"An error occurred: {e}")

        ed = ExecucaoDetalhada.objects.all()

        print("Execucao Detalhada-----------------------------------------------------------------------------")

        for execucaoDetalhada in ed:
            print(execucaoDetalhada.acaoGoverno.nome + ' - ' + execucaoDetalhada.ugResponsavel.nome + " - " +  str( execucaoDetalhada.saldo) )

        print('')

