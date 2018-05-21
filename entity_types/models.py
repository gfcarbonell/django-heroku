#!/usr/bin/python3
# -*- encoding: utf-8 -*-
from django.db import models
from django.template.defaultfilters import slugify
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.core.validators import MaxLengthValidator
from django.core.validators import MinLengthValidator


# Create your models here.
class EntityType(models.Model):
    '''
        This Class: <EntityType> is for to identify the type that an entity belongs.
        Esta Clase: <TipoEntidad> es para identificar el tipo que pertenece una entidad.

        For example:
            Individual Company of Limited Liability I.C.L.L. | Empresa Individual de Responsabilidad Limitada - E.I.R.L.
            Unipersonal Company U.C. | Empresa Unipersonal - E.U.
            Anonymous Society A.S. | Sociedad Anónima - S.A.
            Open Corporation O.P. | Sociedad Anónima Abierta - S.A.A.
            Closed Company C.C | Sociedad Anónima Cerrada - S.A.C.
            Commercial Society of Limited Liability C.S.L.L. | Sociedad Comercial de Responsabilidad Limitada	- S.R.L.
    '''
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
    initials = models.CharField(
        max_length=20,
        unique=True,
        db_index=True,
        validators=[
            MinLengthValidator(1),
            MaxLengthValidator(20),
        ], 
        help_text= 'Initials | Iniciales'
    )
    slug = models.SlugField(
        editable=False, 
        max_length=255,
        unique=True, 
        db_index=True 
    )

    def __str__(self):
        return '%s - %s' %(self.get_name(), self.get_initials())

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.get_name())
        else:
            slug = slugify(self.get_name())
            if self.slug != slug:
                self.slug = slug
        super(EntityType, self).save(*args, **kwargs)

    #Setter
    def set_name(self, name):
        self.name = name
    
    def set_initials(self, initials):
        self.initials = initials
    
    #Getter
    def get_name(self):
        return self.name
   
    def get_initials(self):
        return self.initials

    class Meta:
        db_table = 'entity_types'
        ordering = ['name', 'initials']
        verbose_name = 'Entity Type'
        verbose_name_plural = 'Entity Types'