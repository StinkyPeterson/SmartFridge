# Generated by Django 4.1.3 on 2022-12-19 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smartfridge', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listofproduct',
            name='in_fridge',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
