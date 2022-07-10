# Generated by Django 3.2.9 on 2022-07-09 23:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='URL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('http_status', models.SmallIntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('check_interval', models.SmallIntegerField(choices=[(5, 'Every 5 minutes'), (15, 'Every 15 minutes'), (30, 'Every 30 minutes'), (24, 'Every 24 hours')])),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='urls', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'URL',
                'verbose_name_plural': 'URLs',
                'ordering': ['-created'],
            },
        ),
    ]