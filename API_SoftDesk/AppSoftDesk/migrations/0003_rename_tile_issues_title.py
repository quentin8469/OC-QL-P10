# Generated by Django 3.2.6 on 2021-08-13 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppSoftDesk', '0002_auto_20210806_0303'),
    ]

    operations = [
        migrations.RenameField(
            model_name='issues',
            old_name='tile',
            new_name='title',
        ),
    ]
