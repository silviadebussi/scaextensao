# Generated by Django 4.2.7 on 2023-11-06 21:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField()),
                ('matricula', models.CharField()),
                ('senha', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('sala', models.IntegerField()),
                ('email', models.EmailField(default='seuemail@gmail.com', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Aula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('data', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Presenca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faltas', models.IntegerField(blank=True)),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplic.aluno')),
                ('aula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplic.aula')),
            ],
        ),
        migrations.CreateModel(
            name='Certificado',
            fields=[
                ('aluno_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='aplic.aluno')),
                ('nome_coordenador_faculdade', models.CharField()),
                ('nome_coordenador_colegio', models.CharField()),
                ('nome_aula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplic.aula')),
            ],
            bases=('aplic.aluno',),
        ),
    ]