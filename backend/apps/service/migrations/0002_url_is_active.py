# Generated by Django 3.2.9 on 2022-07-10 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
