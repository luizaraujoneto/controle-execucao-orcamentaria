# Generated by Django 5.1.3 on 2024-11-18 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('execucaoorcamentariadetalhada', '0007_execucaodetalhada_meslancamento'),
    ]

    operations = [
        migrations.CreateModel(
            name='MesLancamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mesLancamento', models.CharField(db_column='mesLancamento', max_length=150)),
            ],
            options={
                'db_table': 'mesLancamento',
                'managed': True,
            },
        ),
    ]