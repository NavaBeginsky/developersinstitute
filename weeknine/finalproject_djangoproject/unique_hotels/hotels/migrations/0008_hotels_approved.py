# Generated by Django 3.1 on 2020-08-21 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0007_auto_20200821_1647'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotels',
            name='approved',
            field=models.BooleanField(default=True),
        ),
    ]