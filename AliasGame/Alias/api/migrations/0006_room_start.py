# Generated by Django 3.1.5 on 2021-01-19 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20210119_1425'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='start',
            field=models.BooleanField(default=False),
        ),
    ]
