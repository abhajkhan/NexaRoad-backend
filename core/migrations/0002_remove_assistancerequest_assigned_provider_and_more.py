# Generated by Django 5.1.5 on 2025-02-04 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assistancerequest',
            name='assigned_provider',
        ),
        migrations.RemoveField(
            model_name='assistancerequest',
            name='user',
        ),
    ]
