# Generated by Django 2.1.5 on 2019-04-17 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reste', '0002_currentremainders'),
    ]

    operations = [
        migrations.DeleteModel(
            name='currentremainders',
        ),
    ]