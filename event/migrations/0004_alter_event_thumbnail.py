# Generated by Django 5.1 on 2024-08-15 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_remove_event_host'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='media/event_thumbnails'),
        ),
    ]
