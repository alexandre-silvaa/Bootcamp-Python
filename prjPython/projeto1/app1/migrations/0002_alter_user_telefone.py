# Generated by Django 4.2.3 on 2023-07-05 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='telefone',
            field=models.BigIntegerField(verbose_name='telefone'),
        ),
    ]