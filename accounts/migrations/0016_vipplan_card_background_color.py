# Generated by Django 5.0 on 2024-02-19 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_licence_remove_vipplan_all_licence_activate_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='vipplan',
            name='card_background_color',
            field=models.CharField(choices=[('gold', 'gold'), ('silver', 'silver'), ('bronze', 'bronze'), ('none', 'none')], default='none', max_length=255, verbose_name='عنوان'),
        ),
    ]
