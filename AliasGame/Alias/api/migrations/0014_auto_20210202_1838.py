# Generated by Django 3.1.5 on 2021-02-02 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_leader'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leader',
            name='user',
        ),
        migrations.AddField(
            model_name='leader',
            name='player',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.players'),
            preserve_default=False,
        ),
    ]
