# Generated by Django 3.0.7 on 2022-09-16 00:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalAPP', '0003_auto_20220915_1917'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paciente',
            old_name='sexo',
            new_name='genero',
        ),
    ]