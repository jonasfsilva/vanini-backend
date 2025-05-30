# Generated by Django 4.2.15 on 2024-08-28 19:36

import autoslug.fields
from django.db import migrations, models
import localflavor.br.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Indentificador')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado às')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado às')),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True, verbose_name='Deletado às')),
                ('deleted', models.BooleanField(db_index=True, default=False, verbose_name='Deletado')),
                ('uf', localflavor.br.models.BRStateField(blank=True, max_length=2, null=True, verbose_name='estado')),
                ('zone_code', models.CharField(max_length=255, verbose_name='código IBGE da Zona')),
                ('zone', models.CharField(choices=[('Norte', 'Norte'), ('Nordeste', 'Nordeste'), ('Sudeste', 'Sudeste'), ('Sul', 'Sul'), ('Centro-Oeste', 'Centro-Oeste')], max_length=255, verbose_name='zona')),
                ('code', models.CharField(error_messages={'unique': 'Já existe um estado cadastrado com esse código'}, max_length=255, unique=True, verbose_name='código IBGE')),
                ('name', models.CharField(max_length=255, verbose_name='nome')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique=True)),
            ],
            options={
                'verbose_name': 'Estado',
                'verbose_name_plural': 'Estados',
            },
        ),
    ]
