# Generated by Django 2.1.5 on 2021-06-09 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20210609_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='fname',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='form',
            name='lname',
            field=models.CharField(max_length=300),
        ),
    ]
