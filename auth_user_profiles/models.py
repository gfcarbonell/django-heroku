# Create your models here.
#!/usr/bin/python3
# -*- encoding: utf-8 -*-
from django.db import models
from persons.models import Person
from auth_users.models import AuthUser
from contact_information.models import ContactInformation
from extra_information.models import ExtraInformation
from collectionfield.models import CollectionField


# Create your models here.
class AuthUserProfile(Person):
    
    user = models.OneToOneField(
        AuthUser, 
        unique=True,
        db_index=True,
        on_delete=models.CASCADE
    )

    contact_information = models.ManyToManyField(
        ContactInformation,
        blank=True
    )

    extra_information = models.ForeignKey(
        ExtraInformation,
        null=True,
        blank=True, 
        on_delete=models.SET_NULL
    )

    active = models.BooleanField(
        default=True
    )

    #Setter
    def set_user(self, user):
       self.user = user 
    
    def set_contact_information(self, contact_information):
        self.contact_information = contact_information 
    
    def set_extra_information(self, extra_information):
        self.extra_information = extra_information 
    
    def set_active(self, active):
        self.active = active 
    
    #Getter
    def get_user(self, user):
        return self.user 

    def get_contact_information(self):
        return self.contact_information

    def get_extra_information(self):
        return self.extra_information 
    
    def get_active(self):
        return self.active 

    class Meta:
        db_table = 'auth_user_profiles'
        verbose_name = 'Auth User Profile'
        verbose_name_plural = 'Auth User Profiles'