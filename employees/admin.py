#!/usr/bin/python3
# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
	list_display = ['auth_user_profile', 'active']
	search_fields  = ['auth_user_profile',]
	fieldsets = (
        ('Employee Info', {'fields':('auth_user_profile',)}),
    )
	class Meta:
		model = Employee