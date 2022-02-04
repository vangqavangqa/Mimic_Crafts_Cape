# Generated by Django 2.1.5 on 2022-01-31 18:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicifyapp', '0019_auto_20220201_0011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_post',
            name='time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 1, 0, 16, 30, 78969)),
        ),
        migrations.AlterField(
            model_name='blogs_comments',
            name='time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 1, 0, 16, 30, 79965)),
        ),
        migrations.AlterField(
            model_name='newsletter_table',
            name='time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 1, 0, 16, 30, 80963)),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 2, 1, 0, 16, 30, 76971)),
        ),
        migrations.AlterField(
            model_name='posted_jobs',
            name='post_date',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 2, 1, 0, 16, 30, 76971)),
        ),
    ]