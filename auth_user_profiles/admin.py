#!/usr/bin/python3
# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import AuthUserProfile


@admin.register(AuthUserProfile)
class AuthUserProfileAdmin(admin.ModelAdmin):
    list_display = ('get_full_name', 'birthday', 'gender', 'marital_status', 'blood_group', 'user', 'active')
    search_fields = ['name', 'last_name', 'mother_last_name', 'user__username', 'id']
    filter_horizontal = ['contact_information']
    
    class Meta:
        model = AuthUserProfile