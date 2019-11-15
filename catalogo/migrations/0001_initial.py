# Generated by Django 2.2.6 on 2019-11-08 00:36

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('resumen', models.TextField(help_text='Resumen del producto', max_length=1000)),
                ('codigo', models.CharField(help_text='13 Character">Codigo numerico</a>', max_length=13, verbose_name='codigo')),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Coleccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('date_of_launch', models.DateField(blank=True, null=True)),
            ],
            options={
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='ArticuloInstance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Identificador del articulo', primary_key=True, serialize=False)),
                ('imprint', models.CharField(max_length=200)),
                ('due_back', models.DateField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('m', 'Proximamente'), ('a', 'Disponible'), ('r', 'Reservado')], default='m', help_text='Disponible', max_length=1)),
                ('articulo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalogo.Articulo')),
            ],
            options={
                'ordering': ['due_back'],
            },
        ),
        migrations.AddField(
            model_name='articulo',
            name='coleccion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalogo.Coleccion'),
        ),
    ]