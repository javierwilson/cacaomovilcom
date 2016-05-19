# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from filer.fields.image import FilerImageField
from filer.fields.file import FilerFileField

@python_2_unicode_compatible
class Guide(models.Model):
    """
    This model store the cacaomovil guias digitales
    """
    number = models.IntegerField('Numero', unique=True)
    name = models.CharField('Nombre', max_length=250)
    image = models.ImageField('Imagen', upload_to='guide/')

    class Meta:
        verbose_name = 'Guia'
        verbose_name_plural = 'Guias'
        ordering = ['number']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/guia/%s' % (self.number,)

@python_2_unicode_compatible
class Category(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

@python_2_unicode_compatible
class EventType(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

@python_2_unicode_compatible
class Event(models.Model):
    """Talleres / Webinars: Titulo, imagen, descripcion, fecha inicio, fecha fin"""
    title = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField()
    inicio = models.DateTimeField()
    fin = models.DateTimeField()
    place = models.CharField(max_length=200)
    online = models.BooleanField(default=False)
    eventtype = models.ForeignKey(EventType)
    category = models.ForeignKey(Category, null=True, blank=True)
    url = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.title

@python_2_unicode_compatible
class Document(models.Model):
    """Documentos: Titulo, imagen, descripcion, archivo"""
    title = models.CharField(max_length=200)
    image = models.ImageField()
    file = models.FileField()
    description = models.TextField()
    date = models.DateField()
    category = models.ForeignKey(Category)

    def __str__(self):
        return self.title

@python_2_unicode_compatible
class News(models.Model):
    """Noticias o blogs: Titulo, imagen, descripcion, fecha"""
    title = models.CharField(max_length=200)
    image = models.ImageField()
    description = models.TextField()
    date = models.DateField()
    category = models.ForeignKey(Category)

    def __str__(self):
        return self.title

@python_2_unicode_compatible
class Catalog(models.Model):
    """Multimedia: Fotos, audio y video"""
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category)

    def __str__(self):
        return self.title

@python_2_unicode_compatible
class CatalogFile(models.Model):
    """Multimedia: Fotos, audio y video"""
    catalog = models.ForeignKey(Category)
    image = FilerImageField(null=True, blank=True, related_name="images")
    file = FilerFileField(null=True, blank=True, related_name="files")

    def __str__(self):
        return self.title

@python_2_unicode_compatible
class Field(models.Model):
    """Beneficios: Titulo, imagen, descripcion"""
    title = models.CharField(max_length=200)
    image = models.ImageField()
    description = models.TextField()

    def __str__(self):
        return self.title

@python_2_unicode_compatible
class Product(models.Model):
    """Productos: Titulo, imagen, descripcion"""
    title = models.CharField(max_length=200)
    image = models.ImageField()
    description = models.TextField()
    url = models.CharField(max_length=200, null=True, blank=True)
    nickname = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.title
