# Generated by Django 3.2 on 2021-09-10 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socializei', '0006_remove_evento_sucesso'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='sucesso',
            field=models.CharField(blank=True, default='true', max_length=5),
        ),
    ]
