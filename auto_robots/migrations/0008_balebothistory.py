# Generated by Django 4.2.6 on 2023-11-04 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auto_robots', '0007_remove_metapost_message_action'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaleBotHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_id', models.CharField(blank=True, max_length=255, null=True, verbose_name='chat id')),
                ('message_id', models.CharField(blank=True, max_length=255, null=True, verbose_name='message id')),
                ('metapost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auto_robots.metapost', verbose_name='metapost')),
            ],
            options={
                'verbose_name': 'تاریخچه ربات بله',
                'verbose_name_plural': 'تاریخچه ربات های بله',
            },
        ),
    ]
