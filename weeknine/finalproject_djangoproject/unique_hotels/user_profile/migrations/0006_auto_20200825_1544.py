# Generated by Django 3.1 on 2020-08-25 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0005_auto_20200825_0809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofilepic',
            name='profile_pic',
            field=models.ImageField(default='avatar.png', upload_to='profile_pictures'),
        ),
    ]
