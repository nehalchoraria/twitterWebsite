# Generated by Django 2.1.5 on 2019-01-29 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='parent',
            field=models.IntegerField(),
        ),
    ]
