# Generated by Django 5.0.6 on 2024-07-11 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facil', '0009_emprestimos_resolvido'),
    ]

    operations = [
        migrations.AddField(
            model_name='seminova',
            name='valor',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
