# Generated by Django 3.2.9 on 2021-12-13 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0007_auto_20211213_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video_id',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]