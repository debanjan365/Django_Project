# Generated by Django 2.0 on 2021-06-06 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20191015_0853'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='emp_image',
            field=models.ImageField(default='SOME STRING', upload_to='upload/'),
        ),
    ]