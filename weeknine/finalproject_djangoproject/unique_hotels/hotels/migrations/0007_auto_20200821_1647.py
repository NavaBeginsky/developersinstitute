# Generated by Django 3.1 on 2020-08-21 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0006_auto_20200819_0925'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='hotels',
            unique_together={('name', 'location')},
        ),
    ]