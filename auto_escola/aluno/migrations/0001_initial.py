# Generated by Django 3.0.3 on 2020-02-21 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='nome')),
                ('cpf', models.CharField(max_length=14, verbose_name='CPF')),
                ('telefone', models.CharField(max_length=11, verbose_name='telefone')),
                ('endereco', models.CharField(max_length=200, verbose_name='endereco')),
                ('email', models.CharField(max_length=100, verbose_name='email')),
                ('status', models.CharField(choices=[('A', 'ativo'), ('I', 'inativo')], max_length=1)),
                ('id_escola', models.IntegerField(verbose_name='id_escola')),
                ('senha', models.CharField(max_length=100, verbose_name='senha')),
            ],
        ),
    ]