# Generated by Django 2.1.5 on 2019-04-17 10:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reste', '0003_delete_currentremainders'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='addremainders',
            new_name='Remainders',
        ),
    ]
