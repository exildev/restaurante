# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.core.validators
import cuser.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Almacen',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=45)),
                ('fecha_agregado', models.DateTimeField(auto_now_add=True)),
                ('usuario', cuser.fields.CurrentUserField(editable=False, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Entrada',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(max_length=45)),
                ('cantidad', models.PositiveIntegerField()),
                ('valor_unitario', models.DecimalField(max_digits=6, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)])),
                ('ubicacion', models.CharField(max_length=100)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Presentacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('unidades', models.DecimalField(max_digits=6, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)])),
                ('fecha_agregado', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=45)),
                ('fecha_agregado', models.DateTimeField(auto_now_add=True)),
                ('almacen', models.ForeignKey(to='inventario.Almacen')),
                ('usuario', cuser.fields.CurrentUserField(editable=False, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=45)),
                ('fecha_agregado', models.DateTimeField(auto_now_add=True)),
                ('usuario', cuser.fields.CurrentUserField(editable=False, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RequisicionDeCompra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(max_length=45)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('usuario', cuser.fields.CurrentUserField(editable=False, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Salida',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.DecimalField(max_digits=6, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)])),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('entrada', models.ForeignKey(to='inventario.Entrada')),
                ('usuario', cuser.fields.CurrentUserField(editable=False, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SolicitudDeProducto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.PositiveIntegerField()),
                ('presentacion', models.ForeignKey(to='inventario.Presentacion')),
                ('producto', models.ForeignKey(to='inventario.Producto')),
                ('requisiciondecompra', models.ForeignKey(to='inventario.RequisicionDeCompra')),
            ],
        ),
        migrations.AddField(
            model_name='presentacion',
            name='producto',
            field=models.ForeignKey(to='inventario.Producto'),
        ),
        migrations.AddField(
            model_name='presentacion',
            name='usuario',
            field=cuser.fields.CurrentUserField(editable=False, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='entrada',
            name='presentacion',
            field=models.ForeignKey(to='inventario.Presentacion'),
        ),
        migrations.AddField(
            model_name='entrada',
            name='producto',
            field=models.ForeignKey(to='inventario.Producto'),
        ),
        migrations.AddField(
            model_name='entrada',
            name='proveedor',
            field=models.ForeignKey(to='inventario.Proveedor'),
        ),
        migrations.AddField(
            model_name='entrada',
            name='usuario',
            field=cuser.fields.CurrentUserField(editable=False, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
