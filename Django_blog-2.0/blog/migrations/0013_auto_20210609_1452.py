# Generated by Django 2.1.5 on 2021-06-09 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20210609_1448'),
    ]

    operations = [
        migrations.RenameField(
            model_name='form',
            old_name='profession',
            new_name='contact',
        ),
    ]
