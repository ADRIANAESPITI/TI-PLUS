# Generated by Django 3.0.7 on 2022-09-16 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalAPP', '0004_auto_20220915_1917'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='familiar',
            name='genero',
        ),
        migrations.AlterField(
            model_name='medico',
            name='especialidad',
            field=models.CharField(choices=[('1', 'Medico gral'), ('2', 'Cardiología'), ('3', 'Gastroenterología'), ('4', 'Neurología'), ('5', 'Nutriología'), ('6', 'Pediatría'), ('7', 'Psiquiatría'), ('8', 'Psicologia')], default='medico gral', max_length=1),
        ),
    ]