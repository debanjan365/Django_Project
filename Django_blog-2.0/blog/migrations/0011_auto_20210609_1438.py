# Generated by Django 2.1.5 on 2021-06-09 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20210609_1409'),
    ]

    operations = [
        migrations.CreateModel(
            name='Forms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profession', models.CharField(max_length=20)),
                ('fname', models.CharField(max_length=20)),
                ('lname', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('iname', models.CharField(max_length=30)),
                ('comment', models.TextField(max_length=300)),
            ],
        ),
        migrations.DeleteModel(
            name='Form',
        ),
    ]
