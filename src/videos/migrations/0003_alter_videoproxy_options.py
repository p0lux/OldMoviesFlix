# Generated by Django 3.2.9 on 2021-12-06 21:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0002_videoproxy'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='videoproxy',
            options={'verbose_name': 'Published video', 'verbose_name_plural': 'Published videos'},
        ),
    ]
