# Generated by Django 3.1.5 on 2021-03-27 16:02

import books.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20210316_0825'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover',
            field=models.FileField(default=None, null=True, upload_to=books.models.book_upload_cover),
        ),
    ]
