# Generated by Django 2.1.3 on 2019-06-02 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tppo', '0011_auto_20190510_1630'),
    ]

    operations = [
        migrations.CreateModel(
            name='theme_new',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme_name', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='theme',
        ),
        migrations.RenameField(
            model_name='users',
            old_name='name',
            new_name='user',
        ),
    ]
