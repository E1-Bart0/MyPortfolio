# Generated by Django 3.1.5 on 2021-02-01 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20210126_2150'),
    ]

    operations = [
        migrations.AddField(
            model_name='players',
            name='lead',
            field=models.BooleanField(default=False),
        ),
    ]
