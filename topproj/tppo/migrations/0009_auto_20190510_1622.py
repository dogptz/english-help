# Generated by Django 2.1.3 on 2019-05-10 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tppo', '0008_auto_20190510_1619'),
    ]

    operations = [
        migrations.CreateModel(
            name='keks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keke', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='themes',
        ),
    ]
