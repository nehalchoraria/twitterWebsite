# Generated by Django 2.1.5 on 2019-01-29 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0002_auto_20190129_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='parent',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
