# Generated by Django 3.1 on 2020-08-29 15:47

import annoying.fields
from django.conf import settings
from django.db import migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_profile', '0006_auto_20200825_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofilepic',
            name='user',
            field=annoying.fields.AutoOneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]