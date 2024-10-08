# Generated by Django 5.1 on 2024-09-12 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_recurso_icone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assinatura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('assinatura', models.CharField(max_length=100, verbose_name='Assinatura')),
                ('preco', models.IntegerField(default=10, verbose_name='Preço')),
                ('descricao_01', models.TextField(max_length=200, verbose_name='Descrição')),
                ('descricao_02', models.TextField(max_length=200, verbose_name='Descrição')),
                ('descricao_03', models.TextField(max_length=200, verbose_name='Descrição')),
                ('descricao_04', models.TextField(max_length=200, verbose_name='Descrição')),
                ('icone', models.CharField(choices=[('lni-package', 'Pacote'), ('lni-drop', 'Gota'), ('lni-star', 'Estrela')], max_length=16, verbose_name='Icone')),
            ],
            options={
                'verbose_name': 'Assinatura',
                'verbose_name_plural': 'Assinaturas',
            },
        ),
    ]
