# Generated by Django 4.2.6 on 2023-11-12 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calendar_event', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='event_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='event_name',
            new_name='name',
        ),
    ]
