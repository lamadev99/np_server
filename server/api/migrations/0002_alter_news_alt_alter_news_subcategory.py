# Generated by Django 4.1.5 on 2023-02-20 05:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='alt',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='news',
            name='subCategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.subcategory'),
        ),
    ]
