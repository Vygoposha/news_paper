# Generated by Django 3.2 on 2021-06-06 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_auto_20210606_2014'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='subscribers',
            new_name='subscriber',
        ),
    ]