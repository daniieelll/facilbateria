# Generated by Django 5.0.6 on 2024-07-09 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facil', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='assistencia',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='facil/'),
        ),
        migrations.AddField(
            model_name='emprestimos',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='facil/'),
        ),
        migrations.AddField(
            model_name='seminova',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='facil/'),
        ),
    ]
