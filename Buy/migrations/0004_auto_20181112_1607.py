# Generated by Django 2.1.2 on 2018-11-12 10:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Buy', '0003_match_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticket',
            old_name='emailId',
            new_name='userId',
        ),
    ]
