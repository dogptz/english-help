# Generated by Django 2.1.4 on 2018-12-20 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tppo', '0004_choice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='votes',
        ),
        migrations.AddField(
            model_name='choice',
            name='stat',
            field=models.BooleanField(default=False),
        ),
    ]
