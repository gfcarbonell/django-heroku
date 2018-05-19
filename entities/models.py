#!/usr/bin/python3
# -*- encoding: utf-8 -*-
from django.db import models
from django.template.defaultfilters import slugify
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.core.validators import MaxLengthValidator
from django.core.validators import MinLengthValidator


from entity_activities.models import EntityActivity
from entity_classes.models import EntityClass
from entity_types.models import EntityType


# Create your models here.
class Entity(models.Model):
    
    entity_class = models.ForeignKey(
        EntityClass,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    entity_type = models.ForeignKey(
        EntityType,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    entity_activity = models.ForeignKey(
        EntityActivity, 
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    
    name = models.CharField(
        max_length=100,
        unique=True,
        db_index=True,
        validators=[
            MinLengthValidator(1),
            MaxLengthValidator(100),
        ]
    )

    slogan = models.CharField(
        max_length=100,
        unique=True,
        null=True, 
        blank=True,
        db_index=True,
        validators=[
            MinLengthValidator(1),
            MaxLengthValidator(100),
        ]
    )

    initials = models.CharField(
        max_length=20,
        unique=True,
        null=True, 
        blank=True,
        db_index=True,
        validators=[
            MinLengthValidator(1),
            MaxLengthValidator(20),
        ]
    )

    logo = models.ImageField(
        upload_to='image/entities/', 
        null=True, 
        blank=True,
        default=None
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
        super(Entity, self).save(*args, **kwargs)
    
    def set_name(self, name):
        self.name = name 

    def get_name(self):
        return self.name
        
    class Meta:
        db_table = 'entities'
        verbose_name = 'Entity'
        verbose_name_plural = 'Entities'