# Generated by Django 3.2.14 on 2022-07-30 04:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('txn_trackerApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
