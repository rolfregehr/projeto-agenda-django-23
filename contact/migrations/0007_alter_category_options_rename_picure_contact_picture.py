# Generated by Django 5.1.3 on 2024-12-04 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0006_contact_owner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='picure',
            new_name='picture',
        ),
    ]
