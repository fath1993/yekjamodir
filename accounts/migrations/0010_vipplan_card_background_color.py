# Generated by Django 4.2.7 on 2023-11-28 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_alter_vipplan_options_vipplan_all_licence_activate_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='vipplan',
            name='card_background_color',
            field=models.CharField(choices=[('gold', 'gold'), ('silver', 'silver'), ('boronz', 'boronz'), ('none', 'none')], default='none', max_length=255, verbose_name='عنوان'),
        ),
    ]
