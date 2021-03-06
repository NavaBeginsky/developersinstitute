# Generated by Django 3.1 on 2020-08-06 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='books',
            field=models.ManyToManyField(to='books.LibraryBooks'),
        ),
        migrations.RemoveField(
            model_name='author',
            name='name',
        ),
        migrations.AddField(
            model_name='author',
            name='name',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
