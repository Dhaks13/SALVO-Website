# Generated by Django 5.2rc1 on 2025-04-03 17:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_alter_member_join_date_alter_post_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2025, 4, 3, 22, 45, 13, 749733)),
        ),
    ]
