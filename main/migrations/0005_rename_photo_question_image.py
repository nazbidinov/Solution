# Generated by Django 5.0.3 on 2024-03-05 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_rename_sciences_science'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='photo',
            new_name='image',
        ),
    ]
