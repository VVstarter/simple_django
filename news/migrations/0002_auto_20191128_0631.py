# Generated by Django 2.2.7 on 2019-11-28 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsm',
            name='date',
            field=models.CharField(max_length=100, verbose_name='Дата публикации'),
        ),
    ]
