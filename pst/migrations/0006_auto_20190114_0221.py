# Generated by Django 2.1.4 on 2019-01-14 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pst', '0005_auto_20190112_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
