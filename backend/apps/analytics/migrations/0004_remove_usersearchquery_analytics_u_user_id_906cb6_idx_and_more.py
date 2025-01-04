# Generated by Django 5.1.4 on 2025-01-02 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0003_usersearchquery_category'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='usersearchquery',
            name='analytics_u_user_id_906cb6_idx',
        ),
        migrations.RemoveField(
            model_name='usersearchquery',
            name='device_info',
        ),
        migrations.RemoveField(
            model_name='usersearchquery',
            name='location',
        ),
        migrations.RemoveField(
            model_name='usersearchquery',
            name='session_id',
        ),
        migrations.RemoveField(
            model_name='usersearchquery',
            name='user_id',
        ),
        migrations.AddIndex(
            model_name='usersearchquery',
            index=models.Index(fields=['category'], name='analytics_u_categor_2a3ae6_idx'),
        ),
    ]
