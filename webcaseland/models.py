# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ckeditor.fields import RichTextField
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.core.exceptions import ValidationError
from colorfield.fields import ColorField


# Create your models here.
def validate_image(fieldfile_obj):
    file_size = fieldfile_obj.file.size
    megabyte_limit = 0.3
    if file_size > megabyte_limit * 1024 * 1024:
        raise ValidationError("Maximo tamaño de la imagen es %s MB (%s Kb)" % (megabyte_limit, megabyte_limit*1000))


@python_2_unicode_compatible
class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name='nombre')
    order = models.IntegerField(verbose_name='orden', blank=False, default=0)
    image = models.ImageField(blank=False, validators=[validate_image], verbose_name='imagen')
    visible = models.BooleanField(verbose_name='visible', blank=False, default=True)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class SubCategory(models.Model):
    name = models.CharField(verbose_name="Nombre", max_length=255, blank=False, unique=False)
    image = models.ImageField(blank=False, validators=[validate_image], verbose_name='imagen')
    category = models.ForeignKey(Category, verbose_name="Categoría", blank=False, null=True)
    order = models.IntegerField(verbose_name="Orden", blank=False, default=0)
    visible = models.BooleanField(verbose_name='visible', blank=False, default=True)

    class Meta:
        verbose_name = "SubCategoría"
        verbose_name_plural = "SubCategorías"

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Product(models.Model):
    code = models.CharField(max_length=30, verbose_name='código', unique=True)
    name = models.CharField(max_length=30, verbose_name='nombre')
    description = RichTextField(verbose_name='Descripcion', max_length=4000, blank=False)
    image = models.ImageField(blank=False, validators=[validate_image],verbose_name='imagen')
    order = models.PositiveIntegerField(verbose_name='orden', blank=False, default=1)
    visible = models.BooleanField(verbose_name='visible', blank=False, default=True)
    category = models.ForeignKey(Category,verbose_name='categoria')
    price = models.FloatField(verbose_name='precio', blank=False, default=0)


    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return self.name

    def image_pic(self):
        return """
            <img src="/media/%s" width="100">
        """ % self.image

    image_pic.allow_tags = True

@python_2_unicode_compatible
class CatalogProduct(models.Model):
    code = models.CharField(max_length=30, verbose_name='código', unique=True)
    name = models.CharField(max_length=30, verbose_name='nombre')
    description = RichTextField(verbose_name='Descripcion', max_length=4000, blank=False)
    image = models.ImageField(blank=False, validators=[validate_image],verbose_name='imagen')
    order = models.PositiveIntegerField(verbose_name='orden', blank=False, default=1)
    visible = models.BooleanField(verbose_name='visible', blank=False, default=True)
    subcategory = models.ForeignKey(SubCategory,verbose_name='subcategoria')
    price = models.FloatField(verbose_name='precio', blank=False, default=0)


    class Meta:
        verbose_name = "Catalogo Producto"
        verbose_name_plural = "Catalogo Productos"

    def __str__(self):
        return self.name

    def image_pic(self):
        return """
            <img src="/media/%s" width="100">
        """ % self.image

    image_pic.allow_tags = True