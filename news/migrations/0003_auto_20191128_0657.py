# Generated by Django 2.2.7 on 2019-11-28 04:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20191128_0631'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='newsm',
            unique_together={('title', 'content')},
        ),
    ]