# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=200)

class Webinar(models.Model):
    """Talleres / Webinars: Titulo, imagen, descripcion, fecha inicio, fecha fin"""
    title = models.CharField(max_length=200)
    image = models.ImageField()
    description = models.TextField()
    inicio = models.DateTimeField()
    fin = models.DateTimeField()
    place = models.CharField(max_length=200)
    online = models.BooleanField(default=False)

class Document(models.Model):
    """Documentos: Titulo, imagen, descripcion, archivo"""
    title = models.CharField(max_length=200)
    image = models.ImageField()
    file = models.ImageField()
    description = models.TextField()
    date = models.DateField()
    category = models.ForeignKey(Category)

class News(models.Model):
    """Noticias o blogs: Titulo, imagen, descripcion, fecha"""
    title = models.CharField(max_length=200)
    image = models.ImageField()
    description = models.TextField()
    date = models.DateField()
    category = models.ForeignKey(Category)

#class Media(models.Model):
#    """Multimedia: Fotos, audio y video"""
#
class Field(models.Model):
    """Beneficios: Titulo, imagen, descripcion"""
    title = models.CharField(max_length=200)
    image = models.ImageField()
    description = models.TextField()
