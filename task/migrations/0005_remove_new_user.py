# Generated by Django 4.1.4 on 2022-12-23 20:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0004_alter_new_id_new_alter_newid_new_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='new',
            name='user',
        ),
    ]