# -*- encoding: utf-8 -*-
from django.shortcuts import render
from rest_framework import viewsets

from .models import AuthUser
from django.contrib.auth.models import Group
from .serializers import AuthUserModelSerializer, GroupModelSerializer


# Create your views here.
# ViewSets define the view behavior.
class AuthUserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = AuthUser.objects.all()
    serializer_class = AuthUserModelSerializer
    queryset_detail  = queryset.prefetch_related('groups__permissions')

    
class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupModelSerializer