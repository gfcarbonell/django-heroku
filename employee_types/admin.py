#!/usr/bin/python3
# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import EmployeeType


@admin.register(EmployeeType)
class EmployeeTypeAdmin(admin.ModelAdmin):
	list_display = ['name', 'initials']
	search_fields  = ['name', 'initials', 'id']
	fieldsets = (
        ('Entity Type', {'fields':('name', 'initials')}),
    )
	class Meta:
		model = EmployeeType