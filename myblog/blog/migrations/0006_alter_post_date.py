# Generated by Django 4.2.4 on 2023-08-29 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(verbose_name='Дата публикации'),
        ),
    ]
