from django.db import models

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

    class Meta:
        managed = True
        db_table = "AcaoGoverno" 

                             