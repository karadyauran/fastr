# Generated by Django 5.0.4 on 2024-04-08 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_app', '0002_profileuser_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='profileuser',
            name='location',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
