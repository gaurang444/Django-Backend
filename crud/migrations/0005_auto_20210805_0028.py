# Generated by Django 2.2.11 on 2021-08-04 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0004_auto_20210805_0027'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='last_updatedat',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_created_at',
        ),
    ]