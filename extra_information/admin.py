#!/usr/bin/python3
# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import ExtraInformation


@admin.register(ExtraInformation)
class ExtraInformationAdmin(admin.ModelAdmin):
	fieldsets = (
        ('Extra Info', {'fields':('description', 'observation')}),
    )

	class Meta:
		model = ExtraInformation