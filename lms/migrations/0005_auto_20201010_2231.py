# Generated by Django 3.1.2 on 2020-10-10 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0004_auto_20201010_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='Quantity',
            field=models.IntegerField(default=0),
        ),
    ]
