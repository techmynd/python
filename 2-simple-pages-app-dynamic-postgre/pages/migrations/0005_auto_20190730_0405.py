# Generated by Django 2.2.3 on 2019-07-29 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_page_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='image',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
    ]
