# Generated by Django 4.2.3 on 2023-07-05 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='nome')),
                ('telefone', models.IntegerField(verbose_name='telefone')),
                ('email', models.CharField(max_length=255, verbose_name='email')),
            ],
        ),
    ]
