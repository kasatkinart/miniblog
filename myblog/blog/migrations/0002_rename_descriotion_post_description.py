# Generated by Django 4.2.4 on 2023-08-29 01:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='descriotion',
            new_name='description',
        ),
    ]
