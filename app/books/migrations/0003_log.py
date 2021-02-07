# Generated by Django 3.1.5 on 2021-02-07 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20210131_1133'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=500)),
                ('method', models.CharField(max_length=32)),
                ('time', models.PositiveIntegerField()),
            ],
        ),
    ]
