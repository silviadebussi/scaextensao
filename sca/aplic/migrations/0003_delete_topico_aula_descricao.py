# Generated by Django 4.2.4 on 2023-11-27 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0002_remove_topico_aula_alter_topico_titulo'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Topico',
        ),
        migrations.AddField(
            model_name='aula',
            name='descricao',
            field=models.CharField(default='si', max_length=30),
        ),
    ]
