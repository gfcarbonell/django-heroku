#!/usr/bin/python3
# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
	list_display = ['auth_user_profile', 'start_date_contract', 'end_date_contract','active']
	search_fields  = ['auth_user_profile',]
	filter_horizontal = ['occupation_type']
	fieldsets = (
        ('Employee Info', {'fields':('employee_type', 'employee_position', 'auth_user_profile',)}),
		('Contract Info', {'fields':('start_date_contract', 'end_date_contract')}),
		('Study Center', {'fields':('instruction_level', 'occupation_type')}),
		('Activation', {'fields':('active',)}),
    )
	class Meta:
		model = Employee