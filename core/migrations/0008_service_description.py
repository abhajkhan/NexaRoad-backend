# Generated by Django 5.1.5 on 2025-02-05 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_service_alter_serviceprovider_service_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='description',
            field=models.TextField(default='at your service'),
            preserve_default=False,
        ),
    ]
