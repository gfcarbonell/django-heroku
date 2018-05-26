#!/usr/bin/python3
# -*- encoding: utf-8 -*-
from django.db import models
from django.template.defaultfilters import slugify
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.core.validators import MaxLengthValidator
from django.core.validators import MinLengthValidator


# Create your models here.
class OccupationType(models.Model):
    '''
        This Class: <OccupationType> is to identify the type of occupation.
        Esta Clase: <TipoOcupación> es para identificar el tipo de ocupación.

        For example:
            Pescador - Pesc.
            Cocinero - Coc.
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
    abbreviation = models.CharField(
        max_length=20,
        unique=True,
        db_index=True,
        validators=[
            MinLengthValidator(1),
            MaxLengthValidator(20),
        ], 
        help_text= 'Abbreviation | Abreviación'
    )
    slug = models.SlugField(
        editable=False, 
        max_length=255,
        unique=True, 
        db_index=True 
    )

    def __str__(self):
        return '%s - %s' %(self.get_name(), self.get_abbreviation())

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.get_name())
        else:
            slug = slugify(self.get_name())
            if self.slug != slug:
                self.slug = slug
        super(EmployeePosition, self).save(*args, **kwargs)

    #Setter
    def set_name(self, name):
        self.name = name
    
    def set_abbreviation(self, abbreviation):
        self.abbreviation = abbreviation
    
    #Getter
    def get_name(self):
        return self.name
   
    def get_abbreviation(self):
        return self.abbreviation

    class Meta:
        db_table = 'occupation_types'
        ordering = ['name', 'abbreviation']
        verbose_name = 'Occupation Type'
        verbose_name_plural = 'Occupation Types'