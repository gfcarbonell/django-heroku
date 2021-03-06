# Generated by Django 2.0.5 on 2018-05-21 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth_user_profiles', '0002_auto_20180521_1153'),
        ('employee_positions', '0001_initial'),
        ('employee_types', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date_contract', models.DateField()),
                ('end_date_contract', models.DateField()),
                ('active', models.BooleanField(default=True, help_text='Active | Activo')),
                ('slug', models.SlugField(editable=False, max_length=255, unique=True)),
                ('auth_user_profile', models.OneToOneField(help_text='Auth user profile | Auth perfil de usuario', on_delete=django.db.models.deletion.CASCADE, to='auth_user_profiles.AuthUserProfile')),
                ('employee_position', models.ForeignKey(help_text='Employee position | Tipo de posición (cargo)', on_delete=django.db.models.deletion.CASCADE, to='employee_positions.EmployeePosition')),
                ('employee_type', models.ForeignKey(help_text='Employee type | Tipo de empleado', on_delete=django.db.models.deletion.CASCADE, to='employee_types.EmployeeType')),
            ],
            options={
                'verbose_name': 'Employee',
                'verbose_name_plural': 'Employees',
                'db_table': 'employees',
                'ordering': ['auth_user_profile'],
            },
        ),
    ]
