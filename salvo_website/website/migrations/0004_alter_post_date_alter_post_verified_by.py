# Generated by Django 5.2rc1 on 2025-04-06 15:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_alter_post_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2025, 4, 6, 21, 22, 15, 894872)),
        ),
        migrations.AlterField(
            model_name='post',
            name='verified_by',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
