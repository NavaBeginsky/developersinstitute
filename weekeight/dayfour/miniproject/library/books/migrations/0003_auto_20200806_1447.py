# Generated by Django 3.1 on 2020-08-06 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20200806_1339'),
    ]

    operations = [
        migrations.RenameField(
            model_name='currentlycheckedoutby',
            old_name='person',
            new_name='book',
        ),
    ]