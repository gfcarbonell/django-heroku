# Generated by Django 2.0.5 on 2018-05-21 04:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authuser',
            name='email',
            field=models.EmailField(db_index=True, max_length=100, unique=True, validators=[django.core.validators.EmailValidator(), django.core.validators.MinLengthValidator(3), django.core.validators.MaxLengthValidator(100)]),
        ),
        migrations.AlterField(
            model_name='authuser',
            name='username',
            field=models.CharField(db_index=True, max_length=100, unique=True, validators=[django.core.validators.MinLengthValidator(2), django.core.validators.MaxLengthValidator(100)]),
        ),
    ]
