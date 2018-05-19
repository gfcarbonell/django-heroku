#!/usr/bin/python3
# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import Entity


@admin.register(Entity)
class EntityAdmin(admin.ModelAdmin):
	class Meta:
		model = Entity