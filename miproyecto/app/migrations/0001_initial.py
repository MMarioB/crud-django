# Generated by Django 2.0.2 on 2021-02-23 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('identificador', models.CharField(max_length=200)),
                ('direccion', models.CharField(max_length=200, null=True)),
                ('departamento', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
