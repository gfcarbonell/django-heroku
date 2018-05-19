#!/usr/bin/python3
# -*- encoding: utf-8 -*-
from django.db import models


# Create your models here.
class ExtraInformation(models.Model):
   
    description = models.TextField(
        null=True,
        blank=True
    )

    observation = models.TextField(
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
        return self.get_extra_info()

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.get_extra_info())
        else:
            slug = slugify(self.get_extra_info())
            if self.slug != slug:
                self.slug = slug
        super(ExtraInformation, self).save(*args, **kwargs)

    #Setter
    def set_description(self, description):
        self.description = description
    
    def set_observation(self, observation):
        self.observation = observation
    
    #Getter
    def get_description(self):
        return self.description
   
    def get_observation(self):
        return self.observation

    def get_extra_info(self):
        data = '%s | %s' %(self.get_description(), self.get_observation())
        info = (data[:20] + '...') if len(data) > 20 else data
        return info

    class Meta:
        db_table = 'extra_info'
        verbose_name = 'Extra Information'
        verbose_name_plural = 'Extra Information'