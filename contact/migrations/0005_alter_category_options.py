# Generated by Django 5.1.3 on 2024-11-27 00:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0004_category_contact_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Categoria', 'verbose_name_plural': 'Categorias'},
        ),
    ]
