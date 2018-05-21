#!/usr/bin/python3
# -*- encoding: utf-8 -*-
from django.db import models
from django.template.defaultfilters import slugify
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.core.validators import MaxLengthValidator
from django.core.validators import MinLengthValidator


# Create your models here.
class EntityActivity(models.Model):
    '''
        This Class: <EntityActivity> is for to identify the activity that an entity belongs.
        Esta Clase: <EntidadActividad> es para identificar la actividad que pertenece una entidad.

        For example:
            Textile | Textil
            Telecommunication | Telecomunicación 
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

    slug = models.SlugField(
        editable=False, 
        max_length=255,
        unique=True, 
        db_index=True 
    )

    def __str__(self):
        return self.get_name()

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.get_name())
        else:
            slug = slugify(self.get_name())
            if self.slug != slug:
                self.slug = slug
        super(EntityActivity, self).save(*args, **kwargs)

    #Setter
    def set_name(self, name):
        self.name = name
    
    #Getter
    def get_name(self):
        return self.name

    class Meta:
        db_table = 'entity_activities'
        ordering = ['name']
        verbose_name = 'Entity Activity'
        verbose_name_plural = 'Entity Activities'