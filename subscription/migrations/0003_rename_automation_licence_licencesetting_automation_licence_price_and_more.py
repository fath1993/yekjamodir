# Generated by Django 5.0 on 2024-05-13 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0002_licencesetting'),
    ]

    operations = [
        migrations.RenameField(
            model_name='licencesetting',
            old_name='automation_licence',
            new_name='automation_licence_price',
        ),
        migrations.RenameField(
            model_name='licencesetting',
            old_name='blog_licence',
            new_name='blog_licence_price',
        ),
        migrations.RenameField(
            model_name='licencesetting',
            old_name='financial_licence',
            new_name='financial_licence_price',
        ),
        migrations.RenameField(
            model_name='licencesetting',
            old_name='send_message',
            new_name='send_message_price',
        ),
        migrations.RenameField(
            model_name='licencesetting',
            old_name='social_licence',
            new_name='social_licence_price',
        ),
        migrations.RenameField(
            model_name='licencesetting',
            old_name='warehouse_licence',
            new_name='warehouse_licence_price',
        ),
    ]
