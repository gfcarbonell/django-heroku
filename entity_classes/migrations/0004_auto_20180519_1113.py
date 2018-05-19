# Generated by Django 2.0.5 on 2018-05-19 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entity_classes', '0003_auto_20180519_1050'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entityclass',
            options={'ordering': ['entity_scope', 'name'], 'verbose_name': 'Entity Class', 'verbose_name_plural': 'Entity Classes'},
        ),
        migrations.RemoveField(
            model_name='entityclass',
            name='scope_entity',
        ),
        migrations.AddField(
            model_name='entityclass',
            name='entity_scope',
            field=models.CharField(choices=[('Actividad Econónica', 'Actividad Econónica'), ('Ámbito de Operación', 'Ámbito de Operación'), ('Composición del Capital', 'Composición del Capital'), ('Forma Jurídica', 'Forma Jurídica'), ('Tamaño', 'Tamaño')], db_index=True, default='', help_text='Scope entity | Ámbito Entidad', max_length=50),
            preserve_default=False,
        ),
    ]