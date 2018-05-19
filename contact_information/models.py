# Create your models here.
#!/usr/bin/python3
# -*- encoding: utf-8 -*-
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class ContactInformation(models.Model):
   
    email = models.EmailField(
        unique=True,
        db_index=True,
    )

    cell_phone = PhoneNumberField(
        unique=True,
        db_index=True,
    )

    telephone = PhoneNumberField(
        unique=True,
        db_index=True,
    )
    
    slug = models.SlugField(
        editable=False, 
        max_length=255,
        unique=True, 
        db_index=True 
    )

    def __str__(self):
        return self.get_contact_info()

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.get_contact_info())
        else:
            slug = slugify(self.get_contact_info())
            if self.slug != slug:
                self.slug = slug
        super(ContactInformation, self).save(*args, **kwargs)
    
    #Setter
    def set_email(self, email):
        self.email = email 
    
    def set_cell_phone(self, cell_phone):
        self.cell_phone = cell_phone
    
    def set_telephone(self, telephone):
        self.telephone = telephone

    #Getter
    def get_email(self):
        return self.email 
    
    def get_cell_phone(self):
        return self.cell_phone
    
    def get_telephone(self):
        return self.telephone

    def get_contact_info(self):
        return '%s | %s | %s' %(self.get_email(), self.get_cell_phone(), self.get_telephone())

    class Meta:
        db_table = 'contact_information'
        verbose_name = 'Contact Information'
        verbose_name_plural = 'Contact Information'