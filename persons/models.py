#!/usr/bin/python3
# -*- encoding: utf-8 -*-
from django.db import models
from persons.enums import Gender, MaritalStatus, BloodGroup

from django.template.defaultfilters import slugify
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.core.validators import MaxLengthValidator
from django.core.validators import MinLengthValidator


# Create your models here.
class Person(models.Model):
    '''
        This Class:<Person> is abstract and contains basic personal information.
        Esta Clase:<Persona> es abstracto y contiene la información personal básica.
    '''
    CHOICES_GENDER = [(gender.value, gender.value) for gender in Gender]
    CHOICES_MARITAL_STATUS = [(marital_status.value, marital_status.value) for marital_status in MaritalStatus]
    CHOICES_BLOOD_GROUP = [(blood_group.value, blood_group.value) for blood_group in BloodGroup]
    
    name = models.CharField(
        max_length=100,
        unique=True,
        db_index=True,
        validators=[
            MinLengthValidator(1),
            MaxLengthValidator(100),
        ],
        help_text='Name | Nombre'
    )
    last_name = models.CharField(
        max_length=100,
        unique=True,
        db_index=True,
        validators=[
            MinLengthValidator(1),
            MaxLengthValidator(100),
        ],
        help_text='Last name | Apellido paterno'
    )
    mother_last_name = models.CharField(
        max_length=100,
        unique=True,
        db_index=True,
        validators=[
            MinLengthValidator(1),
            MaxLengthValidator(100),
        ], 
        help_text='Mother last name | Apellido materno'
    )   
    birthday = models.DateField(
        help_text='birthday | Fecha nacimiento'
    )
    gender = models.CharField(
        choices = CHOICES_GENDER,
        max_length=9,
        help_text='Gender | Género'
    )
    marital_status = models.CharField(
        choices = CHOICES_MARITAL_STATUS,
        max_length=9,
        help_text='Marital status | Estado marital o civil'
    )
    blood_group = models.CharField(
        choices = CHOICES_BLOOD_GROUP,
        max_length=9,
        null=True,
        blank=True,
        help_text='Blood group | Grupo sanguíneo'
    )  
    photography = models.ImageField(
        upload_to='image/persons/', 
        null=True, 
        blank=True,
        default=None, 
        help_text='Photography | Fotografía'
    ) 
    slug = models.SlugField(
        editable=False, 
        max_length=255,
        unique=True, 
        db_index=True 
    )
    
    def __str__(self):
        return self.get_full_name()

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.get_full_name())
        else:
            slug = slugify(self.get_full_name())
            if self.slug != slug:
                self.slug = slug
        super(Person, self).save(*args, **kwargs)

    def get_full_name(self):
        return '%s %s, %s' % (self.get_last_name(), self.get_mother_last_name(), self.get_name())

    #Setter
    def set_name(self, name):
        self.name = name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def set_mother_last_name(self, mother_last_name):
        self.mother_last_name = mother_last_name

    def set_birthday(self, birthday):
        self.birthday = birthday

    def set_gender(self, gender):
        self.gender = gender

    def set_marital_status(self, marital_status):
        self.marital_status = marital_status

    def set_blood_group(self, blood_group):
        self.blood_group = blood_group

    #Getter 
    def get_name(self):
        return self.name

    def get_last_name(self):
        return self.last_name

    def get_mother_last_name(self):
        return self.mother_last_name

    def get_birthday(self):
        return self.birthday 

    def get_gender(self):
        return self.gender

    def get_marital_status(self):
        return self.marital_status 

    def get_blood_group(self):
        return self.blood_group 

    class Meta:
        abstract = True