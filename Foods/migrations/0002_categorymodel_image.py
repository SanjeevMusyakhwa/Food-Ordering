# Generated by Django 5.1.5 on 2025-01-26 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Foods', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorymodel',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='categories/'),
        ),
    ]
