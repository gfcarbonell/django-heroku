#!/usr/bin/python3
# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

from django.template.defaultfilters import slugify
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.core.validators import MaxLengthValidator
from django.core.validators import MinLengthValidator
from django.core.validators import EmailValidator


# Create your models here.
class UserManager(BaseUserManager):
	
    def _create_user(self, username, email, password, **extra_fields):
        if not username:
            raise ValueError('the given username must be set')
        email = self.normalize_email(email)
        user = self.model(username = username, email = email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_active', False)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)
	
    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        if extra_fields.get('is_active') is not True:
            raise ValueError('User must have is_active=True.')
        if extra_fields.get('is_staff') is not True:
            raise ValueError('User must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('User must have is_superuser=True.')
        return self._create_user(username, email, password, **extra_fields)


class AuthUser(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(
        max_length=100,
        unique=True,
        db_index=True,
        validators=[
            MinLengthValidator(2),
            MaxLengthValidator(50),
        ]
    )

    email = models.EmailField(
        max_length=100,
        unique=True,
        db_index=True,
        validators=[
            EmailValidator(),
            MinLengthValidator(3),
            MaxLengthValidator(50),
        ]
    )
    
    slug = models.SlugField(
        editable=False, 
        max_length=255,
        unique=True, 
        db_index=True 
    )
    
    is_active = models.BooleanField(default=True)
    is_staff  = models.BooleanField(default=True)

    #date_joined = models.DateTimeField(auto_now=True, auto_now_add=True)
    
    objects = UserManager()
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email',]

    def __str__(self):
        return self.get_username()

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.get_username())
        else:
            slug = slugify(self.get_username())
            if self.slug != slug:
                self.slug = slug
        super(AuthUser, self).save(*args, **kwargs)

    #Setter
    def get_short_name(self):
        return self.username
        
    def set_username(self, username):
        self.username = username
        
    def set_email(self, email):
        self.email = email

    #Getter 
    def get_username(self):
        return self.username

    def get_email(self):
        return self.email
    
    class Meta:
        db_table = 'auth_users'
        ordering = ('username', 'email')
        verbose_name = 'Auth User'
        verbose_name_plural = 'Auth Users'