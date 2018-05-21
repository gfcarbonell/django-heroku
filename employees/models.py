#!/usr/bin/python3
# -*- encoding: utf-8 -*-
from django.db import models
from django.template.defaultfilters import slugify
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.core.validators import MaxLengthValidator
from django.core.validators import MinLengthValidator
from django.core.validators import EmailValidator

from auth_user_profiles.models import AuthUserProfile

# Create your models here.
class Employee(models.Model):

    auth_user_profile = models.OneToOneField(
        AuthUserProfile,
        on_delete=models.CASCADE,
        unique=True,
        db_index=True,
        help_text='Auth user profile | Auth perfil de usuario',
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