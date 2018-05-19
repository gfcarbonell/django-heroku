#!/usr/bin/python3
# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import ContactInformation


@admin.register(ContactInformation)
class ContactInformationAdmin(admin.ModelAdmin):
	list_display = ('email', 'cell_phone', 'telephone')
	search_fields = ['email', 'cell_phone', 'telephone', 'id']
	
	class Meta:
		model = ContactInformation
	
