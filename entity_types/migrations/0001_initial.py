# Generated by Django 2.0.5 on 2018-05-19 15:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EntityType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, unique=True, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(100)])),
                ('initials', models.CharField(db_index=True, max_length=20, unique=True, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(20)])),
                ('slug', models.SlugField(editable=False, max_length=255, unique=True)),
            ],
            options={
                'verbose_name': 'Entity Type',
                'db_table': 'entity_types',
                'verbose_name_plural': 'Entity Types',
            },
        ),
    ]