# Generated by Django 2.1.5 on 2022-01-29 11:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicifyapp', '0012_auto_20220129_1634'),
    ]

    operations = [
        migrations.CreateModel(
            name='catalog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('catalog_File', models.FileField(blank=True, null=True, upload_to='catalog/')),
            ],
        ),
        migrations.AlterField(
            model_name='blog_post',
            name='time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 1, 29, 17, 32, 51, 291442)),
        ),
        migrations.AlterField(
            model_name='blogs_comments',
            name='time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 1, 29, 17, 32, 51, 293468)),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 1, 29, 17, 32, 51, 288449)),
        ),
        migrations.AlterField(
            model_name='posted_jobs',
            name='post_date',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 1, 29, 17, 32, 51, 287453)),
        ),
    ]