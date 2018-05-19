#!/usr/bin/python3
# -*- encoding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import AuthUser


@admin.register(AuthUser)
class UsuarioAdmin(UserAdmin):
	list_display = ('username', 'email', 'is_active', 'is_staff', 'is_superuser', 'password')
	search_fields  = ['username', 'email', 'id']
	fieldsets = (
        ('User Info', {'fields':('username', 'password', 'email',)}),

        ('Permissions', {'fields':('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )

	class Meta:
		model = AuthUser