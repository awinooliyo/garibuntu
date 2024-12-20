# Generated by Django 4.2.16 on 2024-10-28 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='forumthread',
            options={'permissions': [('can_lock_thread', 'Can lock threads'), ('can_delete_thread', 'Can delete threads'), ('can_create_thread', 'Can create threads')]},
        ),
        migrations.AddField(
            model_name='forumpost',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='forumreply',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='forumthread',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='forumthread',
            name='is_locked',
            field=models.BooleanField(default=False),
        ),
    ]
