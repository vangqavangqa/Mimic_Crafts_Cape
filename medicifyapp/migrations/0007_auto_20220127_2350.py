# Generated by Django 2.1.5 on 2022-01-27 17:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicifyapp', '0006_auto_20220121_2232'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brands',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Brand_name', models.CharField(max_length=500)),
                ('Brand_discription', models.TextField()),
                ('Brand_image', models.ImageField(blank=True, default='', null=True, upload_to='uploads/category_img')),
            ],
            options={
                'verbose_name_plural': 'Brands',
            },
        ),
        migrations.AlterModelOptions(
            name='bennar',
            options={'verbose_name_plural': 'Bennar'},
        ),
        migrations.AlterModelOptions(
            name='blog_post',
            options={'verbose_name_plural': 'Blog Post'},
        ),
        migrations.AlterModelOptions(
            name='blogs_comments',
            options={'verbose_name_plural': 'Blogs Comments'},
        ),
        migrations.AlterModelOptions(
            name='categories',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='contact_table',
            options={'verbose_name_plural': 'Contact Table'},
        ),
        migrations.AlterModelOptions(
            name='discount_coupon',
            options={'verbose_name_plural': 'Discount Coupon'},
        ),
        migrations.AlterModelOptions(
            name='job_post_status',
            options={'verbose_name_plural': 'Job Post Status'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name_plural': 'All Orders'},
        ),
        migrations.AlterModelOptions(
            name='posted_jobs',
            options={'verbose_name_plural': 'Posted Jobs'},
        ),
        migrations.AlterModelOptions(
            name='product_details',
            options={'verbose_name_plural': 'Product Table'},
        ),
        migrations.AddField(
            model_name='categories',
            name='Category_image',
            field=models.ImageField(blank=True, default='', null=True, upload_to='uploads/category_img'),
        ),
        migrations.AddField(
            model_name='categories',
            name='category_discription',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subcategory',
            name='Subcategory_discription',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subcategory',
            name='Subcategory_image',
            field=models.ImageField(blank=True, default='', null=True, upload_to='uploads/Subcategory_img'),
        ),
        migrations.AlterField(
            model_name='blog_post',
            name='time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 1, 27, 23, 50, 16, 240649)),
        ),
        migrations.AlterField(
            model_name='blogs_comments',
            name='time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 1, 27, 23, 50, 16, 240649)),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 1, 27, 23, 50, 16, 235638)),
        ),
        migrations.AlterField(
            model_name='posted_jobs',
            name='post_date',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 1, 27, 23, 50, 16, 235638)),
        ),
    ]
