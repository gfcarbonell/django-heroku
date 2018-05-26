# Generated by Django 2.0.5 on 2018-05-21 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='instruction_level',
            field=models.CharField(choices=[('Sin nivel', 'Sin nivel'), ('Pre escolar', 'Pre escolar'), ('Primario', 'Primario'), ('Secundario', 'Secundario'), ('Superior', 'Superior')], default='', help_text='Instruction level | Nivel de instrucción', max_length=11),
            preserve_default=False,
        ),
    ]
