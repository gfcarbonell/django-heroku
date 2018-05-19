#!/usr/bin/python3
# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import EntityActivity


@admin.register(EntityActivity)
class EntityActivityAdmin(admin.ModelAdmin):
	list_display = ('name',)
	search_fields  = ['name', 'id']
	fieldsets = (
        ('Entity Activity', {'fields':('name',)}),
    )
	class Meta:
		model = EntityActivity