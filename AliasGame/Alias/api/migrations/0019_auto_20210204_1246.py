# Generated by Django 3.1.5 on 2021-02-04 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_auto_20210204_1200'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='team_1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='room',
            name='team_2',
            field=models.IntegerField(default=0),
        ),
    ]