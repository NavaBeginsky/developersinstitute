# Generated by Django 3.1 on 2020-08-19 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0004_auto_20200819_0901'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotels',
            name='unique_snippet',
            field=models.CharField(default='afdsf', max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hotels',
            name='details',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='location',
            name='lat',
            field=models.DecimalField(decimal_places=7, max_digits=10),
        ),
        migrations.AlterField(
            model_name='location',
            name='lon',
            field=models.DecimalField(decimal_places=7, max_digits=10),
        ),
    ]
