# Generated by Django 4.1 on 2022-08-31 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_role_user_delete_todo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='title',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='cat',
            new_name='role',
        ),
        migrations.RemoveField(
            model_name='user',
            name='content',
        ),
    ]