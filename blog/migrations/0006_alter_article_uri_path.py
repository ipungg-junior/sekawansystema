# Generated by Django 4.2.6 on 2023-11-26 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_article_uri_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='uri_path',
            field=models.CharField(blank=True, default='', max_length=120, null=True),
        ),
    ]
