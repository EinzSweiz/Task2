# Generated by Django 5.1.2 on 2024-10-15 22:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0002_rename_image_image_image_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='image_url',
            new_name='image',
        ),
    ]
