# Generated by Django 2.1.5 on 2022-01-28 18:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicifyapp', '0009_auto_20220129_0025'),
    ]

    operations = [
        migrations.AddField(
            model_name='brands',
            name='Brand_discription',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='blog_post',
            name='time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 1, 29, 0, 36, 23, 590999)),
        ),
        migrations.AlterField(
            model_name='blogs_comments',
            name='time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 1, 29, 0, 36, 23, 591995)),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 1, 29, 0, 36, 23, 589002)),
        ),
        migrations.AlterField(
            model_name='posted_jobs',
            name='post_date',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 1, 29, 0, 36, 23, 588004)),
        ),
    ]
