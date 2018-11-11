# Generated by Django 2.0.7 on 2018-07-22 00:35

from django.db import migrations, models
import django.db.models.deletion
import imovel.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logradouro', models.CharField(max_length=255)),
                ('numero', models.IntegerField()),
                ('complemento', models.CharField(blank=True, max_length=255)),
                ('bairro', models.CharField(max_length=255)),
                ('cidade', models.CharField(max_length=255)),
                ('estado', models.CharField(max_length=2)),
                ('cep', models.CharField(max_length=9)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'Enderecos',
                'get_latest_by': 'created_at',
            },
        ),
        migrations.CreateModel(
            name='Foto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('imagem', models.ImageField(upload_to=imovel.models.Foto.get_upload_path)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'Fotos',
                'get_latest_by': 'created_at',
            },
        ),
        migrations.CreateModel(
            name='Imovel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField()),
                ('breve_descricao', models.CharField(max_length=255)),
                ('quantidade_quartos', models.IntegerField(default=0)),
                ('area', models.IntegerField(default=0)),
                ('garagem', models.IntegerField(default=0)),
                ('tipo', models.IntegerField(choices=[(0, ''), (1, 'APARTAMENTO'), (2, 'CASA'), (3, 'SALA'), (4, 'LOJA')], default=2)),
                ('destaque', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('endereco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imovel.Endereco')),
            ],
            options={
                'db_table': 'Imoveis',
                'get_latest_by': 'created_at',
            },
        ),
        migrations.CreateModel(
            name='Locacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_locacao', models.IntegerField(choices=[(1, 'ALUGUEL-POR-TEMPORADA'), (2, 'ALUGUEL-COMERCIAL'), (3, 'ALUGUEL-RESIDENCIAL'), (4, 'VENDA')], default=3)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('imovel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imovel.Imovel')),
            ],
            options={
                'db_table': 'Locacoes',
                'get_latest_by': 'created_at',
            },
        ),
        migrations.CreateModel(
            name='Propriedade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'Propriedade',
                'get_latest_by': 'created_at',
            },
        ),
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.TextField()),
                ('imagem', models.ImageField(upload_to='servicos/')),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'Servicos',
                'get_latest_by': 'created_at',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('login', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('role', models.IntegerField(choices=[(1, 'Administrador'), (2, 'Operador'), (3, 'Locatario'), (4, 'Proprietario'), (5, 'Outros')], default=5, max_length=2)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'Usuarios',
                'get_latest_by': 'created_at',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('imovel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imovel.Imovel')),
            ],
            options={
                'db_table': 'Videos',
                'get_latest_by': 'created_at',
            },
        ),
        migrations.AddField(
            model_name='propriedade',
            name='dono',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imovel.Usuario'),
        ),
        migrations.AddField(
            model_name='propriedade',
            name='imovel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imovel.Imovel'),
        ),
        migrations.AddField(
            model_name='locacao',
            name='locador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imovel.Usuario'),
        ),
        migrations.AddField(
            model_name='imovel',
            name='locatario',
            field=models.ManyToManyField(through='imovel.Locacao', to='imovel.Usuario'),
        ),
        migrations.AddField(
            model_name='foto',
            name='imovel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imovel.Imovel'),
        ),
    ]
