#!/usr/bin/python3
# -*- encoding: utf-8 -*-
from django.db import models
from django.template.defaultfilters import slugify
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.core.validators import MaxLengthValidator
from django.core.validators import MinLengthValidator
from django.core.validators import EmailValidator
from .enums import InstructionLevel
from employee_types.models  import EmployeeType
from employee_positions.models  import EmployeePosition
from occupation_types.models import OccupationType
from auth_user_profiles.models import AuthUserProfile


# Create your models here.
class Employee(models.Model):
    INSTRUCTION_LEVEL_CHOICES = [(instruction_level.value, instruction_level.value) for instruction_level in InstructionLevel]
    
    employee_type = models.ForeignKey(
        EmployeeType,
        on_delete=models.CASCADE,
        help_text= 'Employee type | Tipo de empleado'
    )
    employee_position = models.ForeignKey(
        EmployeePosition,
        on_delete=models.CASCADE,
        help_text= 'Employee position | Tipo de posición (cargo)'
    )
    auth_user_profile = models.OneToOneField(
        AuthUserProfile,
        on_delete=models.CASCADE,
        unique=True,
        db_index=True,
        help_text='Auth user profile | Auth perfil de usuario',
    )
    instruction_level = models.CharField(
        choices = INSTRUCTION_LEVEL_CHOICES,
        max_length=11,
        help_text= 'Instruction level | Nivel de instrucción'
    )
    occupation_type = models.ManyToManyField(
        OccupationType,
        blank=True, 
        help_text='Occupation Type |Tipo de ocupación'
    )
    start_date_contract = models.DateField(
        
    )
    end_date_contract = models.DateField(
        
    )
    active = models.BooleanField(
        default=True,
        help_text='Active | Activo',
    )
    slug = models.SlugField(
        editable=False, 
        max_length=255,
        unique=True, 
        db_index=True 
    )

    def __str__(self):
        return self.get_auth_user_profile().get_full_name()

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.get_auth_user_profile().get_full_name())
        else:
            slug = slugify(self.get_auth_user_profile().get_full_name())
            if self.slug != slug:
                self.slug = slug
        super(Employee, self).save(*args, **kwargs)

    #Setter
    def set_auth_user_profile(self, auth_user_profile):
        self.auth_user_profile = auth_user_profile

    #Getter 
    def get_auth_user_profile(self):
        return self.auth_user_profile
    
    class Meta:
        db_table = 'employees'
        ordering = ['auth_user_profile']
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'