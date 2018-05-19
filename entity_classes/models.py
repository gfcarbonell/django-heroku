#!/usr/bin/python3
# -*- encoding: utf-8 -*-
from django.db import models
from django.template.defaultfilters import slugify
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.core.validators import MaxLengthValidator
from django.core.validators import MinLengthValidator

from .enums import EntityScope


# Create your models here.
class EntityClass(models.Model):
    '''
        This Class: EntityClass is for to identify the class that an entity belongs.
        Esta Clase: ClaseEntidad es para identificar la clase que pertenece una entidad.

        Attributes - Atributos
            Economic Activity | Actividad Econónica
                >Primary Sector | Sector Primario
                >Secondary Sector | Sector Secundario 
                >Third Sector | Sector Terciario 
            Legal Form | Forma Jurídica
                >Individual Companies | Empresa Individual
                >Corporate Companies | Empresa Societario
            Size | Tamaño
                >Micro company | Micro Empresa
                >Small company | Pequeña Empresa
                >Medium company | Mediana Empresa
                >Big company | Gran Empresa
            Scope of Operation | Ámbito de Operación
                >Local companies | Empresas Locales
                >Regional | Regionales
                >Nationals | Nacionales
                >Multinationals | Multinacionales
            Capital Composition | Composición del Capital
                >Public Company | Empresa Pública
                >Private Company | Empresa Privada
                >Mixed Company | Empresa Mixta
                >Self-management company | Empresa de Autogestión
    '''
    CHOICES_ENTITY_SCOPE = [(entity_scope.value, entity_scope.value) for entity_scope in EntityScope]
    
    entity_scope = models.CharField(
        choices = CHOICES_ENTITY_SCOPE,
        max_length=50,
        db_index=True,
        help_text= 'Entity Scope | Ámbito Entidad'
    )
    name = models.CharField(
        max_length=100,
        unique=True,
        db_index=True,
        validators=[
            MinLengthValidator(1),
            MaxLengthValidator(100),
        ],
        help_text= 'Name | Nombre'
    )
    slug = models.SlugField(
        editable=False, 
        max_length=255,
        unique=True, 
        db_index=True 
    )
    
    def __str__(self):
        return '%s - %s' %(self.get_entity_scope(), self.get_name())

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.get_name())
        else:
            slug = slugify(self.get_name())
            if self.slug != slug:
                self.slug = slug
        super(EntityClass, self).save(*args, **kwargs)

    #Setter
    def set_entity_scope(self, entity_scope):
        self.entity_scope = entity_scope

    def set_name(self, name):
        self.name = name
    
    #Getter
    def get_entity_scope(self):
        return self.entity_scope

    def get_name(self):
        return self.name

    class Meta:
        db_table = 'entity_classes'
        ordering = ['entity_scope', 'name']
        verbose_name = 'Entity Class'
        verbose_name_plural = 'Entity Classes'