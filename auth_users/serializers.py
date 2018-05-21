#!/usr/bin/python3
# -*- encoding: utf-8 -*-
from django.conf.urls import url, include
from rest_framework import serializers
from django.contrib.auth.models import Group
from .models import AuthUser


# Serializers define the API representation.
class AuthUserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        fields = ['id', 'url', 'username', 'email', 'password', 'is_active', 'is_staff', 'is_superuser']
        read_only_fields = ['is_staff', 'is_superuser']
        write_only_fields = ['password']


class GroupModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'url', 'name')