from django.db import models

import django_tables2 as tables

# Create your models here.

class UGResponsavel(models.Model):
    
    codigo = models.CharField(
        db_column="codigoUGResponsavel", 
        max_length=15,
        blank=False,
        null=False,
        primary_key=True,
    )

    nome = models.CharField(
        db_column="nomeUGResponsavel",
        max_length=150,
        blank=False,
        null=False,
    )

    def __str__(self):
        return self.codigo + ' - ' + self.nome

    class Meta:
        managed = True
        db_table = "UGResponsavel"


class DespesaAgregada(models.Model):
    
    codigo = models.CharField(
        db_column="codigoDespesaAgregada", 
        max_length=15,
        blank=False,
        null=False,
        primary_key=True,
    )

    nome = models.CharField(
        db_column="nomeDespesaAgregada",
        max_length=150,
        blank=False,
        null=False,
    )

    def __str__(self):
        return self.codigo + ' - ' + self.nome

    class Meta:
        managed = True
        db_table = "DespesaAgregada"        


class GrupoDespesa(models.Model):
    
    codigo = models.CharField(
        db_column="codigoGrupoDespesa", 
        max_length=15,
        blank=False,
        null=False,
        primary_key=True,
    )

    nome = models.CharField(
        db_column="nomeGrupoDespesa",
        max_length=150,
        blank=False,
        null=False,
    )

    def __str__(self):
        return self.codigo + ' - ' + self.nome

    class Meta:
        managed = True
        db_table = "GrupoDespesa"                
        

class EtapaCredito(models.Model):

    nome = models.CharField(
        db_column="nomeEtapaCredito",
        max_length=150,
        blank=False,
        null=False,
    )

    def __str__(self):
        return self.nome
    
    class Meta:
        managed = True
        db_table = "EtapaCredito" 


class AcaoGoverno(models.Model):
    
    codigo = models.CharField(
        db_column="codigoAcaoGoverno", 
        max_length=15,
        blank=False,
        null=False,
        primary_key=True,
    )

    nome = models.CharField(
        db_column="nomeAcaoGoverno",
        max_length=150,
        blank=False,
        null=False,
    )

    def __str__(self):
        return self.codigo + ' - ' + self.nome
    
    class Meta:
        managed = True
        db_table = "AcaoGoverno" 

 
class NaturezaDespesa(models.Model):
    
    codigo = models.CharField(
        db_column="codigoNaturezaDespesa", 
        max_length=15,
        blank=False,
        null=False,
        primary_key=True,
    )

    nome = models.CharField(
        db_column="nomeNaturezaDespesa",
        max_length=150,
        blank=False,
        null=False,
    )

    def __str__(self):
        return self.codigo + ' - ' + self.nome
    
    class Meta:
        managed = True
        db_table = "NaturezaDespesa" 

                            
class ExecucaoDetalhada(models.Model):
    
    mesLancamento = models.CharField(
        db_column="mesLancamento",
        max_length=10,
        blank=False,
        null=False,
    )

    
    acaoGoverno = models.ForeignKey(
        "AcaoGoverno",
        on_delete=models.PROTECT,
        db_column="codigoAcaoGoverno",
        to_field="codigo",
        blank=False,
        null=False,
    )

    ugResponsavel = models.ForeignKey(
        "UGResponsavel",
        on_delete=models.PROTECT,
        db_column="codigoUGResponsavel",
        to_field="codigo",
        blank=False,
        null=False,
    )

    despesaAgregada = models.ForeignKey(
        "DespesaAgregada",
        on_delete=models.PROTECT,
        db_column="codigoDespesaAgregada",
        to_field="codigo",
        blank=False,
        null=False,
    )

    grupoDespesa = models.ForeignKey(
        "GrupoDespesa",
        on_delete=models.PROTECT,
        db_column="codigoGupooDespesa",
        to_field="codigo",
        blank=False,
        null=False,
    )

    naturezaDespesa = models.ForeignKey(
        "NaturezaDespesa",
        on_delete=models.PROTECT,
        db_column="codigoNaturezaDespesa",
        to_field="codigo",
        blank=False,
        null=False,
    )

    etapaCredito = models.ForeignKey(
        "EtapaCredito",
        on_delete=models.PROTECT,
        db_column="idEtapaCredito",
        to_field="id",
        blank=False,
        null=False,
    )

    saldo = models.DecimalField(
        db_column="saldo",
        blank=False,
        null=False,
        max_digits=10,
        decimal_places=2,
    )


class ExecucaoDetalhadaTable(tables.Table):
    class Meta:
        model = ExecucaoDetalhada