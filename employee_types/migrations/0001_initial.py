# Generated by Django 2.0.5 on 2018-05-21 17:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, help_text='Name | Nombre', max_length=100, unique=True, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(100)])),
                ('initials', models.CharField(db_index=True, help_text='Initials | Iniciales', max_length=20, unique=True, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(20)])),
                ('slug', models.SlugField(editable=False, max_length=255, unique=True)),
            ],
            options={
                'verbose_name': 'Employee Type',
                'verbose_name_plural': 'Employee Types',
                'db_table': 'employee_types',
                'ordering': ['name', 'initials'],
            },
        ),
    ]
