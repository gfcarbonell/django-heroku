#!/usr/bin/python3
# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import Entity


@admin.register(Entity)
class EntityAdmin(admin.ModelAdmin):
	list_display = ['entity_class', 'entity_type', 'entity_activity', 'name', 'slogan', 'initials', 'logo']
	search_fields  = ['name', 'initials', 'id']
	fieldsets = (
        ('Entity Info', {'fields':('entity_class', 'entity_type', 'entity_activity', 'name', 'slogan', 'initials', 'logo')}),
    )
	class Meta:
		model = Entity