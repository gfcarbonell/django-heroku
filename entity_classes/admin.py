#!/usr/bin/python3
# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import EntityClass


@admin.register(EntityClass)
class EntityClassAdmin(admin.ModelAdmin):
	list_display = ['entity_scope', 'name',]
	search_fields  = ['name', 'id']
	fieldsets = (
        ('Entity Class', {'fields':('entity_scope', 'name',)}),
    )
	class Meta:
		model = EntityClass