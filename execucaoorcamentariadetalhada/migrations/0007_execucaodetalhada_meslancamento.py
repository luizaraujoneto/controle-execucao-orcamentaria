# Generated by Django 5.1.3 on 2024-11-17 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('execucaoorcamentariadetalhada', '0006_execucaodetalhada'),
    ]

    operations = [
        migrations.AddField(
            model_name='execucaodetalhada',
            name='mesLancamento',
            field=models.CharField(db_column='mesLancamento', default='NOTSET', max_length=10),
            preserve_default=False,
        ),
    ]
