# Generated by Django 4.1.5 on 2023-02-20 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_pagegenerator_alter_news_alt'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='is_draft',
            field=models.BooleanField(default=False),
        ),
    ]