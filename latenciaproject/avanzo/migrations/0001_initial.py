# Generated by Django 4.1.2 on 2022-10-21 00:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empresavinculada', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Avanzo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empresas_vinculadas', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='empresavinculada.empresavinculada')),
            ],
        ),
    ]
