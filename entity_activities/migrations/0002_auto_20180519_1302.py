# Generated by Django 2.0.5 on 2018-05-19 18:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entity_activities', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entityactivity',
            name='name',
            field=models.CharField(db_index=True, help_text='Name | Nombre', max_length=100, unique=True, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(100)]),
        ),
    ]