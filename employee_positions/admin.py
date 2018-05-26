#!/usr/bin/python3
# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import EmployeePosition


@admin.register(EmployeePosition)
class EmployeePositionAdmin(admin.ModelAdmin):
	list_display = ['name', 'abbreviation']
	search_fields  = ['name', 'abbreviation', 'id']
	fieldsets = (
        ('Entity Type', {'fields':('name', 'abbreviation')}),
    )
	class Meta:
		model = EmployeePosition