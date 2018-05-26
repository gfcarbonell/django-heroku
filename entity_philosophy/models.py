#!/usr/bin/python3
# -*- encoding: utf-8 -*-
from django.db import models
from django.template.defaultfilters import slugify
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.core.validators import MaxLengthValidator
from django.core.validators import MinLengthValidator


# Create your models here.
class EntityPhilosophy(models.Model):
    '''
        This Class: <EntityPhilosophy> contains the philosophy of a entity
        Esta clase: <FilosofíaEntidad> contiene la filosofía de una entidad
    '''
    mission = models.TextField(
        null=True,
        blank=True
    )
    vission = models.TextField(
        null=True,
        blank=True
    )
    slug = models.SlugField(
        editable=False, 
        max_length=255,
        unique=True, 
        db_index=True 
    )
    
    def __str__(self):
        return self.get_entity_philosophy_info()

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.get_entity_philosophy_info())
        else:
            slug = slugify(self.get_entity_philosophy_info())
            if self.slug != slug:
                self.slug = slug
        super(EntityPhilosophy, self).save(*args, **kwargs)

    #Setter
    def set_mission(self, mission):
        self.mission = mission
    
    def set_vission(self, vission):
        self.vission = vission
    
    #Getter
    def get_mission(self):
        return self.mission
   
    def get_vission(self):
        return self.vission

    def get_entity_philosophy_info(self):
        data = '%s | %s' %(self.get_mission(), self.get_vission())
        info = (data[:20] + '...') if len(data) > 20 else data
        return info


    class Meta:
        db_table = 'entity_philosophies'
        ordering = ['mission', 'vission']
        verbose_name = 'Entity Philosophy'
        verbose_name_plural = 'Entity Philosophies'