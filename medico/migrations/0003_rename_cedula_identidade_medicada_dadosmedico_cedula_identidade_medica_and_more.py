# Generated by Django 5.0.4 on 2024-04-25 00:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medico', '0002_dadosmedico'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dadosmedico',
            old_name='cedula_identidade_medicada',
            new_name='cedula_identidade_medica',
        ),
        migrations.AlterField(
            model_name='dadosmedico',
            name='cep',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='dadosmedico',
            name='crm',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='dadosmedico',
            name='descricao',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dadosmedico',
            name='especialidade',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='medico.especialidades'),
        ),
    ]
