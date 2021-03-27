# Generated by Django 3.1.5 on 2021-03-21 20:28

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20210321_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.FileField(default=None, null=True, upload_to=accounts.models.user_upload_avatar),
        ),
    ]