# Generated by Django 4.1.2 on 2022-10-21 01:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('avanzo', '0002_remove_avanzo_empresas_vinculadas_avanzo_nombre'),
        ('empresavinculada', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresavinculada',
            name='avanzo',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='avanzo.avanzo'),
        ),
        migrations.AddField(
            model_name='empresavinculada',
            name='nombre',
            field=models.CharField(max_length=255, null=True),
        ),
    ]