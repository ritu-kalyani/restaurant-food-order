# Generated by Django 2.2.8 on 2021-04-09 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='UserData',
        ),
    ]