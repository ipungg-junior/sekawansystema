# Generated by Django 4.2.6 on 2023-12-14 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0005_supportform_alter_users_first_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='supportform',
            old_name='desc',
            new_name='message',
        ),
    ]