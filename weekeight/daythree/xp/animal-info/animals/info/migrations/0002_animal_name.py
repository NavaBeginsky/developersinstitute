# Generated by Django 3.1 on 2020-08-05 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
