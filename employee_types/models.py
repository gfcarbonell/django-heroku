#!/usr/bin/python3
# -*- encoding: utf-8 -*-
from django.db import models
from django.template.defaultfilters import slugify
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.core.validators import MaxLengthValidator
from django.core.validators import MinLengthValidator


# Create your models here.
class EmployeeType(models.Model):
    '''
        This Class: <EmployeeType> is for to identify the type that an employee belongs.
        Esta Clase: <TipoEmpleado> es para identificar el tipo que pertenece un empleado.

        For example:
           
            Contrato Administrativo de Servicios - C.A.S.
            Freelancer - F 
            Prestaciones de Servicio - P.S.

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
        super(EmployeeType, self).save(*args, **kwargs)

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
        db_table = 'employee_types'
        ordering = ['name', 'initials']
        verbose_name = 'Employee Type'
        verbose_name_plural = 'Employee Types'