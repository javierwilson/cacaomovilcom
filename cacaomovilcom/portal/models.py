# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from filer.fields.image import FilerImageField
from filer.fields.file import FilerFileField

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
    file = models.FileField()
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

class Catalog(models.Model):
    """Multimedia: Fotos, audio y video"""
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category)

class CatalogFile(models.Model):
    """Multimedia: Fotos, audio y video"""
    catalog = models.ForeignKey(Category)
    image = FilerImageField(null=True, blank=True, related_name="images")
    file = FilerFileField(null=True, blank=True, related_name="files")

class Field(models.Model):
    """Beneficios: Titulo, imagen, descripcion"""
    title = models.CharField(max_length=200)
    image = models.ImageField()
    description = models.TextField()
