# Generated by Django 5.0.4 on 2024-04-07 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profileuser',
            name='img',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
