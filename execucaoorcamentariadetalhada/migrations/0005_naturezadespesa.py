# Generated by Django 5.1.3 on 2024-11-16 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('execucaoorcamentariadetalhada', '0004_acaogoverno_etapacredito'),
    ]

    operations = [
        migrations.CreateModel(
            name='NaturezaDespesa',
            fields=[
                ('codigo', models.CharField(db_column='codigoNaturezaDespesa', max_length=15, primary_key=True, serialize=False)),
                ('nome', models.CharField(db_column='nomeNaturezaDespesa', max_length=150)),
            ],
            options={
                'db_table': 'NaturezaDespesa',
                'managed': True,
            },
        ),
    ]