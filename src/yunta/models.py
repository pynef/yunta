#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from django.contrib.auth.models import User
from django.db import models
from .choices import TIPO_FRECUENCIA, GENERO_CHOICES


def generar_ruta_imagen(instance, filename):
    return os.path.join("Profile", filename)


class Usuario(models.Model):
    user = models.OneToOneField(User,  on_delete=models.PROTECT)
    dni = models.CharField('D.N.I.', max_length=8, unique=True, null=True, blank=True)
    nombres = models.CharField('Nombres', max_length=150)
    apellido_paterno = models.CharField('Apellido paterno', max_length=150)
    apellido_materno = models.CharField('Apellido materno', max_length=150)
    genero = models.CharField('Genero', max_length=10, choices=GENERO_CHOICES, default='F')
    correo = models.EmailField('Correo Electronico', max_length=254, null=True, blank=True)
    imagen = models.ImageField(upload_to=generar_ruta_imagen, default="Profile/default.png")
    celular = models.CharField('Celular', max_length=50, null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    usuario_creacion = models.ForeignKey(User, on_delete=models.PROTECT, related_name='+', null=True, blank=True)
    usuario_modificacion = models.ForeignKey(User, on_delete=models.PROTECT, related_name='+', null=True, blank=True)

    def __str__(self):
        return u'{}| {}, {}'.format(self.user.username, self.user.last_name.capitalize(), self.user.first_name.capitalize())

    def nombre_completo(self):
        return u'{}| {}, {}'.format(self.user.username, self.user.apellido_paterno.upper(), self.user.apellido_materno.upper())

    class Meta:
        ordering = ['dni']
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'


class Junta(models.Model):
    nombre = models.CharField(max_length=200)
    monto = models.DecimalField(decimal_places=2, max_digits=8)
    nro_cuotas = models.IntegerField()
    puja = models.DecimalField(decimal_places=2, max_digits=8, default=0)
    clave = models.CharField(max_length=200, null=True)
    nro_participantes = models.IntegerField(default=2)
    frecuencia = models.CharField('Frecuencia', max_length=10, choices=TIPO_FRECUENCIA, default='M', db_index=True)
    creador = models.ForeignKey(User, on_delete=models.PROTECT)
    activo = models.BooleanField(default=False)
    abierto = models.BooleanField(default=False)
    iniciar = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    usuario_creacion = models.ForeignKey(User, on_delete=models.PROTECT, related_name='+', null=True, blank=True)
    usuario_modificacion = models.ForeignKey(User, on_delete=models.PROTECT, related_name='+', null=True, blank=True)

    def __str__(self):
        return u'{}'.format(self.nombre)

    class Meta:
        ordering = ['-fecha_creacion']
        verbose_name = u'Junta'
        verbose_name_plural = u'Juntas'


class ParticipanteJunta(models.Model):
    junta = models.ForeignKey(Junta,  on_delete=models.PROTECT)
    participante = models.ForeignKey(User,  on_delete=models.PROTECT)
    monto = models.DecimalField(decimal_places=2, max_digits=8, default=0)
    nro_cuotas = models.IntegerField()
    cuota = models.IntegerField()
    mi_cuota = models.DecimalField(decimal_places=2, max_digits=8, default=0)
    puja = models.IntegerField(default=0)
    mi_puja = models.DecimalField(decimal_places=2, max_digits=8, default=0)
    fecha = models.DateField(null=True)
    es_activo = models.BooleanField(default=True)
    es_creador = models.BooleanField(default=False)
    iniciar = models.BooleanField(default=False)

    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    usuario_creacion = models.ForeignKey(User, on_delete=models.PROTECT, related_name='+', null=True, blank=True)
    usuario_modificacion = models.ForeignKey(User, on_delete=models.PROTECT, related_name='+', null=True, blank=True)

    def __str__(self):
        return u'{}'.format(self.monto)

    class Meta:
        ordering = ['-fecha_creacion']
        verbose_name = u'Junta'
        verbose_name_plural = u'Juntas'
        unique_together = (('junta', 'participante'),)


class DetalleParticipanteJunta(models.Model):
    participante_junta = models.ForeignKey(ParticipanteJunta,  on_delete=models.PROTECT)
    monto = models.IntegerField()
    nro_cuotas = models.IntegerField()
    nro_cuota_actual = models.IntegerField()
    cuota = models.IntegerField()
    cuota_actual = models.IntegerField
    puja = models.IntegerField(default=0)
    puja_actual = models.IntegerField(default=0)
    fecha_pago = models.DateField(null=True)
    esta_pagado = models.BooleanField(default=False)

    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    usuario_creacion = models.ForeignKey(User, on_delete=models.PROTECT, related_name='+', null=True, blank=True)
    usuario_modificacion = models.ForeignKey(User, on_delete=models.PROTECT, related_name='+', null=True, blank=True)

    def __str__(self):
        return u'{}'.format(self.cuota)

    class Meta:
        ordering = ['-fecha_creacion']
        verbose_name = u'Junta'
        verbose_name_plural = u'Juntas'


class Monedero(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.PROTECT)
    saldo_actual = models.IntegerField()
    saldo_contable = models.IntegerField()

    def __str__(self):
        return u'{} - {}'.format(self.usuario.username, self.saldo_actual)

    class Meta:
        ordering = ['-saldo_actual']
        verbose_name = u'Monedero'
        verbose_name_plural = u'Monederos'
