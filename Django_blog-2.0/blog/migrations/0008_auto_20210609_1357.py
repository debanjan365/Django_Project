# Generated by Django 2.1.5 on 2021-06-09 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20210609_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='contact',
            field=models.CharField(max_length=20),
        ),
    ]
