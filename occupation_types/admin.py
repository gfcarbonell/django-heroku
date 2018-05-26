#!/usr/bin/python3
# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import OccupationType


@admin.register(OccupationType)
class OccupationTypeAdmin(admin.ModelAdmin):
	list_display = ['name', 'abbreviation',]
	search_fields  = ['name', 'id']
	fieldsets = (
        ('Occupation Type', {'fields':('name', 'abbreviation',)}),
    )
	class Meta:
		model = OccupationType