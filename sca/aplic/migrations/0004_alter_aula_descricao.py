# Generated by Django 4.2.4 on 2023-11-27 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0003_delete_topico_aula_descricao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aula',
            name='descricao',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
