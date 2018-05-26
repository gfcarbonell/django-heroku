# Generated by Django 2.0.5 on 2018-05-21 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('occupation_types', '0001_initial'),
        ('employees', '0002_employee_instruction_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='occupation_type',
            field=models.ManyToManyField(blank=True, help_text='Occupation Type |Tipo de ocupación', to='occupation_types.OccupationType'),
        ),
    ]